import datetime
import unittest
from unittest.mock import MagicMock
from requests import Response
import json
from src.chaster.api import ChasterAPI
import src.chaster.lock as lock
import src.chaster.extensions as extensions
from types import SimpleNamespace
from . import response_examples


class MyTestCase(unittest.TestCase):
    """
    Shared Locks
    """

    def test_get_shared_locks_success(self):
        tests = [
            (response_examples.get_shared_locks, 7),
            ('[]', 0)
        ]
        for i, test in enumerate(tests):
            with self.subTest(i=i):
                api = ChasterAPI('')
                response = Response()
                response.json = MagicMock(return_value=json.loads(test[0], object_hook=lambda d: SimpleNamespace(**d)))
                response.status_code = 200
                api._get = MagicMock(return_value=response)
                response, data = api.get_user_shared_locks()
                self.assertEqual(len(data), test[1], msg=None)

    def test_get_shared_locks_by_status_success(self):
        tests = [
            ('[]', 'active'),
            ('[]', 'archived'),
            ('[]', ''),
        ]
        for i, test in enumerate(tests):
            with self.subTest(i=i):
                api = ChasterAPI('')
                response = Response()
                response.json = MagicMock(return_value=json.loads(test[0], object_hook=lambda d: SimpleNamespace(**d)))
                response.status_code = 200
                api._get = MagicMock(return_value=response)
                response, data = api.get_user_shared_locks(status=test[1])
                self.assertEqual(len(data), 0, msg=None)

    def test_get_shared_locks_by_status_failure(self):
        with self.assertRaises(ValueError):
            api = ChasterAPI('')
            _, _ = api.get_user_shared_locks(status='asdf')

    def generate_csl(self, min_duration=10, max_duration=15, maxLimitDuration=None,
                     minDate=None, maxDate=None, maxLimitDate=None, limitLockTime=False):
        csl = lock.CreateSharedLock()
        csl.minDuration = min_duration
        csl.maxDuration = max_duration
        csl.maxLimitDuration = maxLimitDuration
        csl.minDate = minDate
        csl.maxDate = maxDate
        csl.maxLimitDate = maxLimitDate
        csl.displayRemainingTime = True
        csl.limitLockTime = limitLockTime
        csl.maxLockedUsers = 999
        csl.isPublic = False
        csl.password = ''
        csl.requireContact = False
        csl.name = 'Test'
        csl.description = 'Test'
        csl.photoId = ''
        csl.hideTimeLogs = False
        csl.isFindom = False
        return csl

    def test_create_shared_lock_success(self):
        csl = self.generate_csl()
        api = ChasterAPI('')
        # avoid making an api call if the exception is not raised
        response = Response()
        response.json = MagicMock(
            return_value=json.loads(response_examples.created_shared_lock))
        response.status_code = 201
        api._post = MagicMock(return_value=response)
        _, data = api.create_shared_lock(csl)
        self.assertEqual(data, '12345')

    def test_get_shared_lock_details(self):
        api = ChasterAPI('')
        response = Response()
        response.json = MagicMock(
            return_value=json.loads(response_examples.shared_lock_details, object_hook=lambda d: SimpleNamespace(**d)))
        response.status_code = 200
        api._get = MagicMock(return_value=response)
        _, data = api.get_shared_lock_details('65139d7d1a72a968b46338e4')
        self.assertEqual(data._id, '65139d7d1a72a968b46338e4')

    def test_update_shared_lock(self):
        csl = self.generate_csl()
        api = ChasterAPI('')
        response = Response()
        response.status_code = 200
        api._put = MagicMock(return_value=response)
        response = api.update_shared_lock('', csl)
        self.assertEqual(response.status_code, 200)

    def test_archive_shared_lock(self):
        api = ChasterAPI('')
        response = Response()
        response.status_code = 200
        api._post = MagicMock(return_value=response)
        response = api.archive_shared_lock('')
        self.assertEqual(response.status_code, 200)

    def test_check_if_favorited(self):
        tests = [
            True, False
        ]
        for i, test in enumerate(tests):
            with self.subTest(i=i):
                api = ChasterAPI('')
                response = Response()
                response.json = MagicMock(
                    return_value={'favorite': test})
                response.status_code = 200
                api._get = MagicMock(return_value=response)
                _, data = api.check_if_favorited('')
                self.assertEqual(data, test)

    def test_favorite(self):
        api = ChasterAPI('')
        response = Response()
        response.status_code = 200
        api._put = MagicMock(return_value=response)
        response = api.favorite('')
        self.assertEqual(response.status_code, 200)

    def test_remove_favorite(self):
        api = ChasterAPI('')
        response = Response()
        response.status_code = 200
        api._delete = MagicMock(return_value=response)
        response = api.remove_favorite('')
        self.assertEqual(response.status_code, 200)

    def test_get_favorited_shared_locks(self):
        api = ChasterAPI('')
        response = Response()
        response.status_code = 201
        response.json = MagicMock(
            return_value=json.loads(response_examples.get_favorited_share_locks,
                                    object_hook=lambda d: SimpleNamespace(**d)))
        api._post = MagicMock(return_value=response)
        response, data = api.get_favorite_shared_locks()
        self.assertEqual(response.status_code, 201)
        self.assertEqual(len(data.results), 3)

    """
    Locks
    """

    def response_factory(self, status_code, json_str, raw_json=False):
        if json_str == '':
            json_str = '{}'
        api = ChasterAPI('')
        response = Response()
        response.status_code = status_code
        if raw_json:
            response.json = MagicMock(
                return_value=json.loads(json_str))
        else:
            response.json = MagicMock(
                return_value=json.loads(json_str, object_hook=lambda d: SimpleNamespace(**d)))
        api._get = MagicMock(return_value=response)
        api._post = MagicMock(return_value=response)
        api._put = MagicMock(return_value=response)
        api._delete = MagicMock(return_value=response)
        api._post_form = MagicMock(return_value=response)
        return api

    def test_get_locks(self):
        api = self.response_factory(200, response_examples.list_of_user_locks)
        response, data = api.get_user_locks()
        self.assertEqual(len(data), 1)
        self.assertEqual(response.status_code, 200)

    def test_get_lock_details(self):
        api = self.response_factory(200, response_examples.user_lock)
        response, data = api.get_lock_details('')
        self.assertEqual(response.status_code, 200)

    def test_archive_lock(self):
        api = self.response_factory(204, '')
        response = api.archive_lock('')
        self.assertEqual(response.status_code, 204)

    def test_archive_lock_as_keyholder(self):
        api = self.response_factory(204, '')
        response = api.archive_lock_as_keyholder('')
        self.assertEqual(response.status_code, 204)

    def test_update_lock_time(self):
        api = self.response_factory(204, '')
        response = api.update_lock_duration('', 1)
        self.assertEqual(response.status_code, 204)

    def test_freeze(self):
        api = self.response_factory(204, '')
        response = api.set_freeze('', True)
        self.assertEqual(response.status_code, 204)

    def test_unlock(self):
        api = self.response_factory(204, '')
        response = api.unlock('')
        self.assertEqual(response.status_code, 204)

    def test_lock_settings(self):
        api = self.response_factory(204, '')
        response = api.update_lock_settings('', False, False)
        self.assertEqual(response.status_code, 204)

    def test_set_max_limit_date(self):
        api = self.response_factory(204, '')
        response = api.set_max_limit_date('', datetime.datetime.now(), False)
        self.assertEqual(response.status_code, 204)

    def test_set_keyholder_as_trusted(self):
        api = self.response_factory(204, '')
        response = api.trust_keyholder('')
        self.assertEqual(response.status_code, 204)

    def test_get_lock_combination(self):
        api = self.response_factory(200, response_examples.lock_combination)
        response, data = api.get_lock_combination('')
        self.assertEqual(response.status_code, 200)

    def test_get_lock_history(self):
        api = self.response_factory(201, response_examples.lock_history)
        response, data = api.get_lock_history('')
        self.assertEqual(response.status_code, 201)

    def test_is_test_lock(self):
        api = self.response_factory(200, '')
        response = api.set_as_test_lock('')
        self.assertEqual(response.status_code, 200)

    def test_get_extension_information(self):
        api = self.response_factory(200, response_examples.lock_with_extension)
        response, data = api.get_lock_extension_information('', '')
        self.assertEqual(response.status_code, 200)

    def test_trigger_extension_actions(self):
        api = self.response_factory(201, '')
        response = api.trigger_extension_action('', '', {})
        self.assertEqual(response.status_code, 201)

    """
    Triggers
    """

    def test_vote_in_share_links(self):
        status_code = 201
        api = self.response_factory(status_code, response_examples.share_link_vote_ack, raw_json=True)
        response, data = api.vote_in_share_links('', '', 'remove', '')
        self.assertEqual(response.status_code, status_code)

    def test_get_share_link_url_to_vote(self):
        status_code = 201
        api = self.response_factory(status_code, response_examples.share_link_url_response, raw_json=True)
        response, data = api.get_share_link_vote_url('', '')
        self.assertEqual(response.status_code, status_code)

    def test_get_share_link_info(self):
        status_code = 201
        api = self.response_factory(status_code, response_examples.share_link_info_response)
        response, data = api.get_share_link_vote_info('', '')
        self.assertEqual(response.status_code, status_code)

    def test_place_user_into_pillory(self):
        status_code = 201
        api = self.response_factory(status_code, '')
        response = api.place_user_into_pillory('', '', 'mlem', 3600)
        self.assertEqual(response.status_code, status_code)

    def test_get_current_pillory_info(self):
        status_code = 201
        api = self.response_factory(status_code, response_examples.pillory_info)
        response, data = api.get_current_pillory_info('', '')
        self.assertEqual(response.status_code, status_code)

    def test_unlock_for_hygiene(self):
        status_code = 201
        api = self.response_factory(status_code, '')
        response = api.unlock_for_hygiene('', '', True)
        self.assertEqual(response.status_code, status_code)

    def test_roll_dice(self):
        status_code = 201
        api = self.response_factory(status_code, response_examples.dice_roll_result)
        response, data = api.roll_dice('', '')
        self.assertEqual(response.status_code, status_code)

    def test_spin_wheel_of_fortune(self):
        status_code = 201
        api = self.response_factory(status_code, response_examples.wheel_of_fortune_result)
        response, data = api.spin_wheel_of_fortune('', '')
        self.assertEqual(response.status_code, status_code)

    def test_request_a_random_task(self):
        status_code = 201
        api = self.response_factory(status_code, '')
        response = api.request_a_random_task('', '')
        self.assertEqual(response.status_code, status_code)

    def test_community_vote_next_task(self):
        status_code = 201
        api = self.response_factory(status_code, '')
        response = api.community_vote_next_task('', '', 3600)
        self.assertEqual(response.status_code, status_code)

    def test_mark_task_done(self):
        status_code = 201
        api = self.response_factory(status_code, '')
        response = api.mark_task_done('', '', True)
        self.assertEqual(response.status_code, status_code)

    def test_trigger_new_verification(self):
        status_code = 201
        api = self.response_factory(status_code, '')
        response = api.trigger_new_verification('', '')
        self.assertEqual(response.status_code, status_code)

    def test_trigger_guess_the_timer(self):
        status_code = 201
        api = self.response_factory(status_code, response_examples.guess_the_timer_result)
        response, data = api.trigger_guess_the_timer('', '')
        self.assertEqual(response.status_code, status_code)

    """
    Lock Creation
    """

    def test_create_personal_lock(self):
        status_code = 201
        api = self.response_factory(status_code, response_examples.lock_id_response, raw_json=True)
        response, data = api.create_personal_lock(lock.CreateLock())
        self.assertEqual(response.status_code, status_code)

    def test_add_extensions(self):
        status_code = 201
        api = self.response_factory(status_code, '')
        response = api.edit_extensions('', extensions.Extensions())
        self.assertEqual(response.status_code, status_code)

    def test_create_lock_from_shared_lock(self):
        status_code = 201
        api = self.response_factory(status_code, response_examples.lock_id_response, raw_json=True)
        response, data = api.create_lock_from_shared_lock('', lock.LockInfo())
        self.assertEqual(response.status_code, status_code)

    """
    profile
    """

    def test_get_user_locks(self):
        status_code = 200
        api = self.response_factory(status_code, response_examples.list_of_user_locks)
        response, data = api.get_user_public_locks('')
        self.assertEqual(response.status_code, status_code)

    def test_get_profile(self):
        status_code = 200
        api = self.response_factory(status_code, response_examples.user_profile)
        response, data = api.get_profile('')
        self.assertEqual(response.status_code, status_code)

    def test_find_profile(self):
        status_code = 200
        api = self.response_factory(status_code, response_examples.user_profile)
        response, data = api.find_profile('')
        self.assertEqual(response.status_code, status_code)

    def test_find_profile_detailed(self):
        status_code = 200
        api = self.response_factory(status_code, response_examples.detailed_user_profile)
        response, data = api.find_profile_detailed('')
        self.assertEqual(response.status_code, status_code)

    def test_get_badges(self):
        status_code = 200
        api = self.response_factory(status_code, response_examples.user_badges)
        response, data = api.get_badges()
        self.assertEqual(response.status_code, status_code)

    def test_update_profile(self):
        status_code = 200
        api = self.response_factory(status_code, response_examples.user_auth_profile)
        response, data = api.update_profile()
        self.assertEqual(response.status_code, status_code)

    def test_get_your_profile(self):
        status_code = 200
        api = self.response_factory(status_code, response_examples.user_auth_profile)
        response, data = api.get_user_profile()
        self.assertEqual(response.status_code, status_code)

    """
    Files
    """

    # def upload_file(self) -> tuple[requests.models.Response, user.FileToken]:
    def test_upload_file(self):
        status_code = 201
        api = self.response_factory(status_code, response_examples.file_token, raw_json=True)
        response, data = api.upload_file('./tests/test_api_mock_chaster.py',
                                         'test.png',
                                         'image/png')
        self.assertEqual(response.status_code, status_code)

    # def find_file(self, file_key) -> tuple[requests.models.Response, user.FileUrl]:
    def test_find_file(self):
        status_code = 200
        api = self.response_factory(status_code, response_examples.file_url, raw_json=True)
        response, data = api.find_file('')
        self.assertEqual(response.status_code, status_code)

    """
    Combinations
    """

    # def upload_combination_image(self) -> tuple[requests.models.Response, lock.Combination]:
    def test_upload_combination_image(self):
        status_code = 201
        api = self.response_factory(status_code, response_examples.combination_id_response, raw_json=True)
        response, data = api.upload_combination_image('./tests/test_api_mock_chaster.py',
                                                      'test.png',
                                                      'image/png')
        self.assertEqual(response.status_code, status_code)

    # def create_combination_code(self, code: str) -> tuple[requests.models.Response, lock.Combination]:
    def test_create_combination_code(self):
        status_code = 201
        api = self.response_factory(status_code, response_examples.combination_id_response, raw_json=True)
        response, data = api.create_combination_code('')
        self.assertEqual(response.status_code, status_code)

    """
    Extensions
    """

    # def get_all_known_extensions(self) -> tuple[requests.models.Response, list[extensions.KnownExtension]]:
    def test_get_all_known_extensions(self):
        status_code = 200
        api = self.response_factory(status_code, response_examples.all_known_extensions)
        response, data = api.get_all_known_extensions()
        self.assertEqual(response.status_code, status_code)

    """
    Session Offer
    """

    def test_create_keyholding_offer(self):
        status_code = 201
        api = self.response_factory(status_code, '')
        response = api.create_keyholding_offer('', '')
        self.assertEqual(response.status_code, status_code)

    def test_accept_keyholding_request(self):
        status_code = 200
        api = self.response_factory(status_code, '')
        response = api.accept_keyholding_request('')
        self.assertEqual(response.status_code, status_code)

    def test_get_keyholding_offers(self):
        status_code = 200
        api = self.response_factory(status_code, response_examples.keyholder_offers)
        response, data = api.get_sent_keyholding_offers('')
        self.assertEqual(response.status_code, status_code)

    def test_retrieve_keyholder_request_lock_info(self):
        status_code = 200
        api = self.response_factory(status_code, response_examples.user_lock)
        response, data = api.retrieve_keyholder_request_lock_info('')
        self.assertEqual(response.status_code, status_code)

    def test_handle_keyholding_offer(self):
        status_code = 201
        api = self.response_factory(status_code, '')
        response = api.resolve_keyholding_offer('', False)
        self.assertEqual(response.status_code, status_code)

    def test_archive_keyholding_offer(self):
        status_code = 200
        api = self.response_factory(status_code, '')
        response = api.archive_keyholding_offer('')
        self.assertEqual(response.status_code, status_code)

    def test_get_keyholding_offers_from_wearers(self):
        status_code = 200
        api = self.response_factory(status_code, response_examples.wearer_offers)
        response, data = api.get_keyholding_offers_from_wearers()
        self.assertEqual(response.status_code, status_code)

    """
    Messaging
    """

    def test_get_conversations(self):
        status_code = 200
        api = self.response_factory(status_code, response_examples.conversations_list)
        response, data = api.get_conversations()
        self.assertEqual(response.status_code, status_code)

    def test_create_conversation(self):
        status_code = 201
        api = self.response_factory(status_code, response_examples.conversation)
        response, data = api.create_conversation('', '')
        self.assertEqual(response.status_code, status_code)

    def test_get_user_conversation(self):
        status_code = 200
        api = self.response_factory(status_code, response_examples.conversation)
        response, data = api.get_user_conversation('')
        self.assertEqual(response.status_code, status_code)

    def test_post_message(self):
        status_code = 201
        api = self.response_factory(status_code, response_examples.conversation_messasge)
        response, data = api.send_message('', '')
        self.assertEqual(response.status_code, status_code)

    def test_get_conversation(self):
        status_code = 200
        api = self.response_factory(status_code, response_examples.conversation)
        response, data = api.get_conversation('')
        self.assertEqual(response.status_code, status_code)

    def test_set_conversation_status(self):
        status_code = 201
        api = self.response_factory(status_code, '')
        response = api.set_conversation_status('', '')
        self.assertEqual(response.status_code, status_code)

    def test_set_conversation_unread(self):
        status_code = 201
        api = self.response_factory(status_code, '')
        response = api.set_conversation_unread('', False)
        self.assertEqual(response.status_code, status_code)

    def test_get_conversation_messages(self):
        status_code = 200
        api = self.response_factory(status_code, response_examples.conversation_messages)
        response, data = api.get_conversation_messages('')
        self.assertEqual(response.status_code, status_code)

    """
    Extensions - Temporary Opening
    """

    def test_get_temporary_opening_combination(self):
        status_code = 200
        api = self.response_factory(status_code, response_examples.lock_combination)
        response, data = api.get_temporary_opening_combination('')
        self.assertEqual(response.status_code, status_code)

    def test_set_temporary_opening_new_combination(self):
        status_code = 201
        api = self.response_factory(status_code, '')
        response = api.set_temporary_opening_new_combination('', '')
        self.assertEqual(response.status_code, status_code)

    def test_get_temporary_opening_combination_from_action_log(self):
        status_code = 200
        api = self.response_factory(status_code, response_examples.lock_combination)
        response, data = api.get_temporary_opening_combination_from_action_log('', '')
        self.assertEqual(response.status_code, status_code)

    """
    Community Events
    """

    def test_get_community_event_categories(self):
        status_code = 200
        api = self.response_factory(status_code, response_examples.community_event_category_list)
        response, data = api.get_community_event_categories()
        self.assertEqual(response.status_code, status_code)

    def test_get_community_event_details(self):
        status_code = 201
        api = self.response_factory(status_code, response_examples.community_event_details)
        response, data = api.get_community_event_details()
        self.assertEqual(response.status_code, status_code)

    """
    Partner Extensions
    """

    """
    Settings
    """

    def test_get_app_settings(self):
        status_code = 200
        api = self.response_factory(status_code, response_examples.app_settings)
        response, data = api.get_app_settings()
        self.assertEqual(response.status_code, status_code)

    """
    Users
    """

    # def search_for_users(self, search: str) -> tuple[requests.models.Response, list[user.User]]:
    def test_search_for_users(self):
        status_code = 201
        api = self.response_factory(status_code, response_examples.list_of_users)
        response, data = api.search_for_users('')
        self.assertEqual(response.status_code, status_code)

    # def search_for_users_by_discord(self, discord_id: str) -> tuple[requests.models.Response, user.User]:
    def test_search_for_users_by_discord(self):
        status_code = 200
        api = self.response_factory(status_code, response_examples.user_profile)
        response, data = api.search_for_users_by_discord('')
        self.assertEqual(response.status_code, status_code)

    """
    Keyholder
    """

    def test_post_keyholder_locks_search(self):
        status_code = 201
        api = self.response_factory(status_code, response_examples.locked_users)
        response, data = api.find_locked_users()
        self.assertEqual(response.status_code, status_code)

    """
    Reports
    """

    """
    Partner Configurations
    """

    """
    Public Locks
    """

    def test_find_public_shared_lock(self):
        status_code = 200
        api = self.response_factory(status_code, response_examples.public_shared_lock)
        response, data = api.find_public_shared_lock('')
        self.assertEqual(response.status_code, status_code)

    def test_generate_public_shared_lock_flyer(self):
        status_code = 200
        api = self.response_factory(status_code, '{}')
        response = api.generate_public_shared_lock_flyer('', './here.png')
        self.assertEqual(response.status_code, status_code)

    def test_search_for_public_locks(self):
        status_code = 201
        api = self.response_factory(status_code, response_examples.search_public_locks)
        spl = lock.SearchPublicLock()
        response, data = api.search_for_public_locks(spl)
        self.assertEqual(response.status_code, status_code)

    def test_find_explore_page_locks(self):
        status_code = 200
        api = self.response_factory(status_code, response_examples.explore_page_locks)
        response, data = api.find_explore_page_locks()
        self.assertEqual(response.status_code, status_code)

    """
    Extensions - Verification Picture
    """

    # def submit_verification(self, lock_id: str) -> requests.models.Response:
    def test_submit_verification(self):
        status_code = 201
        api = self.response_factory(status_code, '')
        response = api.submit_verification('', './tests/test.png',
                                           'test.png',
                                           'image/png')
        self.assertEqual(response.status_code, status_code)

    # def get_verification_history(self, lock_id: str) -> tuple
    def test_get_verification_history(self):
        status_code = 200
        api = self.response_factory(status_code, response_examples.verification_history)
        response, data = api.get_verification_history('')
        self.assertEqual(response.status_code, status_code)


if __name__ == '__main__':
    unittest.main()
