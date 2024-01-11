from . import conversation
import datetime
import json
from . import lock
import logging
import requests
from requests.adapters import HTTPAdapter, Retry
from . import triggers
import time
from types import SimpleNamespace
from urllib.parse import urlparse, urljoin
from . import user
from . import extensions


class ChasterAPI:

    def __init__(self, bearer, user_agent='ChasterPythonSDK/1.0', delay=5, root_api='https://api.chaster.app/',
                 request_logger=None):
        """
        Not thread safe. Will need a ChasterAPI object per thread.
        :param bearer:
        :param user_agent:
        :param delay:
        :param root_api:
        :param request_logger:
        """
        self.logger = logging.getLogger(self.__class__.__name__)
        self.root_api = urlparse(root_api)
        self.delay = delay
        self.session = requests.Session()  # generally not multithread safe https://github.com/psf/requests/issues/1871
        self.session.headers = {
            'Authorization': f'Bearer {bearer}',
            'accept': 'application/json',
            'Content-Type': 'application/json',
            'User-Agent': user_agent,
            'Accept-Language': 'en-US,en;q=0.5',
            'Connection': 'keep-alive',
        }
        retries = Retry(total=3,
                        backoff_factor=0.1,
                        status_forcelist=[500, 502, 503, 504],
                        respect_retry_after_header=True)
        retries.backoff_jitter = 0.01
        self.session.mount('http://', HTTPAdapter(max_retries=retries))
        self.session.mount('https://', HTTPAdapter(max_retries=retries))
        if request_logger is None:
            self._request_logger = self._request_logger_default
        else:
            self._request_logger = request_logger

    def _request_logger_default(self, response: requests.models.Response, *args, **kwargs):
        print('?')
        chaster_transaction_id = ''
        if 'x-chaster-transaction-id' in response.headers:
            chaster_transaction_id = response.headers['x-chaster-transaction-id']
            pass

        self.logger.info(
            f'{response.status_code} {response.request.url} {response.request.method} {len(response.content)} {chaster_transaction_id}')
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
        if 'retry-after' in response.headers:
            pass
        if 'x-ratelimit-limit' in response.headers:
            pass
        if 'retry-after' in response.headers:
            # this is honored in the retry object
            pass
        if 'x-ratelimit-limit' in response.headers:
            pass
        if 'x-ratelimit-remaining' in response.headers:
            pass
        if 'x-ratelimit-reset' in response.headers:
            pass
        if 'x-chaster-transaction-id' in response.headers:
            pass

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

    def get_shared_locks(self, status: str = 'active') -> tuple[requests.models.Response, list[lock.SharedLock]]:
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
            data = lock.SharedLock.generate_array(x)

        return response, data

    def create_shared_lock(self, create: lock.CreateSharedLock) -> tuple[
        requests.models.Response, lock.IdResponse]:

        create.validate()
        response = self._post('/locks/shared-locks', create.dump())
        data = None
        if response.status_code == 201:
            x = response.json(object_hook=lambda d: SimpleNamespace(**d))
            data = lock.IdResponse().update(x)
        return response, data

    def get_shared_lock_details(self, shared_lock_id: str) -> tuple[
        requests.models.Response, lock.SharedLock]:

        response = self._get(f'/lock/shared-locks/{shared_lock_id}')
        data = None
        if response.status_code == 200:
            x = response.json(object_hook=lambda d: SimpleNamespace(**d))
            data = lock.SharedLock().update(x)
        return response, data

    def update_shared_lock(self, shared_lock_id: str, update: lock.CreateSharedLock) -> requests.models.Response:
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
        requests.models.Response, lock.PageinatedSharedLockList]:
        if limit < 0:
            raise ValueError('limit cannot be zero')
        response = self._post('favorites/shared-locks', {'limit': limit, 'lastId': lastId})

        data = None
        if response.status_code == 201:
            x = response.json(object_hook=lambda d: SimpleNamespace(**d))
            data = lock.PageinatedSharedLockList().update(x)
        return response, data

    """
    Locks
    """

    def get_locks(self, status: str = 'active') -> tuple[requests.models.Response, list[lock.Lock]]:
        path = '/locks'
        if status != '':
            if status == 'active' or status == 'archived' or status == 'all':
                path = f'/locks?status={status}'
            else:
                raise ValueError('status must be one of: active, archived, all, or empty string')

        response = self._get(path)
        data = None
        if response.status_code == 200:
            data = response.json(object_hook=lambda d: SimpleNamespace(**d))
            data = lock.Lock.generate_array(data)
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
    def get_extension_information(self, lock_id: str, extension_id: str) -> tuple[
        requests.models.Response, lock.ExtensionInformation]:
        response = self._get(f'locks/{lock_id}/extensions/{extension_id}')

        data = None
        if response.status_code == 201:
            data = response.json(object_hook=lambda d: SimpleNamespace(**d))
            data = lock.ExtensionInformation().update(data)
        return response, data

    # TODO: Flush out data?
    def trigger_extension_actions(self, lock_id: str, extension_id: str, data: any) -> requests.models.Response:
        """
        See triggers
        :param lock_id:
        :param extension_id:
        :param data:
        :return:
        """
        return self._post(f'locks/{lock_id}/extensions/{extension_id}/action', data=data)

    """
    Triggers
    """

    def _tester_post_request_helper(self, response, update):
        data = None
        if response.status_code == 201:
            data = response.json(object_hook=lambda d: SimpleNamespace(**d))
            data = update(data)
        return response, data

    def vote_in_share_links(self, lock_id: str, extension_id: str, data: triggers.ShareLinksVote) -> tuple[
        requests.models.Response, triggers.ShareLinksVoteReturn]:
        response = self.trigger_extension_actions(lock_id, extension_id, data)
        return self._tester_post_request_helper(response, triggers.ShareLinksVoteReturn().update)

    def get_share_link_url_to_vote(self, lock_id: str, extension_id: str) -> tuple[
        requests.models.Response, triggers.ShareLinkUrlResponse]:
        data = triggers.ActionRequest()
        data.action = 'getLink'
        response = self.trigger_extension_actions(lock_id, extension_id, data)
        return self._tester_post_request_helper(response, triggers.ShareLinksVoteReturn().update)

    def get_share_link_info(self, lock_id: str, extension_id: str) -> tuple[
        requests.models.Response, triggers.ShareLinkGetInfoResponse]:
        data = triggers.ActionRequest()
        data.action = 'getInfo'
        response = self.trigger_extension_actions(lock_id, extension_id, data)
        return self._tester_post_request_helper(response, triggers.ShareLinkGetInfoResponse().update)

    def place_user_into_pillory(self, lock_id: str, extension_id: str,
                                data: triggers.PilloryParameters) -> requests.models.Response:
        return self.trigger_extension_actions(lock_id, extension_id, data)

    def get_current_pillory_info(self, lock_id: str, extension_id: str) -> tuple[
        requests.models.Response, triggers.PilloryVotes]:
        data = triggers.ActionRequest()
        data.action = 'getStatus'
        response = self.trigger_extension_actions(lock_id, extension_id, data)
        return self._tester_post_request_helper(response, triggers.PilloryVotes().update)

    def unlock_for_hygiene(self, lock_id: str, extension_id: str, is_you: bool) -> requests.models.Response:
        data = triggers.ActionRequest()
        data.action = 'keyholderOpen'
        if is_you:
            data.action = 'submit'
        return self.trigger_extension_actions(lock_id, extension_id, data)

    def roll_dice(self, lock_id: str, extension_id: str) -> tuple[
        requests.models.Response, triggers.DiceRollResult]:
        data = triggers.ActionRequest()
        data.action = 'submit'
        response = self.trigger_extension_actions(lock_id, extension_id, data)
        return self._tester_post_request_helper(response, triggers.DiceRollResult().update)

    def spin_wheel_of_fortune(self, lock_id: str, extension_id: str) -> tuple[
        requests.models.Response, triggers.DiceRollResult]:
        data = triggers.ActionRequest()
        data.action = 'submit'
        response = self.trigger_extension_actions(lock_id, extension_id, data)
        return self._tester_post_request_helper(response, triggers.DiceRollResult().update)

    def request_a_random_task(self, lock_id: str, extension_id: str) -> requests.models.Response:
        data = {"action": "submit", "payload": {"requestVote": False}}
        return self.trigger_extension_actions(lock_id, extension_id, data)

    def community_vote_next_task(self, lock_id: str, extension_id: str, vote_duration: int) -> requests.models.Response:
        data = {"action": "submit", "payload": {"requestVote": True, "voteDuration": vote_duration}}
        return self.trigger_extension_actions(lock_id, extension_id, data)

    def mark_task_done(self, lock_id: str, extension_id: str, succeeded: bool) -> requests.models.Response:
        data = {"action": "completeTask", "payload": {"isCompleted": succeeded}}
        return self.trigger_extension_actions(lock_id, extension_id, data)

    def trigger_new_verification(self, lock_id: str, extension_id: str) -> requests.models.Response:
        data = {"action": "createVerificationRequest", "payload": {}}
        return self.trigger_extension_actions(lock_id, extension_id, data)

    def trigger_guess_the_timer(self, lock_id: str, extension_id: str) -> tuple[
        requests.models.Response, triggers.GuessTheTimerResponse]:
        data = {"action": "createVerificationRequest", "payload": {}}
        response = self.trigger_extension_actions(lock_id, extension_id, data)
        return self._tester_post_request_helper(response, triggers.GuessTheTimerResponse().update)

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
        return self._tester_get_wrapper(f'locks/user/{user_id}', lock.Lock.generate_array)

    def get_profile(self, user_id: str) -> tuple[requests.models.Response, user.User]:
        return self._tester_get_wrapper(f'users/profile/by-id/{user_id}', user.User().update)

    def find_profile(self, username: str) -> tuple[requests.models.Response, user.User]:
        return self._tester_get_wrapper(f'users/profile/{username}', user.User().update)

    def find_profile_detailed(self, username: str) -> tuple[requests.models.Response, user.DetailedUser]:
        return self._tester_get_wrapper(f'users/profile/{username}/details', user.DetailedUser().update)

    def get_badges(self) -> tuple[requests.models.Response, user.Badges]:
        return self._tester_get_wrapper('users/badge/count', user.Badges.update)

    def update_profile(self) -> tuple[requests.models.Response, user.AuthProfile]:
        return self._tester_get_wrapper('auth/profile/update', user.AuthProfile().update)

    def get_your_profile(self) -> tuple[requests.models.Response, user.AuthProfile]:
        return self._tester_get_wrapper('auth/profile', user.AuthProfile().update)

    """
    Files
    """
    # /files/upload
    # /files/filekey

    """
    Combinations
    """
    # /combinations/image
    # /combinations/code

    """
    Extensions
    """

    def get_all_known_extensions(self) -> tuple[requests.models.Response, list[extensions.KnownExtension]]:
        return self._tester_get_wrapper('extensions', extensions.known_extension_list_update)

    """
    Session Offer
    """

    def create_keyholding_offer(self, lock_id, keyholder: str) -> requests.models.Response:
        return self._post(f'session-offer/lock/{lock_id}', data={
            'keyholder': keyholder
        })

    def accept_keyholding_request(self, offer_token: str) -> requests.models.Response:
        return self._get(f'session-offer/token/{offer_token}/accept')

    def get_keyholding_offers(self, lock_id: str) -> tuple[requests.models.Response, list[user.KeyholderOfferEntry]]:
        return self._tester_get_wrapper(f'session-offer/lock/{lock_id}/status', user.keyholder_offer_list_update)

    def retrieve_keyholder_request_lock_info(self, offer_token: str) -> tuple[requests.models.Response, lock.Lock]:
        return self._tester_get_wrapper(f'session-offer/token/{offer_token}', lock.Lock().update)

    def handle_keyholding_offer(self, session_request_id, do_accept) -> requests.models.Response:
        return self._post(f'session-offer/{session_request_id}', data={'accept': do_accept})

    def archive_keyholding_offer(self, session_request_id) -> requests.models.Response:
        return self._get(f'session-offer/{session_request_id}/archive')

    def get_keyholding_offers_from_wearers(self) -> tuple[requests.models.Response, list[user.KeyholderOfferEntry]]:
        return self._tester_get_wrapper('session-offer/requests', user.keyholder_offer_list_update)

    """
    Messaging
    """

    def get_conversations(self, limit: int = 15, status: str = 'approved') -> tuple[
        requests.models.Response, conversation.Conversations]:
        path = 'conversations'
        if limit is not None or status is not None:
            path += "?"
        if limit is not None:
            path += f'limit={limit}&'
        if status is not None:
            path += f'status={status}&'
        return self._tester_get_wrapper(path, conversation.Conversations().update)

    # TODO: Input object? Are there multiple types?
    def create_conversation(self, user_id: str, message: str) -> tuple[
        requests.models.Response, conversation.Conversation]:
        response = self._post('conversations',
                              {'users': [user_id],
                               'type': "private",
                               "message": message})

        return self._tester_post_request_helper(response, conversation.Conversation().update)

    def get_user_conversation(self, user_id: str) -> tuple[requests.models.Response, conversation.Conversation]:
        return self._tester_get_wrapper(f'conversations/by-user/{user_id}', conversation.Conversation().update)

    def post_message(self, conversation_id: str, message: str) -> tuple[requests.models.Response, conversation.Message]:
        response = self._post(f'conversations/{conversation_id}',
                              {"message": message})

        return self._tester_post_request_helper(response, conversation.Message().update)

    def get_conversation(self, conversation_id: str) -> tuple[requests.models.Response, conversation.Conversation]:
        return self._tester_get_wrapper(f'conversations/{conversation_id}', conversation.Conversation().update)

    def set_conversation_status(self, conversation_id, status: str) -> requests.models.Response:
        return self._put(f'conversations/{conversation_id}/status', data={'status': status})

    # /conversation/conversationid/unread
    def set_conversation_unread(self, conversation_id, unread: bool) -> requests.models.Response:
        return self._put(f'conversations/{conversation_id}/status', data={'unread': unread})

    def get_conversation_messages(self, conversation_id: str, limit=15, lastId=None) -> tuple[
        requests.models.Response, conversation.ConversationMessages]:
        path = f'conversations/{conversation_id}/messages?limit={limit}'
        if lastId is not None:
            path += f'&lastId={lastId}'
        return self._tester_get_wrapper(path, conversation.ConversationMessages().update)

    """
    Extensions - Temporary Opening
    """

    def get_temporary_opening_combination(self, lock_id: str) -> tuple[requests.models.Response, user.LockCombination]:
        return self._tester_get_wrapper(f'/extensions/temporary-opening/{lock_id}/combination',
                                        user.LockCombination().update)

    def set_temporary_opening_new_combination(self, lock_id: str, combination_id: str) -> requests.models.Response:
        return self._post(f'/extensions/temporary-opening/{lock_id}/combination', {'combinationId': combination_id})

    def get_temporary_opening_combination_from_action_log(self, action_log_id: str, lock_id: str) -> tuple[
        requests.models.Response, user.LockCombination]:
        return self._tester_get_wrapper(
            f'/extensions/temporary-opening/{lock_id}/action-log/{action_log_id}/combination',
            user.LockCombination().update)

    """
    Community Events
    """

    def get_community_event_categories(self) -> tuple[
        requests.models.Response, user.CommunityEventCategory]:
        return self._tester_get_wrapper('/community-event/categories', user.CommunityEventCategory.generate_array)

    def get_community_event_details(self, date: datetime.datetime = datetime.datetime.now()) -> tuple[
        requests.models.Response, user.CommunityEventDetails]:
        response = self._put(f'/community-event/details', data={'date': date.isoformat()})
        data = None
        if response.status_code == 201:
            x = response.json(object_hook=lambda d: SimpleNamespace(**d))
            data = user.CommunityEventDetails().update(x)
        return response, data

    """
    Partner Extensions
    """
    # TODO: Gain access

    """
    Settings
    """

    def get_app_settings(self) -> tuple[requests.models.Response, user.AppSettings]:
        return self._tester_get_wrapper('/settings', user.AppSettings.update)

    """
    Users
    """

    def search_for_users(self, search: str) -> tuple[requests.models.Response, list[user.User]]:
        response = self._post('users/search/by-username', {'search': search})
        return self._tester_post_request_helper(response, user.User.generate_array)

    def search_for_users_by_discord(self, discord_id: str) -> tuple[requests.models.Response, user.User]:
        return self._tester_get_wrapper(f'users/search/by-discord-id/{discord_id}', user.User().update)

    """
    Keyholder
    """

    status_deserted = 'deserted'
    status_archived = 'archived'
    status_unlocked = 'unlocked'
    status_locked = 'locked'

    def post_keyholder_locks_search(self, page: int = 0, status: str = 'locked', limit: int = 15, criteria: dict = {},
                                    search: str = None) -> tuple[requests.models.Response, lock.LockedUsers]:
        data = {
            'page': page,
            'status': status,
            'limit': limit,
            'criteria': criteria
        }
        if search is not None:
            data['search'] = search

        response = self._post('keyholder/locks/search', data)
        return self._tester_post_request_helper(response, lock.LockedUsers().update)

    """
    Reports
    """

    def post_report(self):
        self.logger.error('This API is deliberately not supported. Please use the website for reporting other users.')
        assert False

    """
    Partner Configurations
    """
    # TODO: Gain access

    """
    Public Locks
    """
    # /public-locks/{sharedLockId}
    # /public-locks/images/{sharedLockId}
    # /public-locks/search
    # /explore/categories

    """
    Extensions - Verification Picture
    """
    # /extensions/verification-picture/{lockId}/submit
    # /locks/{lockId}/verification-pictures


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
