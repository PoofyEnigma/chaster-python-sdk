from . import conversation
import datetime
import json
from . import lock
import logging
import requests
from requests.adapters import HTTPAdapter, Retry
from . import shared_lock
import time
from types import SimpleNamespace
from urllib.parse import urlparse, urljoin
from . import user
from . import extensions


class ChasterAPI:
    def __init__(self, bearer, user_agent='ChasterPythonSDK/1.0', delay=5, root_api='https://api.chaster.app/',
                 request_logger=None):
        self.logger = logging.getLogger(self.__class__.__name__)
        self.root_api = urlparse(root_api)
        self.delay = delay
        self.session = requests.Session()
        self.session.headers = {
            'Authorization': f'Bearer {bearer}',
            'accept': 'application/json',
            'Content-Type': 'application/json',
            'User-Agent': user_agent
        }
        retries = Retry(total=3,
                        backoff_factor=0.1,
                        status_forcelist=[500, 502, 503, 504])
        retries.backoff_jitter = 0.01
        self.session.mount('http://', HTTPAdapter(max_retries=retries))
        self.session.mount('https://', HTTPAdapter(max_retries=retries))
        if request_logger is None:
            self._request_logger = self._request_logger_default
        else:
            self._request_logger = request_logger

    def _request_logger_default(self, response: requests.models.Response, *args, **kwargs):
        self.logger.info(
            f'{response.status_code} {response.request.url} {response.request.method} {len(response.content)}')
        self.logger.info(f'{response.text}')
        if 200 <= response.status_code < 300:
            return

        self.logger.error(f'{response.text}')
        match response.status_code:
            # Bad Request
            case 400:
                pass
            # Unauthenticated
            case 401:
                pass
            # Unauthorized
            case 403:
                pass
            # Not found
            case 404:
                pass
            # Too Many Requests
            case 429:
                time.sleep(30)
            case 503:
                pass

        # Other 400
        if 400 <= response.status_code < 500:
            return
        # Other 500s
        if 500 <= response.status_code < 600:
            self.logger.error(f'{response.text}')
            return

    def _post_request_handler(self, response: requests.models.Response, *args, **kwargs):
        time.sleep(self.delay)

    def _get(self, path: str) -> requests.models.Response:
        response = self.session.get(urljoin(self.root_api.geturl(), path),
                                    hooks={'response': [self._post_request_handler, self._request_logger]})
        return response

    def _post(self, path: str, data) -> requests.models.Response:
        response = self.session.post(urljoin(self.root_api.geturl(), path),
                                     data=json.dumps(data),
                                     hooks={'response': [self._post_request_handler, self._request_logger]})
        return response

    def _put(self, path: str, data) -> requests.models.Response:
        response = self.session.put(urljoin(self.root_api.geturl(), path),
                                    data=json.dumps(data), hooks={'response': self._post_request_handler})
        return response

    def _delete(self, path: str):
        response = self.session.delete(urljoin(self.root_api.geturl(), path),
                                       hooks={'response': self._post_request_handler})
        return response

    """
    Shared Locks
    """

    def get_shared_locks(self, status: str = 'active') -> tuple[requests.models.Response, list[shared_lock.SharedLock]]:
        path = 'locks/shared-locks'
        if status != '':
            if status == 'active' or status == 'archived':
                path = f'locks/shared-locks?status={status}'
            else:
                raise ValueError('status must be one of: active, archived, or empty string')

        response = self._get(path)

        data = None
        if response.status_code == 200:
            x = response.json(object_hook=lambda d: SimpleNamespace(**d))
            data = shared_lock.shared_locks(x)

        return response, data

    def create_shared_lock(self, create: shared_lock.CreateSharedLock) -> tuple[
        requests.models.Response, shared_lock.IdResponse]:

        create.validate()
        response = self._post('/locks/shared-locks', create.dump())
        data = None
        if response.status_code == 201:
            x = response.json(object_hook=lambda d: SimpleNamespace(**d))
            data = shared_lock.IdResponse().update(x)
        return response, data

    def get_shared_lock_details(self, shared_lock_id: str) -> tuple[
        requests.models.Response, shared_lock.SharedLock]:

        response = self._get(f'/lock/shared-locks/{shared_lock_id}')
        data = None
        if response.status_code == 200:
            x = response.json(object_hook=lambda d: SimpleNamespace(**d))
            data = shared_lock.SharedLock().update(x)
        return response, data

    def update_shared_lock(self, shared_lock_id: str, update: shared_lock.CreateSharedLock) -> requests.models.Response:
        update.validate()
        return self._put(f'/lock/shared-lock/{shared_lock_id}', update.dump())

    def archive_shared_lock(self, shared_lock_id: str):
        return self._post(f'/locks/shared-locks/{shared_lock_id}/archive', {})

    def check_if_favorited(self, shared_lock_id: str) -> tuple[requests.models.Response, bool]:
        response = self._get(f'/shared-locks/{shared_lock_id}/favorite')
        data = None
        if response.status_code == 200:
            data = response.json()['favorite']
        return response, data

    def favorite(self, shared_lock_id: str) -> requests.models.Response:
        return self._put(f'/shared-locks/{shared_lock_id}/favorite', data={})

    def remove_favorite(self, shared_lock_id: str) -> requests.models.Response:
        return self._delete(f'/shared-locks/{shared_lock_id}/favorite')

    # shared-locks
    def get_favorited_shared_locks(self, limit: int = 15, lastId: str = None) -> tuple[
        requests.models.Response, shared_lock.PageinatedSharedLockList]:
        if limit < 0:
            raise ValueError('limit cannot be zero')
        response = self._post('favorites/shared-locks', {'limit': limit, 'lastId': lastId})

        data = None
        if response.status_code == 201:
            y = response.json()
            x = response.json(object_hook=lambda d: SimpleNamespace(**d))
            data = shared_lock.PageinatedSharedLockList().update(x)
        return response, data

    """
    Locks
    """

    def get_locks(self, status: str = 'active') -> tuple[requests.models.Response, list[lock.Lock]]:
        path = '/locks'
        if status != '':
            if status == 'active' or status == 'archived':
                path = f'/locks?status={status}'
            else:
                raise ValueError('status must be one of: active, archived, or empty string')

        response = self._get(path)
        data = None
        if response.status_code == 200:
            data = response.json(object_hook=lambda d: SimpleNamespace(**d))
            data = lock.update(data)
        return response, data

    def get_lock_details(self, lock_id: str) -> tuple[requests.models.Response, lock.Lock]:
        response = self._get(f'/locks/{lock_id}')

        data = None
        if response.status_code == 200:
            data = response.json(object_hook=lambda d: SimpleNamespace(**d))
            data = lock.Lock().update(data)
        return response, data

    def archive_lock(self, lock_id: str) -> requests.models.Response:
        return self._post(f'/locks/{lock_id}', {})

    def archive_lock_as_keyholder(self, lock_id: str) -> requests.models.Response:
        return self._post(f'/locks/{lock_id}/archive/keyholder', {})

    def update_lock_time(self, lock_id: str, time_seconds: int):
        return self._post(f'locks/{lock_id}/update-time', {'duration': time_seconds})

    def freeze(self, lock_id: str, freeze: bool) -> requests.models.Response:
        return self._post(f'locks/{lock_id}/freeze', data={"isFrozen": freeze})

    def unlock(self, lock_id: str) -> requests.models.Response:
        return self._post(f'/locks/{lock_id}/unlock', {})

    def lock_settings(self, lock_id: str, display_remaining_time: bool,
                      hide_time_logs: bool) -> requests.models.Response:
        return self._post(f'locks/{lock_id}/settings', data={
            "displayRemainingTime": display_remaining_time,
            "hideTimeLogs": hide_time_logs
        })

    def set_max_limit_date(self, lock_id: str, max_limit_date: datetime.datetime,
                           disable_max_time_limit: bool) -> requests.models.Response:
        return self._post(f'locks/{lock_id}/max-limit-date', data={
            "maxLimitDate": max_limit_date.isoformat(),
            "disableMaxLimitDate": disable_max_time_limit
        })

    def set_keyholder_as_trusted(self, lock_id: str) -> requests.models.Response:
        return self._post(f'locks/{lock_id}/trust-keyholder', data={})

    def get_lock_combination(self, lock_id: str) -> tuple[requests.models.Response, any]:
        response = self._get(f'/locks/{lock_id}/combination')

        data = None
        if response.status_code == 200:
            data = response.json(object_hook=lambda d: SimpleNamespace(**d))
            data = user.LockCombination().update(data)
        return response, data

    def get_lock_history(self, lock_id: str, extension: str = None, limit: int = None, last_id: str = None) -> tuple[
        requests.models.Response, lock.PageinatedLockHistory]:
        data = {}
        if extension is not None and extension != '':
            data['extension'] = extension
        if limit is not None:
            data['limit'] = extension
        if last_id is not None:
            data['lastId'] = extension
        response = self._post(f'locks/{lock_id}/history', data=data)

        data = None
        if response.status_code == 201:
            data = response.json(object_hook=lambda d: SimpleNamespace(**d))
            data = lock.PageinatedLockHistory().update(data)
        return response, data

    def is_test_lock(self, lock_id) -> requests.models.Response:
        return self._put(f'locks/{lock_id}/is-test-lock', data={})

    # TODO: The reason for this API is unclear. Does it send more data than what is already present in the lock?
    def get_extension_information(self, lock_id, extension_id) -> tuple[
        requests.models.Response, lock.ExtensionInformation]:
        response = self._get(f'locks/{lock_id}/extensions/{extension_id}')

        data = None
        if response.status_code == 201:
            data = response.json(object_hook=lambda d: SimpleNamespace(**d))
            data = lock.ExtensionInformation().update(data)
        return response, data

    # TODO: Flush out data?
    def trigger_extension_actions(self, lock_id, extension_id, data):
        return self._post(f'locks/{lock_id}/extensions/{extension_id}/action', data=data)

    """
    Lock Creation
    """

    def create_personal_lock(self, self_lock: lock.Lock) -> tuple[requests.models.Response, lock.LockId]:
        response = self._post('locks', data=self_lock.dump())

        data = None
        if response.status_code == 201:
            data = response.json(object_hook=lambda d: SimpleNamespace(**d))
            data = lock.LockId().update(data)
        return response, data

    def add_extensions(self, lock_id: str, ext: extensions.Extensions) -> requests.models.Response:
        return self._post(f'locks/{lock_id}/extensions', data=ext.dump())

    def create_lock_from_shared_lock(self, shared_lock_id: str, lock_details: lock.LockInfo) -> tuple[
        requests.models.Response, lock.LockId]:
        response = self._post(f'public-locks/{shared_lock_id}/create-lock', data=lock_details.dump())

        data = None
        if response.status_code == 201:
            data = response.json(object_hook=lambda d: SimpleNamespace(**d))
            data = lock.LockId().update(data)
        return response, data

    """
    profile
    """

    def passthrough(self, obj):
        return obj

    def _tester_get_wrapper(self, path, func):
        response = self._get(path)
        data = None
        if response.status_code == 200:
            data = response.json(object_hook=lambda d: SimpleNamespace(**d))
            data = func(data)
        return response, data

    def get_user_locks(self, user_id: str) -> tuple[requests.models.Response, list[lock.Lock]]:
        return self._tester_get_wrapper(f'locks/user/{user_id}', lock.update)

    # TODO: Need to flush out return obj
    def get_profile(self, user_id: str) -> tuple[requests.models.Response, any]:
        return self._tester_get_wrapper(f'users/profile/by-id/{user_id}', self.passthrough)

    # TODO: Need to flush out return obj
    def find_profile(self, username: str) -> tuple[requests.models.Response, any]:
        return self._tester_get_wrapper(f'users/profile/{username}', self.passthrough)

    # TODO: Need to flush out return obj
    def find_profile_detailed(self, username: str) -> tuple[requests.models.Response, any]:
        return self._tester_get_wrapper(f'users/profile/{username}/details', self.passthrough)

    # TODO: Need to flush out return obj
    def get_badges(self) -> tuple[requests.models.Response, any]:
        return self._tester_get_wrapper('users/badge/count', self.passthrough)

    # TODO: Need to flush out return obj
    def update_profile(self) -> tuple[requests.models.Response, any]:
        return self._tester_get_wrapper('auth/profile/update', self.passthrough)

    # TODO: Need to flush out return obj
    def get_your_profile(self) -> tuple[requests.models.Response, any]:
        return self._tester_get_wrapper('auth/profile', self.passthrough)

    """
    Files
    """
    # /files/upload
    # /files/filekey

    """
    Combinations
    """
    # /combinaions/image
    # /combinations/code

    """
    Extensions
    """

    # TODO: Need to flush out return obj
    def get_all_known_extensions(self) -> tuple[requests.models.Response, any]:
        return self._tester_get_wrapper('extensions', self.passthrough)

    """
    Session Offer
    """

    # TODO: Flush out return obj
    # TODO: Need to flush out input obj
    def create_keyholding_offer(self, lock_id, keyholder) -> requests.models.Response:
        return self._post(f'session-offer/lock/{lock_id}', data=keyholder)

    def accept_keyholding_request(self, offer_token) -> requests.models.Response:
        return self._get(f'session-offer/token/{offer_token}/accept')

    def get_keyholding_offers(self, lock_id) -> tuple[requests.models.Response, any]:
        return self._tester_get_wrapper(f'session-offer/lock/{lock_id}/status', self.passthrough)

    # session-offer/token/offertoken
    def retrieve_keyholder_request_lock_info(self, offer_token) -> tuple[requests.models.Response, any]:
        return self._tester_get_wrapper(f'session-offer/token/{offer_token}', self.passthrough)

    # session-offer/sessionRequestId
    def handle_keyholding_offer(self, session_request_id, do_accept) -> requests.models.Response:
        return self._post(f'session-offer/{session_request_id}', data={'accept': do_accept})

    # session-offer/sessionRequestId/archive
    def archive_keyholding_offer(self, session_request_id) -> requests.models.Response:
        return self._get(f'session-offer/{session_request_id}/archive')

    # session-offer/requests
    def get_keyholding_offers_from_wearers(self) -> tuple[requests.models.Response, any]:
        return self._tester_get_wrapper('session-offer/requests', self.passthrough)

    """
    Messaging
    """

    def get_conversations(self):
        response = requests.get('https://api.chaster.app/conversations?limit=50&status=approved',
                                headers={
                                    'accept': 'application/json',
                                    'Authorization': 'Bearer 8N3d2pzH9n4PlYgm9DH27KuFecC2rM17',
                                })
        return response.json()

    def create_conversation(self, user, message) -> tuple[requests.models.Response, conversation.Conversation]:
        response = requests.post('https://api.chaster.app/conversations',
                                 headers={
                                     'accept': '*/*',
                                     'Authorization': 'Bearer 8N3d2pzH9n4PlYgm9DH27KuFecC2rM17',
                                     'Content-Type': 'application/json'
                                 }, data=json.dumps({'users': [user],
                                                     'type': "private",
                                                     "message": message}))

        data = None
        if response.status_code == 201:
            x = response.json(object_hook=lambda d: SimpleNamespace(**d))
            data = conversation.Conversation().update(x)

        return response, data

    def get_conversation(self, user_id) -> tuple[requests.models.Response, conversation.Conversation]:
        response = requests.get(f'https://api.chaster.app/conversations/by-user/{user_id}',
                                headers={
                                    'accept': 'application/json',
                                    'Authorization': 'Bearer 8N3d2pzH9n4PlYgm9DH27KuFecC2rM17',
                                })

        data = None
        if response.status_code == 200:
            x = json.loads(json.dumps(response.json()), object_hook=lambda d: SimpleNamespace(**d))
            data = conversation.Conversation().update(x)

        return response, data

    def post_message(self, conversation_id, message):
        data = '{"message": "' + message + '"}'
        json.loads(data)
        response = requests.post(f'https://api.chaster.app/conversations/{conversation_id}',
                                 headers={
                                     'accept': 'application/json',
                                     'Authorization': 'Bearer 8N3d2pzH9n4PlYgm9DH27KuFecC2rM17',
                                     'Content-Type': 'application/json'
                                 }, data=data)

        return response, response.json()

    def get_conversation_messages(self, conversation_id) -> tuple[
        requests.models.Response, conversation.ConversationMessages]:
        response = requests.get(f'https://api.chaster.app/conversations/{conversation_id}/messages?limit=50',
                                headers={
                                    'accept': 'application/json',
                                    'Authorization': 'Bearer 8N3d2pzH9n4PlYgm9DH27KuFecC2rM17',
                                })
        data = None
        if response.status_code == 200:
            x = response.json(object_hook=lambda d: SimpleNamespace(**d))
            data = conversation.ConversationMessages().update(x)

        return response, data

    def set_conversation_status(self, conversation_id, status: str) -> requests.models.Response:
        return self._put(f'conversations/{conversation_id}/status', data={'status': status})

    # /conversation/conversationid/unread
    def set_conversation_unread(self, conversation_id, unread: bool):
        return self._put(f'conversations/{conversation_id}/status', data={'unread': unread})

    # TODO: Finish stub
    # TODO: Find a query builder object
    def find_message_in_a_conversation(self, conversation_id, limit: int, last_id: str):
        return self._tester_get_wrapper(f'conversations/{conversation_id}/message?limit={limit}&lastI{last_id}|',
                                        self.passthrough)

    """
    Extensions - Temporary Opening
    """

    """
    Community Events
    """

    """
    Partner Extensions
    """
    # TODO: Gain access

    """
    Settings
    """

    """
    Users
    """

    """
    Keyholder
    """

    def post_keyholder_locks_search(self) -> tuple[any, lock.LockedUsers]:
        response = requests.post('https://api.chaster.app/keyholder/locks/search',
                                 headers={
                                     'accept': '*/*',
                                     'Authorization': 'Bearer 8N3d2pzH9n4PlYgm9DH27KuFecC2rM17',
                                     'Content-Type': 'application/json'
                                 }, data=json.dumps({'criteria': {},
                                                     'status': "locked",
                                                     "page": 0,
                                                     "limit": 10}))
        data = None
        if response.status_code == 201:
            x = response.json(object_hook=lambda d: SimpleNamespace(**d))
            data = lock.LockedUsers().update(x)
        return response, data

    """
    Reports
    """

    """
    Partner Configurations
    """

    """
    Public Locks
    """

    """
    Extensions - Verification Picture
    """


class MockChasterData:
    user_locks = {}

    def __init__(self):
        pass


class MockChasterAPI(ChasterAPI):
    def __init__(self, mock_chaster_data: MockChasterData, user_id):
        super().__init__('')
        self.session.get = self.m_get
        self.user_id = user_id
        self.mock_chaster_data = mock_chaster_data

    def m_get(self, url, **kwargs) -> requests.models.Response:
        url = urlparse(url)
        response = requests.models.Response()
        if url.path == 'locks/shared-locks?status=archived':
            pass
        if url.path == 'locks/shared-locks?status=active':
            pass
        if url.path == 'locks/shared-locks':
            pass
        for hook in kwargs['hooks']:
            hook(response)

        return response
