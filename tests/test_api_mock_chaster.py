#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Module documentation goes here."""
import datetime
import unittest
from unittest.mock import MagicMock
from requests import Response
import json
from src.api import ChasterAPI
import src.lock as lock
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
                response, data = api.get_shared_locks()
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
                response, data = api.get_shared_locks(status=test[1])
                self.assertEqual(len(data), 0, msg=None)

    def test_get_shared_locks_by_status_failure(self):
        with self.assertRaises(ValueError):
            api = ChasterAPI('')
            _, _ = api.get_shared_locks(status='asdf')

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

    def test_create_shared_lock_fail(self):

        tests = [
            ('min duration gt max duration', self.generate_csl(min_duration=51, max_duration=50)),
            ('max duration gt limit duration',
             self.generate_csl(max_duration=50, maxLimitDuration=49, limitLockTime=True)),
            ('min date gt max date', self.generate_csl(minDate=datetime.datetime.now() + datetime.timedelta(hours=8),
                                                       maxDate=datetime.datetime.now())),
            ('max date gt limit date', self.generate_csl(minDate=datetime.datetime.now(),
                                                         maxDate=datetime.datetime.now() + datetime.timedelta(hours=8),
                                                         maxLimitDate=datetime.datetime.now(),
                                                         limitLockTime=True)),
            ('max date none min date not none', self.generate_csl(minDate=datetime.datetime.now(),
                                                                  maxDate=None)),
            ('max date not none min date none', self.generate_csl(minDate=None,
                                                                  maxDate=datetime.datetime.now())),
            ('limit duration set but limit lock time is not', self.generate_csl(min_duration=49, max_duration=50,
                                                                                maxLimitDuration=51)),
            ('limit date set but limit lock time is not', self.generate_csl(minDate=datetime.datetime.now(),
                                                                            maxDate=datetime.datetime.now(),
                                                                            maxLimitDate=datetime.datetime.now() + datetime.timedelta(
                                                                                hours=8))),
        ]
        for test in tests:
            with self.subTest(name=test[0]):
                with self.assertRaises(ValueError):
                    api = ChasterAPI('')
                    # avoid making an api call if the exception is not raised
                    response = Response()
                    response.status_code = 500
                    api._post = MagicMock(return_value=response)
                    _, _ = api.create_shared_lock(test[1])

    def test_create_shared_lock_success(self):
        csl = self.generate_csl()
        api = ChasterAPI('')
        # avoid making an api call if the exception is not raised
        response = Response()
        response.json = MagicMock(
            return_value=json.loads(response_examples.created_shared_lock, object_hook=lambda d: SimpleNamespace(**d)))
        response.status_code = 201
        api._post = MagicMock(return_value=response)
        _, data = api.create_shared_lock(csl)
        self.assertEqual(data.id, '12345')

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
        response, data = api.get_favorited_shared_locks()
        self.assertEqual(response.status_code, 201)
        self.assertEqual(len(data.results), 3)

    """
    Locks
    """

    def response_factory(self, status_code, json_str):
        if json_str == '':
            json_str = '{}'
        api = ChasterAPI('')
        response = Response()
        response.status_code = status_code
        response.json = MagicMock(
            return_value=json.loads(json_str, object_hook=lambda d: SimpleNamespace(**d)))
        api._get = MagicMock(return_value=response)
        api._post = MagicMock(return_value=response)
        api._put = MagicMock(return_value=response)
        api._delete = MagicMock(return_value=response)
        return api

    # def get_locks(self, status: str = 'active') -> tuple[requests.models.Response, list[lock.Lock]]:
    def test_get_locks(self):
        api = self.response_factory(200, response_examples.list_of_user_locks)
        response, data = api.get_locks()
        self.assertEqual(len(data), 1)
        self.assertEqual(response.status_code, 200)

    # def get_lock_details(self, lock_id: str) -> tuple[requests.models.Response, lock.Lock]:
    def test_get_lock_details(self):
        api = self.response_factory(200, response_examples.user_lock)
        response, data = api.get_lock_details('')
        self.assertEqual(response.status_code, 200)

    # def archive_lock(self, lock_id: str) -> requests.models.Response:
    def test_archive_lock(self):
        api = self.response_factory(204, '')
        response = api.archive_lock('')
        self.assertEqual(response.status_code, 204)

    # def archive_lock_as_keyholder(self, lock_id: str) -> requests.models.Response:
    def test_archive_lock_as_keyholder(self):
        api = self.response_factory(204, '')
        response = api.archive_lock_as_keyholder('')
        self.assertEqual(response.status_code, 204)

    # def update_lock_time(self, lock_id: str, time_seconds: int):
    def test_update_lock_time(self):
        api = self.response_factory(204, '')
        response = api.update_lock_time('', 1)
        self.assertEqual(response.status_code, 204)

    # def freeze(self, lock_id: str, freeze: bool) -> requests.models.Response:
    def test_freeze(self):
        api = self.response_factory(204, '')
        response = api.freeze('', True)
        self.assertEqual(response.status_code, 204)

    # def unlock(self, lock_id: str) -> requests.models.Response:
    def test_unlock(self):
        api = self.response_factory(204, '')
        response = api.unlock('')
        self.assertEqual(response.status_code, 204)

    # def lock_settings(self, lock_id: str, display_remaining_time: bool, hide_time_logs: bool) -> requests.models.Response:
    def test_lock_settings(self):
        api = self.response_factory(204, '')
        response = api.lock_settings('', False, False)
        self.assertEqual(response.status_code, 204)

    # def set_max_limit_date(self, lock_id: str, max_limit_date: datetime.datetime, disable_max_time_limit: bool) -> requests.models.Response:
    def test_set_max_limit_date(self):
        api = self.response_factory(204, '')
        response = api.set_max_limit_date('', datetime.datetime.now(), False)
        self.assertEqual(response.status_code, 204)

    # def set_keyholder_as_trusted(self, lock_id: str) -> requests.models.Response:
    def test_set_keyholder_as_trusted(self):
        api = self.response_factory(204, '')
        response = api.set_keyholder_as_trusted('')
        self.assertEqual(response.status_code, 204)

    # def get_lock_combination(self, lock_id: str) -> tuple[requests.models.Response, any]:
    def test_get_lock_combination(self):
        api = self.response_factory(200, response_examples.lock_combination)
        response, data = api.get_lock_combination('')
        self.assertEqual(response.status_code, 200)

    # def get_lock_history(self, lock_id: str, extension: str = None, limit: int = None, last_id: str = None) -> tuple[
    def test_get_lock_history(self):
        api = self.response_factory(201, response_examples.lock_history)
        response, data = api.get_lock_history('')
        self.assertEqual(response.status_code, 201)

    # def is_test_lock(self, lock_id) -> requests.models.Response:
    def test_is_test_lock(self):
        api = self.response_factory(200, '')
        response = api.is_test_lock('')
        self.assertEqual(response.status_code, 200)

    # def get_extension_information(self, lock_id: str, extension_id: str) -> tuple[
    def test_get_extension_information(self):
        api = self.response_factory(200, response_examples.lock_with_extension)
        response, data = api.get_extension_information('', '')
        self.assertEqual(response.status_code, 200)

    # def trigger_extension_actions(self, lock_id: str, extension_id: str, data: any) -> requests.models.Response:
    def test_trigger_extension_actions(self):
        api = self.response_factory(201, '')
        response = api.trigger_extension_actions('', '', {})
        self.assertEqual(response.status_code, 201)

    """
    Triggers
    """

    # def _tester_post_request_helper(self, response, update):

    # def vote_in_share_links(self, lock_id: str, extension_id: str, data: triggers.ShareLinksVote) -> tuple[

    # def get_share_link_url_to_vote(self, lock_id: str, extension_id: str) -> tuple[

    # def get_share_link_info(self, lock_id: str, extension_id: str) -> tuple[

    # def place_user_into_pillory(self, lock_id: str, extension_id: str,

    # def get_current_pillory_info(self, lock_id: str, extension_id: str) -> tuple[

    # def unlock_for_hygiene(self, lock_id: str, extension_id: str, is_you: bool) -> requests.models.Response:

    # def roll_dice(self, lock_id: str, extension_id: str) -> tuple[

    # def spin_wheel_of_fortune(self, lock_id: str, extension_id: str) -> tuple[

    # def request_a_random_task(self, lock_id: str, extension_id: str) -> requests.models.Response:

    # def community_vote_next_task(self, lock_id: str, extension_id: str, vote_duration: int) -> requests.models.Response:

    # def mark_task_done(self, lock_id: str, extension_id: str, succeeded: bool) -> requests.models.Response:

    # def trigger_new_verification(self, lock_id: str, extension_id: str) -> requests.models.Response:

    # def trigger_guess_the_timer(self, lock_id: str, extension_id: str) -> tuple[

    """
    Lock Creation
    """

    # def create_personal_lock(self, self_lock: lock.Lock) -> tuple[requests.models.Response, lock.LockId]:

    # def add_extensions(self, lock_id: str, ext: extensions.Extensions) -> requests.models.Response:

    # def create_lock_from_shared_lock(self, shared_lock_id: str, lock_details: lock.LockInfo) -> tuple[

    """
    profile
    """

    # def get_user_locks(self, user_id: str) -> tuple[requests.models.Response, list[lock.Lock]]:

    # def get_profile(self, user_id: str) -> tuple[requests.models.Response, user.User]:

    # def find_profile(self, username: str) -> tuple[requests.models.Response, user.User]:

    # def find_profile_detailed(self, username: str) -> tuple[requests.models.Response, user.DetailedUser]:

    # def get_badges(self) -> tuple[requests.models.Response, user.Badges]:

    # def update_profile(self) -> tuple[requests.models.Response, user.AuthProfile]:

    # def get_your_profile(self) -> tuple[requests.models.Response, user.AuthProfile]:

    """
    Files
    """

    # def upload_file(self) -> tuple[requests.models.Response, user.FileToken]:

    # def find_file(self, file_key) -> tuple[requests.models.Response, user.FileUrl]:

    """
    Combinations
    """

    # def upload_combination_image(self) -> tuple[requests.models.Response, lock.Combination]:

    # def create_combination_code(self, code: str) -> tuple[requests.models.Response, lock.Combination]:

    """
    Extensions
    """

    # def get_all_known_extensions(self) -> tuple[requests.models.Response, list[extensions.KnownExtension]]:

    """
    Session Offer
    """

    # def create_keyholding_offer(self, lock_id, keyholder: str) -> requests.models.Response:

    # def accept_keyholding_request(self, offer_token: str) -> requests.models.Response:

    # def get_keyholding_offers(self, lock_id: str) -> tuple[requests.models.Response, list[user.KeyholderOfferEntry]]:

    # def retrieve_keyholder_request_lock_info(self, offer_token: str) -> tuple[requests.models.Response, lock.Lock]:

    # def handle_keyholding_offer(self, session_request_id, do_accept) -> requests.models.Response:

    # def archive_keyholding_offer(self, session_request_id) -> requests.models.Response:

    # def get_keyholding_offers_from_wearers(self) -> tuple[requests.models.Response, list[user.KeyholderOfferEntry]]:

    """
    Messaging
    """

    # def get_conversations(self, limit: int = 15, status: str = 'approved') -> tuple[

    # def create_conversation(self, user_id: str, message: str) -> tuple[

    # def get_user_conversation(self, user_id: str) -> tuple[requests.models.Response, conversation.Conversation]:

    # def post_message(self, conversation_id: str, message: str) -> tuple[requests.models.Response, conversation.Message]:

    # def get_conversation(self, conversation_id: str) -> tuple[requests.models.Response, conversation.Conversation]:

    # def set_conversation_status(self, conversation_id, status: str) -> requests.models.Response:

    # def set_conversation_unread(self, conversation_id, unread: bool) -> requests.models.Response:

    # def get_conversation_messages(self, conversation_id: str, limit=15, lastId=None) -> tuple[

    """
    Extensions - Temporary Opening
    """

    # def get_temporary_opening_combination(self, lock_id: str) -> tuple[requests.models.Response, user.LockCombination]:

    # def set_temporary_opening_new_combination(self, lock_id: str, combination_id: str) -> requests.models.Response:

    # def get_temporary_opening_combination_from_action_log(self, action_log_id: str, lock_id: str) -> tuple[

    """
    Community Events
    """

    # def get_community_event_categories(self) -> tuple[

    # def get_community_event_details(self, date: datetime.datetime = datetime.datetime.now()) -> tuple[

    """
    Partner Extensions
    """
    # TODO: Gain access

    """
    Settings
    """

    # def get_app_settings(self) -> tuple[requests.models.Response, user.AppSettings]:

    """
    Users
    """

    # def search_for_users(self, search: str) -> tuple[requests.models.Response, list[user.User]]:

    # def search_for_users_by_discord(self, discord_id: str) -> tuple[requests.models.Response, user.User]:

    """
    Keyholder
    """

    # def post_keyholder_locks_search(self, page: int = 0, status: str = 'locked', limit: int = 15, criteria: dict = {},

    """
    Reports
    """

    # def post_report(self):

    """
    Partner Configurations
    """
    # TODO: Gain access

    """
    Public Locks
    """

    # def find_public_shared_lock(self, shared_lock_id: str) -> tuple[

    # def generate_public_shared_lock_flyer(self, shared_lock_id: str) -> requests.models.Response:

    # def search_for_public_locks(self, searchPublicLock: lock.SearchPublicLock) -> \

    # def find_explore_page_locks(self) -> tuple[requests.models.Response, lock.ExplorePageLock]:

    """
    Extensions - Verification Picture
    """

    # def submit_verification(self, lock_id: str) -> requests.models.Response:

    # def get_verification_history(self, lock_id: str) -> tuple


if __name__ == '__main__':
    unittest.main()
