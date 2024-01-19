from . import conversation, extensions, lock, triggers, user
import datetime
import json
import logging
import requests
from requests.adapters import HTTPAdapter, Retry
import time
from types import SimpleNamespace
from urllib.parse import urlparse, urljoin


class FileMultipartForm:
    def __init__(self):
        self.uri: str = ''
        self.name: str = ''
        self.type: str = ''


def generate_multipart_form_from_uri(uri) -> FileMultipartForm:
    fmf = FileMultipartForm()
    fmf.uri = uri
    fmf.name = 'test.png'
    fmf.type = 'image/png'
    return fmf


class ChasterAPI:

    def __init__(self, bearer, user_agent='ChasterPythonSDK/1.0', delay=5, root_api='https://api.chaster.app/'):
        """
        Not thread safe. Will need a ChasterAPI object per thread.
        :param bearer: bearer token for authentication
        :param user_agent: the value assigned to the User-Agent http header
        :param delay: the amount of seconds to wait after a request
        :param root_api: the url to the api endpoint
        """

        self.logger = logging.getLogger(self.__class__.__name__)
        self.root_api = urlparse(root_api)
        self.delay = delay
        self.session = requests.Session()  # generally not multithread safe https://github.com/psf/requests/issues/1871
        self.session.headers = {
            'Authorization': f'Bearer {bearer}',
            'Accept': 'application/json',
            'User-Agent': user_agent,
            'Accept-Language': 'en-US,en;q=0.5',
            'Connection': 'keep-alive'
        }
        retries = Retry(total=3,
                        backoff_factor=0.1,
                        status_forcelist=[500, 502, 503, 504],
                        respect_retry_after_header=True)
        retries.backoff_jitter = 0.01  # TODO: why is backoff_jitter not present in Retry?
        self.session.mount('http://', HTTPAdapter(max_retries=retries))
        self.session.mount('https://', HTTPAdapter(max_retries=retries))

    def _request_logger_default(self, response: requests.models.Response, *args, **kwargs):
        chaster_transaction_id = ''
        if 'x-chaster-transaction-id' in response.headers:
            chaster_transaction_id = response.headers['x-chaster-transaction-id']
            pass

        self.logger.debug(
            f'{response.status_code} {response.request.method} {response.request.url}  chaster_transaction_id:{chaster_transaction_id} {response.content}')
        self.logger.debug(
            f'chaster_transaction_id:{chaster_transaction_id} {response.request.body}')
        if 200 <= response.status_code < 300:
            return
        self.logger.error(
            f'{response.status_code} {response.request.method} {response.request.url}  chaster_transaction_id:{chaster_transaction_id} {response.content}')

    def _post_request_handler(self, response: requests.models.Response, *args, **kwargs):
        time.sleep(self.delay)

    def _get(self, path: str) -> requests.models.Response:
        response = self.session.get(urljoin(self.root_api.geturl(), path),
                                    hooks={'response': [self._post_request_handler, self._request_logger]})
        return response

    def _post(self, path: str, data) -> requests.models.Response:
        response = self.session.post(urljoin(self.root_api.geturl(), path),
                                     data=json.dumps(data),
                                     hooks={'response': [self._post_request_handler, self._request_logger]},
                                     headers={'Content-Type': 'application/json'})
        return response

    def _post_form(self, path: str, form) -> requests.models.Response:
        response = self.session.post(urljoin(self.root_api.geturl(), path),
                                     hooks={'response': [self._post_request_handler, self._request_logger]},
                                     files=form)
        return response

    def _put(self, path: str, data) -> requests.models.Response:
        response = self.session.put(urljoin(self.root_api.geturl(), path),
                                    data=json.dumps(data), hooks={'response': self._post_request_handler},
                                    headers={'Content-Type': 'application/json'})
        return response

    def _delete(self, path: str):
        response = self.session.delete(urljoin(self.root_api.geturl(), path),
                                       hooks={'response': self._post_request_handler})
        return response

    def _tester_get_wrapper(self, path, func):
        response = self._get(path)
        data = None
        if response.status_code == 200:
            data = response.json(object_hook=lambda d: SimpleNamespace(**d))
            data = func(data)
        return response, data

    def _tester_post_request_helper(self, response, update):
        data = None
        if response.status_code == 201 or response.status_code == 200:
            data = response.json(object_hook=lambda d: SimpleNamespace(**d))
            data = update(data)
        return response, data

    """
    Shared Locks
    """

    def get_user_shared_locks(self, status: str = 'active') -> tuple[requests.models.Response, list[lock.SharedLock]]:
        """
         `endpoint <https://api.chaster.app/api#/Shared%20Locks/SharedLockController_findAll>`_

        :param status: 'active', 'archived', or '' or None for both active and archived locks
        :return:
        """
        path = 'locks/shared-locks'
        if status != '' or None:
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
        """
        `endpoint <https://api.chaster.app/api#/Shared%20Locks/SharedLockController_create>`_

        Creates the given shared lock.
        :param create:
        :return:
        """

        create.validate()
        response = self._post('/locks/shared-locks', create.dump())
        data = None
        if response.status_code == 201:
            x = response.json(object_hook=lambda d: SimpleNamespace(**d))
            data = lock.IdResponse().update(x)
        return response, data

    def get_shared_lock_details(self, shared_lock_id: str) -> tuple[
        requests.models.Response, lock.SharedLock]:
        """
        `endpoint <https://api.chaster.app/api#/Shared%20Locks/SharedLockController_findOne>`_
        :param shared_lock_id:
        :return:
        """

        response = self._get(f'/lock/shared-locks/{shared_lock_id}')
        data = None
        if response.status_code == 200:
            x = response.json(object_hook=lambda d: SimpleNamespace(**d))
            data = lock.SharedLock().update(x)
        return response, data

    def update_shared_lock(self, shared_lock_id: str, update: lock.CreateSharedLock) -> requests.models.Response:
        """
        `endpoint <https://api.chaster.app/api#/Shared%20Locks/SharedLockController_update>`_
        :param shared_lock_id:
        :param update:
        :return:
        """
        update.validate()
        return self._put(f'/lock/shared-lock/{shared_lock_id}', update.dump())

    def archive_shared_lock(self, shared_lock_id: str) -> requests.models.Response:
        """
        `endpoint <https://api.chaster.app/api#/Shared%20Locks/SharedLockController_archive>`_
        :param shared_lock_id:
        :return:
        """
        return self._post(f'/locks/shared-locks/{shared_lock_id}/archive', {})

    def check_if_favorited(self, shared_lock_id: str) -> tuple[requests.models.Response, bool]:
        """
        `endpoint <https://api.chaster.app/api#/Shared%20Locks/SharedLockFavoriteController_isFavorite>`_
        :param shared_lock_id:
        :return:
        """
        response = self._get(f'/shared-locks/{shared_lock_id}/favorite')
        data = None
        if response.status_code == 200:
            data = response.json()['favorite']
        return response, data

    def favorite(self, shared_lock_id: str) -> requests.models.Response:
        """
        `endpoint <https://api.chaster.app/api#/Shared%20Locks/SharedLockFavoriteController_setFavorite>`_
        :param shared_lock_id:
        :return:
        """
        return self._put(f'/shared-locks/{shared_lock_id}/favorite', data={})

    def remove_favorite(self, shared_lock_id: str) -> requests.models.Response:
        """
        `endpoint <https://api.chaster.app/api#/Shared%20Locks/SharedLockFavoriteController_removeFavorite>`_
        :param shared_lock_id:
        :return:
        """
        return self._delete(f'/shared-locks/{shared_lock_id}/favorite')

    def get_favorite_shared_locks(self, limit: int = 15, last_id: str = None) -> tuple[
        requests.models.Response, lock.PageinatedSharedLockList]:
        """
        `endpoint <https://api.chaster.app/api#/Shared%20Locks/SharedLockFavoritesController_getFavoriteSharedLocks>`_
        :param limit: maximum number of shared locks in the response
        :param last_id: the id of the last result of the previous page
        :return:
        """
        if limit < 0:
            raise ValueError('limit cannot be zero')
        response = self._post('favorites/shared-locks', {'limit': limit, 'lastId': last_id})

        data = None
        if response.status_code == 201:
            x = response.json(object_hook=lambda d: SimpleNamespace(**d))
            data = lock.PageinatedSharedLockList().update(x)
        return response, data

    """
    Locks
    """

    def get_user_locks(self, status: str = 'active') -> tuple[requests.models.Response, list[lock.Lock]]:
        """
        `endpoint <https://api.chaster.app/api#/Locks/LockController_findAll>`_
        :param status: 'active', 'archived', 'all', or None
        :return:
        """
        path = '/locks'
        if status is not None:
            if status != '':
                if status == 'active' or status == 'archived' or status == 'all':
                    path = f'/locks?status={status}'
                else:
                    raise ValueError('status must be one of: active, archived, all, empty string, or None')

        response = self._get(path)
        data = None
        if response.status_code == 200:
            data = response.json(object_hook=lambda d: SimpleNamespace(**d))
            data = lock.Lock.generate_array(data)
        return response, data

    def get_lock_details(self, lock_id: str) -> tuple[requests.models.Response, lock.Lock]:
        """
        `endpoint <https://api.chaster.app/api#/Locks/LockController_findOne>`_
        :param lock_id:
        :return:
        """
        response = self._get(f'/locks/{lock_id}')

        data = None
        if response.status_code == 200:
            data = response.json(object_hook=lambda d: SimpleNamespace(**d))
            data = lock.Lock().update(data)
        return response, data

    def archive_lock(self, lock_id: str) -> requests.models.Response:
        """
        `endpoint <https://api.chaster.app/api#/Locks/LockController_archive>`_
        :param lock_id:
        :return:
        """
        return self._post(f'/locks/{lock_id}/archive', {})

    def archive_lock_as_keyholder(self, lock_id: str) -> requests.models.Response:
        """
        `endpoint <https://api.chaster.app/api#/Locks/LockController_archiveKeyholder>`_
        :param lock_id:
        :return:
        """
        return self._post(f'/locks/{lock_id}/archive/keyholder', {})

    def update_lock_duration(self, lock_id: str, time: int) -> requests.models.Response:
        """
        `endpoint <https://api.chaster.app/api#/Locks/LockController_updateTime>`_
        :param lock_id:
        :param time: time length in seconds
        :return:
        """
        return self._post(f'locks/{lock_id}/update-time', {'duration': time})

    def set_freeze(self, lock_id: str, freeze: bool) -> requests.models.Response:
        """
        `endpoint <https://api.chaster.app/api#/Locks/LockController_setFreeze>`_
        :param lock_id:
        :param freeze: True to freeze the lock, False to unfreeze the lock
        :return:
        """
        return self._post(f'locks/{lock_id}/freeze', data={"isFrozen": freeze})

    def unlock(self, lock_id: str) -> requests.models.Response:
        """
        `endpoint <https://api.chaster.app/api#/Locks/LockController_unlock>`_
        :param lock_id:
        :return:
        """
        return self._post(f'/locks/{lock_id}/unlock', {})

    def update_lock_settings(self, lock_id: str, display_remaining_time: bool,
                             hide_time_logs: bool) -> requests.models.Response:
        """
        `endpoint <https://api.chaster.app/api#/Locks/LockController_setSettings>`_
        :param lock_id:
        :param display_remaining_time:
        :param hide_time_logs:
        :return:
        """
        return self._post(f'locks/{lock_id}/settings', data={
            "displayRemainingTime": display_remaining_time,
            "hideTimeLogs": hide_time_logs
        })

    # TODO: would you ever set bot max_limit_date and disable_max_time_limit
    def set_max_limit_date(self, lock_id: str, max_limit_date: datetime.datetime,
                           disable_max_time_limit: bool) -> requests.models.Response:
        """
        `endpoint <https://api.chaster.app/api#/Locks/LockController_setMaxLimitDate>`_
        :param lock_id:
        :param max_limit_date:
        :param disable_max_time_limit:
        :return:
        """
        return self._post(f'locks/{lock_id}/max-limit-date', data={
            "maxLimitDate": max_limit_date.isoformat(),
            "disableMaxLimitDate": disable_max_time_limit
        })

    def trust_keyholder(self, lock_id: str) -> requests.models.Response:
        """
        `endpoint <https://api.chaster.app/api#/Locks/LockController_trustKeyholder>`_
        :param lock_id:
        :return:
        """
        return self._post(f'locks/{lock_id}/trust-keyholder', data={})

    def get_lock_combination(self, lock_id: str) -> tuple[requests.models.Response, user.LockCombination]:
        """
        `endpoint <https://api.chaster.app/api#/Locks/LockController_combination>`_
        :param lock_id:
        :return:
        """
        response = self._get(f'/locks/{lock_id}/combination')

        data = None
        if response.status_code == 200:
            data = response.json(object_hook=lambda d: SimpleNamespace(**d))
            data = user.LockCombination().update(data)
        return response, data

    def get_lock_history(self, lock_id: str, extension: str = None, limit: int = 25, last_id: str = None) -> tuple[
        requests.models.Response, lock.PageinatedLockHistory]:
        """
        `endpoint <https://api.chaster.app/api#/Locks/LockController_getLockHistory>`_
        :param lock_id:
        :param extension:
        :param limit: response length limit
        :param last_id: last id of the last response of the previous page, not necessary for the first page
        :return:
        """
        data = {}
        if extension is not None and extension != '':
            data['extension'] = extension
        if limit is not None:
            data['limit'] = limit
        if last_id is not None:
            data['lastId'] = last_id
        response = self._post(f'locks/{lock_id}/history', data=data)

        data = None
        if response.status_code == 201:
            data = response.json(object_hook=lambda d: SimpleNamespace(**d))
            data = lock.PageinatedLockHistory().update(data)
        return response, data

    def set_as_test_lock(self, lock_id: str) -> requests.models.Response:
        """
        `endpoint <https://api.chaster.app/api#/Locks/LockController_setAsTestLock>`_
        :param lock_id:
        :return:
        """
        return self._put(f'locks/{lock_id}/is-test-lock', data={})

    # TODO: The reason for this API is unclear. Does it send more data than what is already present in the lock?
    def get_lock_extension_information(self, lock_id: str, extension_id: str) -> tuple[
        requests.models.Response, lock.ExtensionInformation]:
        """
        `endpoint <https://api.chaster.app/api#/Locks/LockExtensionController_getLockInfoFromExtension>`_
        :param lock_id:
        :param extension_id:
        :return:
        """
        return self._tester_get_wrapper(f'locks/{lock_id}/extensions/{extension_id}',
                                        lock.ExtensionInformation().update)

    def trigger_extension_action(self, lock_id: str, extension_id: str, data: any) -> requests.models.Response:
        """
        `endpoint <https://api.chaster.app/api#/Locks/LockExtensionController_triggerAction>`_
        See triggers.
        :param lock_id:
        :param extension_id:
        :param data:
        :return:
        """
        return self._post(f'locks/{lock_id}/extensions/{extension_id}/action', data=data)

    """
    Triggers
    """

    def vote_in_share_links(self, lock_id: str, extension_id: str, vote: triggers.ShareLinksVote) -> tuple[
        requests.models.Response, triggers.ShareLinksVoteReturn]:
        """
        `endpoint <https://api.chaster.app/api#/Locks/LockExtensionController_triggerAction>`_
        :param lock_id:
        :param extension_id:
        :param vote:
        :return:
        """
        response = self.trigger_extension_action(lock_id, extension_id, vote.dump())
        return self._tester_post_request_helper(response, triggers.ShareLinksVoteReturn().update)

    def get_share_link_vote_url(self, lock_id: str, extension_id: str) -> tuple[
        requests.models.Response, triggers.ShareLinkUrlResponse]:
        """
        `endpoint <https://api.chaster.app/api#/Locks/LockExtensionController_triggerAction>`_
        :param lock_id:
        :param extension_id:
        :return:
        """
        data = triggers.ActionRequest()
        data.action = 'getLink'
        response = self.trigger_extension_action(lock_id, extension_id, data.dump())
        return self._tester_post_request_helper(response, triggers.ShareLinksVoteReturn().update)

    def get_share_link_vote_info(self, lock_id: str, extension_id: str) -> tuple[
        requests.models.Response, triggers.ShareLinkGetInfoResponse]:
        """
        `endpoint <https://api.chaster.app/api#/Locks/LockExtensionController_triggerAction>`_
        :param lock_id:
        :param extension_id:
        :return:
        """
        data = triggers.ActionRequest()
        data.action = 'getInfo'
        response = self.trigger_extension_action(lock_id, extension_id, data.dump())
        return self._tester_post_request_helper(response, triggers.ShareLinkGetInfoResponse().update)

    def place_user_into_pillory(self, lock_id: str, extension_id: str,
                                data: triggers.PilloryParameters) -> requests.models.Response:
        return self.trigger_extension_action(lock_id, extension_id, data.dump())

    def get_current_pillory_info(self, lock_id: str, extension_id: str) -> tuple[
        requests.models.Response, triggers.PilloryVotes]:
        """
        `endpoint <https://api.chaster.app/api#/Locks/LockExtensionController_triggerAction>`_
        :param lock_id:
        :param extension_id:
        :return:
        """
        data = triggers.ActionRequest()
        data.action = 'getStatus'
        response = self.trigger_extension_action(lock_id, extension_id, data.dump())
        return self._tester_post_request_helper(response, triggers.PilloryVotes().update)

    def unlock_for_hygiene(self, lock_id: str, extension_id: str, is_you: bool) -> requests.models.Response:
        """
        `endpoint <https://api.chaster.app/api#/Locks/LockExtensionController_triggerAction>`_
        :param lock_id:
        :param extension_id:
        :param is_you: True if the authenticated user is unlocking themselves, False if the authenticated user is unlocking someone they are keyholding
        :return:
        """
        data = triggers.ActionRequest()
        data.action = 'keyholderOpen'
        if is_you:
            data.action = 'submit'
        return self.trigger_extension_action(lock_id, extension_id, data.dump())

    def roll_dice(self, lock_id: str, extension_id: str) -> tuple[
        requests.models.Response, triggers.DiceRollResult]:
        """
        `endpoint <https://api.chaster.app/api#/Locks/LockExtensionController_triggerAction>`_
        :param lock_id:
        :param extension_id:
        :return:
        """
        data = triggers.ActionRequest()
        data.action = 'submit'
        response = self.trigger_extension_action(lock_id, extension_id, data.dump())
        return self._tester_post_request_helper(response, triggers.DiceRollResult().update)

    def spin_wheel_of_fortune(self, lock_id: str, extension_id: str) -> tuple[
        requests.models.Response, triggers.WheelOfFortuneResult]:
        """
        `endpoint <https://api.chaster.app/api#/Locks/LockExtensionController_triggerAction>`_
        :param lock_id:
        :param extension_id:
        :return:
        """
        data = triggers.ActionRequest()
        data.action = 'submit'
        response = self.trigger_extension_action(lock_id, extension_id, data.dump())
        return self._tester_post_request_helper(response, triggers.WheelOfFortuneResult().update)

    def request_a_random_task(self, lock_id: str, extension_id: str) -> requests.models.Response:
        """
        `endpoint <https://api.chaster.app/api#/Locks/LockExtensionController_triggerAction>`_
        :param lock_id:
        :param extension_id:
        :return:
        """
        data = {"action": "submit", "payload": {"requestVote": False}}
        return self.trigger_extension_action(lock_id, extension_id, data)

    def community_vote_next_task(self, lock_id: str, extension_id: str, vote_duration: int) -> requests.models.Response:
        """
        `endpoint <https://api.chaster.app/api#/Locks/LockExtensionController_triggerAction>`_
        :param lock_id:
        :param extension_id:
        :param vote_duration: duration in seconds
        :return:
        """
        data = {"action": "submit", "payload": {"requestVote": True, "voteDuration": vote_duration}}
        return self.trigger_extension_action(lock_id, extension_id, data)

    def assign_task(self, lock_id: str, extension_id: str, task: extensions.Task):
        """
        `endpoint <https://api.chaster.app/api#/Locks/LockExtensionController_triggerAction>`_
        :param lock_id:
        :param extension_id:
        :param task:
        :return:
        """
        data = {
            "action": "assignTask",
            "payload": {
                'task': task.dump()
            }
        }
        return self.trigger_extension_action(lock_id, extension_id, data)

    def mark_task_done(self, lock_id: str, extension_id: str, complete: bool) -> requests.models.Response:
        """
        `endpoint <https://api.chaster.app/api#/Locks/LockExtensionController_triggerAction>`_
        :param lock_id:
        :param extension_id:
        :param complete: True if task is complete, False if abandoned
        :return:
        """
        data = {"action": "completeTask", "payload": {"isCompleted": complete}}
        return self.trigger_extension_action(lock_id, extension_id, data)

    def trigger_new_verification(self, lock_id: str, extension_id: str) -> requests.models.Response:
        """
        `endpoint <https://api.chaster.app/api#/Locks/LockExtensionController_triggerAction>`_
        :param lock_id:
        :param extension_id:
        :return:
        """
        data = {"action": "createVerificationRequest", "payload": {}}
        return self.trigger_extension_action(lock_id, extension_id, data)

    def trigger_guess_the_timer(self, lock_id: str, extension_id: str) -> tuple[
        requests.models.Response, triggers.GuessTheTimerResponse]:
        """
        `endpoint <https://api.chaster.app/api#/Locks/LockExtensionController_triggerAction>`_
        :param lock_id:
        :param extension_id:
        :return:
        """
        data = {"action": "submit", "payload": {}}
        response = self.trigger_extension_action(lock_id, extension_id, data)
        return self._tester_post_request_helper(response, triggers.GuessTheTimerResponse().update)

    """
    Lock Creation
    """

    def create_personal_lock(self, self_lock: lock.CreateLock) -> tuple[requests.models.Response, lock.LockId]:
        """
        `endpoint <https://api.chaster.app/api#/Lock%20Creation/LockCreationController_create>`_
        :param self_lock:
        :return:
        """
        response = self._post('locks', data=self_lock.dump())

        data = None
        if response.status_code == 201:
            data = response.json(object_hook=lambda d: SimpleNamespace(**d))
            data = lock.LockId().update(data)
        return response, data

    def edit_extensions(self, lock_id: str, ext: extensions.Extensions) -> requests.models.Response:
        """
        `endpoint <https://api.chaster.app/api#/Lock%20Creation/LockCreationController_setLockExtensions>`_
        :param lock_id:
        :param ext: the new extensions for the lock
        :return:
        """
        return self._post(f'locks/{lock_id}/extensions', data=ext.dump())

    def create_lock_from_shared_lock(self, shared_lock_id: str, lock_details: lock.LockInfo) -> tuple[
        requests.models.Response, lock.LockId]:
        """
        `endpoint <https://api.chaster.app/api#/Lock%20Creation/LockCreationController_createLockFromSharedLock>`_
        :param shared_lock_id:
        :param lock_details:
        :return:
        """
        response = self._post(f'public-locks/{shared_lock_id}/create-lock', data=lock_details.dump())

        data = None
        if response.status_code == 201:
            data = response.json(object_hook=lambda d: SimpleNamespace(**d))
            data = lock.LockId().update(data)
        return response, data

    """
    Profile
    """

    def get_user_public_locks(self, user_id: str) -> tuple[requests.models.Response, list[lock.Lock]]:
        """
        `endpoint <https://api.chaster.app/api#/Profile/LockVisitorController_getUserLocks>`_
        :param user_id:
        :return:
        """
        return self._tester_get_wrapper(f'locks/user/{user_id}', lock.Lock.generate_array)

    def get_profile(self, user_id: str) -> tuple[requests.models.Response, user.User]:
        """
        `endpoint <https://api.chaster.app/api#/Profile/ProfileController_getUserById>`_
        :param user_id:
        :return:
        """
        return self._tester_get_wrapper(f'users/profile/by-id/{user_id}', user.User().update)

    def find_profile(self, username: str) -> tuple[requests.models.Response, user.User]:
        """
        `endpoint <https://api.chaster.app/api#/Profile/ProfileController_getUser>`_
        :param username:
        :return:
        """
        return self._tester_get_wrapper(f'users/profile/{username}', user.User().update)

    def find_profile_detailed(self, username: str) -> tuple[requests.models.Response, user.DetailedUser]:
        """
        `endpoint <https://api.chaster.app/api#/Profile/ProfileController_getUserProfile>`_
        :param username:
        :return:
        """
        return self._tester_get_wrapper(f'users/profile/{username}/details', user.DetailedUser().update)

    def get_badges(self) -> tuple[requests.models.Response, user.Badges]:
        """
        `endpoint <https://api.chaster.app/api#/Profile/UserBadgeController_getUserBadgeCount>`_
        :return:
        """
        return self._tester_get_wrapper('users/badge/count', user.Badges().update)

    def update_profile(self) -> tuple[requests.models.Response, user.AuthProfile]:
        """
        `endpoint <https://api.chaster.app/api#/Profile/AuthMeController_meEdit>`_
        :return:
        """
        return self._tester_get_wrapper('auth/profile/update', user.AuthProfile().update)

    def get_user_profile(self) -> tuple[requests.models.Response, user.AuthProfile]:
        """
        `endpoint <https://api.chaster.app/api#/Profile/AuthMeController_me>`_
        :return:
        """
        return self._tester_get_wrapper('auth/profile', user.AuthProfile().update)

    """
    Files
    """

    def upload_file(self, uri, usage: str = 'messaging') -> tuple[requests.models.Response, user.FileToken]:
        """
        `endpoint <https://api.chaster.app/api#/Files/StorageController_uploadFiles>`_
        :param uri:
        :param usage: 'messaging' or 'community_event_challenge'
        :return:
        """
        fmf = generate_multipart_form_from_uri(uri)
        files = {'files': (fmf.name, open(fmf.uri, 'rb'), fmf.type),
                 'type': (None, usage)}

        response = self._post_form('/files/upload', files)

        return self._tester_post_request_helper(response, user.FileToken().update)

    def find_file(self, file_key) -> tuple[requests.models.Response, user.FileUrl]:
        """
        `endpoint <https://api.chaster.app/api#/Files/StorageController_getFileFromKey>`_
        :param file_key:
        :return:
        """
        return self._tester_get_wrapper(f'/files/{file_key}', user.FileUrl().update)

    """
    Combinations
    """

    def upload_combination_image(self, uri, manual_check: bool = False) -> tuple[
        requests.models.Response, lock.Combination]:
        """
        `endpoint <https://api.chaster.app/api#/Combinations/CombinationController_uploadImage>`_
        :param uri:
        :param manual_check:
        :return:
        """
        fmf = generate_multipart_form_from_uri(uri)
        with open(fmf.uri, 'rb') as f:
            content = f.read()
            print(len(content))
            files = {'file': (fmf.name, content, fmf.type),
                     'enableManualCheck': (None, str(manual_check).lower())}
        response = self._post_form('combinations/image', files)
        return self._tester_post_request_helper(response, lock.Combination().update)

    def create_combination_code(self, code: str) -> tuple[requests.models.Response, lock.Combination]:
        """
        `endpoint <https://api.chaster.app/api#/Combinations/CombinationController_createCode>`_
        :param code:
        :return:
        """
        response = self._post(f'combinations/code', {'code': code})
        return self._tester_post_request_helper(response, lock.Combination().update)

    """
    Extensions
    """

    def get_all_known_extensions(self) -> tuple[requests.models.Response, list[extensions.KnownExtension]]:
        """
        `endpoint <https://api.chaster.app/api#/Extensions/ExtensionListController_getExtensions>`_
        :return:
        """
        return self._tester_get_wrapper('extensions', extensions.known_extension_list_update)

    """
    Session Offer
    """

    def create_keyholding_offer(self, lock_id, keyholder: str) -> requests.models.Response:
        """
        `endpoint <https://api.chaster.app/api#/Session%20Offer/SessionOfferController_createKeyholdingOffer>`_
        :param lock_id:
        :param keyholder:
        :return:
        """
        return self._post(f'session-offer/lock/{lock_id}', data={
            'keyholder': keyholder
        })

    def accept_keyholding_request(self, offer_token: str) -> requests.models.Response:
        """
        `endpoint <https://api.chaster.app/api#/Session%20Offer/SessionOfferController_acceptKeyholdingRequest>`_
        :param offer_token:
        :return:
        """
        return self._get(f'session-offer/token/{offer_token}/accept')

    def get_sent_keyholding_offers(self, lock_id: str) -> tuple[
        requests.models.Response, list[user.KeyholderOfferEntry]]:
        """
        `endpoint <https://api.chaster.app/api#/Session%20Offer/SessionOfferController_getOfferRequestStatus>`_
        :param lock_id:
        :return:
        """
        return self._tester_get_wrapper(f'session-offer/lock/{lock_id}/status', user.KeyholderOfferEntry.generate_array)

    def retrieve_keyholder_request_lock_info(self, offer_token: str) -> tuple[requests.models.Response, lock.Lock]:
        """
        `endpoint <https://api.chaster.app/api#/Session%20Offer/SessionOfferController_getLockKeyholdingRequest>`_
        :param offer_token:
        :return:
        """
        return self._tester_get_wrapper(f'session-offer/token/{offer_token}', lock.Lock().update)

    def resolve_keyholding_offer(self, session_request_id: str, accept: bool) -> requests.models.Response:
        """
        `endpoint <https://api.chaster.app/api#/Session%20Offer/SessionOfferController_validateOfferRequest>`_
        :param session_request_id:
        :param accept:
        :return:
        """
        return self._post(f'session-offer/{session_request_id}', data={'accept': accept})

    def archive_keyholding_offer(self, session_request_id: str) -> requests.models.Response:
        """
        `endpoint <https://api.chaster.app/api#/Session%20Offer/SessionOfferController_archiveKeyholdingOffer>`_
        :param session_request_id:
        :return:
        """
        return self._get(f'session-offer/{session_request_id}/archive')

    def get_keyholding_offers_from_wearers(self) -> tuple[requests.models.Response, list[user.KeyholderRequestEntry]]:
        """
        `endpoint <https://api.chaster.app/api#/Session%20Offer/SessionOfferController_getKeyholderRequests>`_
        :return:
        """
        return self._tester_get_wrapper('session-offer/requests', user.KeyholderRequestEntry.generate_array)

    """
    Messaging
    """

    def get_conversations(self, limit: int = 15, status: str = 'approved') -> tuple[
        requests.models.Response, conversation.Conversations]:
        """
        `endpoint <https://api.chaster.app/api#/Messaging/MessagingController_getConversations>`_
        :param limit:
        :param status: 'approved', 'pending', 'ignored', or None for all conversations.
        :return:
        """
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
        """
        `endpoint <https://api.chaster.app/api#/Messaging/MessagingController_createConversation>`_
        :param user_id:
        :param message:
        :return:
        """
        response = self._post('conversations',
                              {'users': [user_id],
                               'type': "private",
                               "message": message})

        return self._tester_post_request_helper(response, conversation.Conversation().update)

    def get_user_conversation(self, user_id: str) -> tuple[requests.models.Response, conversation.Conversation]:
        """
        `endpoint <https://api.chaster.app/api#/Messaging/MessagingController_getConversationByUserId>`_
        :param user_id:
        :return:
        """
        return self._tester_get_wrapper(f'conversations/by-user/{user_id}', conversation.Conversation().update)

    # TODO: flushout attachments, what is nonce?
    """
    {"message":"here","attachments":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmaWxlcyI6WyI2NWE4OGU2OWE4NTIwMDAxYzc2MTc2OTkiXSwidHlwZSI6Im1lc3NhZ2luZyIsInVzZXIiOiI2NGU1YjQ4MWI1MzNhNWNjZmU2MTU2N2YiLCJpYXQiOjE3MDU1NDUzMjEsImV4cCI6MTcwNTYzMTcyMX0.u2HPOjyhmqAB-2aTd4Uq_HF-b-Z6V8-T8soPZytLj9w","nonce":"HhH_YHrj8TAAhkyDFfEYs"}
    """

    def post_message(self, conversation_id: str, message: str) -> tuple[requests.models.Response, conversation.Message]:
        """
        `endpoint <https://api.chaster.app/api#/Messaging/MessagingController_sendMessage>`_
        :param conversation_id:
        :param message:
        :return:
        """
        response = self._post(f'conversations/{conversation_id}',
                              {"message": message})

        return self._tester_post_request_helper(response, conversation.Message().update)

    def get_conversation(self, conversation_id: str) -> tuple[requests.models.Response, conversation.Conversation]:
        """
        `endpoint <https://api.chaster.app/api#/Messaging/MessagingController_getConversation>`_
        :param conversation_id:
        :return:
        """
        return self._tester_get_wrapper(f'conversations/{conversation_id}', conversation.Conversation().update)

    # TODO: What options for status are there?
    # TODO: Confirm the listed statuses are the correct ones
    def set_conversation_status(self, conversation_id: str, status: str) -> requests.models.Response:
        """
        `endpoint <https://api.chaster.app/api#/Messaging/MessagingController_setConversationStatus>`_
        :param conversation_id:
        :param status: 'approved', 'pending', 'ignored'
        :return:
        """
        return self._put(f'conversations/{conversation_id}/status', data={'status': status})

    def set_conversation_unread(self, conversation_id: str, unread: bool) -> requests.models.Response:
        """
        `endpoint <https://api.chaster.app/api#/Messaging/MessagingController_setConversationUnread>`_
        :param conversation_id:
        :param unread:
        :return:
        """
        return self._put(f'conversations/{conversation_id}/unread', data={'unread': unread})

    def get_conversation_messages(self, conversation_id: str, limit: int = 15, last_id: str = None) -> tuple[
        requests.models.Response, conversation.ConversationMessages]:
        """
        `endpoint <https://api.chaster.app/api#/Messaging/MessagingController_getMessages>`_
        :param conversation_id:
        :param limit: the maximum number of messages to return
        :param last_id: the id of the last message in the previous page, None if there is no previous page
        :return:
        """
        path = f'conversations/{conversation_id}/messages?limit={limit}'
        if last_id is not None:
            path += f'&lastId={last_id}'
        return self._tester_get_wrapper(path, conversation.ConversationMessages().update)

    """
    Extensions - Temporary Opening
    """

    def get_temporary_opening_combination(self, lock_id: str) -> tuple[requests.models.Response, user.LockCombination]:
        """
        `endpoint <https://api.chaster.app/api#/Extensions%20-%20Temporary%20Opening/TemporaryOpeningExtensionController_getCombination>`_
        :param lock_id:
        :return:
        """
        return self._tester_get_wrapper(f'/extensions/temporary-opening/{lock_id}/combination',
                                        user.LockCombination().update)

    def set_temporary_opening_new_combination(self, lock_id: str, combination_id: str) -> requests.models.Response:
        """
        `endpoint <https://api.chaster.app/api#/Extensions%20-%20Temporary%20Opening/TemporaryOpeningExtensionController_setCombination>`_
        :param lock_id:
        :param combination_id:
        :return:
        """
        return self._post(f'/extensions/temporary-opening/{lock_id}/combination', {'combinationId': combination_id})

    def get_temporary_opening_combination_from_action_log(self, action_log_id: str, lock_id: str) -> tuple[
        requests.models.Response, user.LockCombination]:
        """
        `endpoint <https://api.chaster.app/api#/Extensions%20-%20Temporary%20Opening/TemporaryOpeningExtensionController_getCombinationFromHistoryEntry>`_
        :param action_log_id:
        :param lock_id:
        :return:
        """
        return self._tester_get_wrapper(
            f'/extensions/temporary-opening/{lock_id}/action-log/{action_log_id}/combination',
            user.LockCombination().update)

    """
    Community Events
    """

    def get_community_event_categories(self) -> tuple[
        requests.models.Response, list[user.CommunityEventCategory]]:
        """
        `endpoint <https://api.chaster.app/api#/Community%20Events/CommunityEventController_getCategories>`_
        :return:
        """
        return self._tester_get_wrapper('/community-event/categories', user.CommunityEventCategory.generate_array)

    def get_community_event_details(self, date: datetime.datetime = datetime.datetime.now()) -> tuple[
        requests.models.Response, user.CommunityEventDetails]:
        """
        `endpoint <https://api.chaster.app/api#/Community%20Events/CommunityEventController_getPeriodDetails>`_
        :param date:
        :return:
        """
        response = self._post(f'community-event/details', data={'date': date.isoformat()})
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
        """
        `endpoint <https://api.chaster.app/api#/Settings/SettingsController_getAppSettings>`_
        :return:
        """
        return self._tester_get_wrapper('/settings', user.AppSettings().update)

    """
    Users
    """

    def search_for_users(self, search: str) -> tuple[requests.models.Response, list[user.User]]:
        """
        `endpoint <https://api.chaster.app/api#/Users/UserSearchController_searchByUsername>`_
        :param search:
        :return:
        """
        response = self._post('users/search/by-username', {'search': search})
        return self._tester_post_request_helper(response, user.User.generate_array)

    def search_for_users_by_discord(self, discord_id: str) -> tuple[requests.models.Response, user.User]:
        """
        `endpoint <https://api.chaster.app/api#/Users/UserSearchController_getUserByDiscordId>`_
        :param discord_id:
        :return:
        """
        return self._tester_get_wrapper(f'users/search/by-discord-id/{discord_id}', user.User().update)

    """
    Keyholder
    """
    # TODO: Flush out this function.
    def post_keyholder_locks_search(self, page: int = 0, status: str = 'locked', limit: int = 15, criteria: dict = {},
                                    search: str = None) -> tuple[requests.models.Response, lock.LockedUsers]:
        """
        `endpoint <https://api.chaster.app/api#/Keyholder/KeyholderController_searchLocks>`_
        :param page:
        :param status: 'locked', 'unlocked', 'archived', 'deserted'
        :param limit:
        :param criteria:
        :param search:
        :return:
        """
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

    """
    Partner Configurations
    """
    # TODO: Gain access

    """
    Public Locks
    """

    def find_public_shared_lock(self, shared_lock_id: str) -> tuple[
        requests.models.Response, lock.PublicSharedLockInfo]:
        """
        `endpoint <https://api.chaster.app/api#/Public%20Locks/PublicLockController_findOne>`_
        :param shared_lock_id:
        :return:
        """
        return self._tester_get_wrapper(f'/public-locks/{shared_lock_id}', lock.PublicSharedLockInfo().update)

    # TODO: Need to handle file with other file apis
    def generate_public_shared_lock_flyer(self, shared_lock_id: str) -> requests.models.Response:
        """
        `endpoint <https://api.chaster.app/api#/Public%20Locks/PublicLockController_getSharedLockImage>`_
        :param shared_lock_id:
        :return:
        """
        response = self._get(f'/public-locks/images/{shared_lock_id}')
        return response

    def search_for_public_locks(self, params: lock.SearchPublicLock) -> \
            tuple[requests.models.Response, lock.PageinatedSharedLockList]:
        """
        `endpoint <https://api.chaster.app/api#/Public Locks/PublicLockController_search>`_
        :param params:
        :return:
        """
        response = self._post('/public-locks/search', data=params.dump())

        data = None
        if response.status_code == 200:
            x = response.json(object_hook=lambda d: SimpleNamespace(**d))
            data = lock.PageinatedSharedLockList().update(x)
        return response, data

    def find_explore_page_locks(self) -> tuple[requests.models.Response, list[lock.ExplorePageLock]]:
        """
        `endpoint <https://api.chaster.app/api#/Public%20Locks/PublicLockExploreController_findAll>`_
        :return:
        """
        return self._tester_get_wrapper('/explore/categories', lock.ExplorePageLock.generate_array)

    """
    Extensions - Verification Picture
    """

    # TODO: enableVerificationCode False does what?
    def submit_verification(self, lock_id: str, uri, enable_verification_code: bool = True) -> requests.models.Response:
        """
        `endpoint <https://api.chaster.app/api#/Extensions%20-%20Verification%20Picture/VerificationPictureController_submitPicture>`_
        :param lock_id:
        :param uri:
        :param enable_verification_code:
        :return:
        """
        fmf = generate_multipart_form_from_uri(uri)
        files = {'file': (fmf.name, open(fmf.uri, 'rb'), fmf.type),
                 'enableVerificationCode': (None, enable_verification_code)}
        return self._post_form(f'/extensions/verification-picture/{lock_id}/submit', files)

    def get_verification_history(self, lock_id: str) -> tuple[
        requests.models.Response, list[lock.VerificationPhotoHistory]]:
        """
        `endpoint <https://api.chaster.app/api#/Extensions%20-%20Verification%20Picture/VerificationPictureController_getVerificationPictures>`_
        :param lock_id:
        :return:
        """
        return self._tester_get_wrapper(f'/locks/{lock_id}/verification-pictures',
                                        lock.VerificationPhotoHistory.generate_array)


class _MockChasterData:
    user_locks = {}

    def __init__(self):
        """
        in progress
        """
        pass


class _MockChasterAPI(ChasterAPI):
    def __init__(self, mock_chaster_data: _MockChasterData, user_id):
        """
        in progress
        :param mock_chaster_data:
        :param user_id:
        """
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
