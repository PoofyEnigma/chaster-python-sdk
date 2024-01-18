import datetime
import time

import src.api as api
import src.lock as lock
import src.extensions as extensions
import unittest
import uuid
import logging
import os
from dateutil.tz import tzutc

chaster_api = api.ChasterAPI(os.environ.get('CHASTER_BEARER_TOKEN'), user_agent='PythonSDKDeveloplment/1.0')
chaster_api_lockee = api.ChasterAPI(os.environ.get('CHASTER_BEARER_TOKEN_II'), user_agent='PythonSDKDeveloplment/1.0')


class ApiTestCases(unittest.TestCase):

    def out_test(self, response, data):
        time.sleep(0)

    """
    Shared Locks
    """

    @unittest.SkipTest
    def test_get_shared_locks_active(self):
        response, data = chaster_api.get_shared_locks()
        self.out_test(response, data)
        assert response.status_code == 200

    @unittest.SkipTest
    def test_get_locks(self):
        response, data = chaster_api.get_locks()
        self.out_test(response, data)
        assert response.status_code == 200

    @unittest.SkipTest
    def test_create_get_update_get_archive_shared_lock(self):
        csl = lock.CreateSharedLock()
        csl.minDuration = 3600
        csl.maxDuration = 7200
        csl.maxLimitDuration = None
        csl.minDate = datetime.datetime.now()
        csl.maxDate = datetime.datetime.now() + datetime.timedelta(days=7)
        csl.maxLimitDate = None
        csl.displayRemainingTime = True
        csl.limitLockTime = False
        csl.maxLockedUsers = None
        csl.isPublic = False
        csl.password = ''
        csl.requireContact = False
        csl.name = uuid.uuid4().hex
        csl.description = 'Test'
        csl.photoId = ''
        csl.hideTimeLogs = False
        csl.isFindom = False
        response, lock_id_data = chaster_api.create_shared_lock(csl)
        response, data = chaster_api.get_shared_lock_details(lock_id_data.id)
        self.assertFalse(data.hideTimeLogs)
        csl.hideTimeLogs = True
        _ = chaster_api.update_shared_lock(lock_id_data.id, csl)
        response, data = chaster_api.get_shared_lock_details(lock_id_data.id)
        self.assertTrue(data.hideTimeLogs)
        _ = chaster_api.archive_shared_lock(lock_id_data.id)

    @unittest.SkipTest
    def test_favortie_check_remove(self):
        id = '659c6b549e2355d6c5e8dd55'
        response, data = chaster_api.check_if_favorited(id)
        self.assertEqual(response.status_code, 200)
        self.assertFalse(data)

        response = chaster_api.favorite(id)
        self.assertEqual(response.status_code, 200)

        response, data = chaster_api.check_if_favorited(id)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(data)

        response = chaster_api.remove_favorite(id)
        self.assertEqual(response.status_code, 200)

        response, data = chaster_api.check_if_favorited(id)
        self.assertEqual(response.status_code, 200)
        self.assertFalse(data)

    @unittest.SkipTest
    def test_get_favorited_shared_locks(self):
        response, data = chaster_api.get_favorited_shared_locks()
        self.assertEqual(response.status_code, 201)
        self.assertTrue(len(data.results) > 0)

    """
    Locks
    """

    @unittest.SkipTest
    def test_get_locks_and_details(self):
        response, locks = chaster_api.get_locks('archived')
        self.assertEqual(response.status_code, 200)

        response, profile = chaster_api.get_your_profile()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(locks[0].user._id, profile._id)

        response, lock = chaster_api.get_lock_details(locks[0]._id)
        self.assertEqual(response.status_code, 200)

    @unittest.SkipTest
    def test_update_lock_time(self):
        response, combination = chaster_api_lockee.create_combination_code('1234')

        l = lock.LockInfo()
        l.isTestLock = True
        l.combinationId = combination.combinationId
        l.password = 'puppy'
        response, lock_id = chaster_api_lockee.create_lock_from_shared_lock('64e69feb2f626eb789dafd6e', l)

        response, locks = chaster_api_lockee.get_locks()
        lock_before = locks[0]

        _ = chaster_api.freeze(lock_id.lockId, True)
        _ = chaster_api_lockee.update_lock_time(lock_id.lockId, 10000)

        response, locks = chaster_api_lockee.get_locks()
        lock_after = locks[0]
        self.assertFalse(lock_before.isFrozen)
        self.assertGreater(lock_after.endDate, lock_before.endDate)
        self.assertTrue(lock_after.isFrozen)

        _ = chaster_api.unlock(lock_id.lockId)
        _ = chaster_api_lockee.archive_lock(lock_id.lockId)

    @unittest.SkipTest
    def test_set_keyholder_as_trusted(self):
        _, combination = chaster_api_lockee.create_combination_code('1234')

        l = lock.LockInfo()
        l.isTestLock = False
        l.combinationId = combination.combinationId
        l.password = 'puppy'
        _, lock_id = chaster_api_lockee.create_lock_from_shared_lock('64e69feb2f626eb789dafd6e', l)

        response = chaster_api.lock_settings(lock_id.lockId, False, True)
        self.assertEqual(response.status_code, 204)
        response = chaster_api_lockee.set_keyholder_as_trusted(lock_id.lockId)
        self.assertEqual(response.status_code, 204)
        max_limit_date = datetime.datetime.now(tz=tzutc()) + datetime.timedelta(days=30)
        response = chaster_api_lockee.set_max_limit_date(lock_id.lockId,
                                                         max_limit_date, False)
        self.assertEqual(response.status_code, 204)

        response, locked_users = chaster_api.post_keyholder_locks_search()
        self.assertIsNotNone(locked_users)
        self.assertEqual(len(locked_users.locks), 1)
        lock_before = locked_users.locks[0]
        self.assertTrue(lock_before.trusted)
        # self.assertEqual(lock_before.maxLimitDate, max_limit_date)
        self.assertFalse(lock_before.displayRemainingTime)
        self.assertTrue(lock_before.hideTimeLogs)

        max_limit_date = datetime.datetime.now(tz=tzutc()) + datetime.timedelta(days=40)
        response = chaster_api_lockee.set_max_limit_date(lock_id.lockId, max_limit_date, True)
        self.assertEqual(response.status_code, 204)

        response, locked_users = chaster_api.post_keyholder_locks_search()
        self.assertIsNotNone(locked_users)
        self.assertEqual(len(locked_users.locks), 1)
        lock_after = locked_users.locks[0]
        self.assertIsNone(lock_after.maxLimitDate)

        _ = chaster_api.unlock(lock_id.lockId)
        _ = chaster_api_lockee.archive_lock(lock_id.lockId)
        response = chaster_api_lockee.is_test_lock(lock_id.lockId)
        self.assertEqual(response.status_code, 200)

    """
    Lock Creation
    """

    @unittest.SkipTest
    def test_create_personal_lock(self):
        response, combination = chaster_api_lockee.create_combination_code('1234')
        self.assertIsNotNone(combination)
        self.assertNotEqual(combination.combinationId, '')

        l = lock.CreateLock()
        l.minDuration = 0
        l.maxDuration = 1
        l.isTestLock = True
        l.combinationId = combination.combinationId
        response, lock_data = chaster_api_lockee.create_personal_lock(l)
        self.assertIsNotNone(lock_data)
        self.assertNotEqual(lock_data.lockId, '')
        time.sleep(l.maxDuration)
        response = chaster_api_lockee.unlock(lock_data.lockId)
        self.assertEqual(response.status_code, 204)

        response = chaster_api_lockee.archive_lock(lock_data.lockId)
        self.assertEqual(response.status_code, 204)

        response, lock_data = chaster_api_lockee.get_locks()
        self.assertIsNotNone(lock_data)
        self.assertEqual(len(lock_data), 0)
        self.assertEqual(response.status_code, 200)

    @unittest.SkipTest
    def test_add_extensions(self):
        response, combination = chaster_api_lockee.upload_combination_image('./tests/test.png')
        self.assertIsNotNone(combination)
        self.assertNotEqual(combination.combinationId, '')

        l = lock.LockInfo()
        l.isTestLock = True
        l.combinationId = combination.combinationId
        l.password = 'puppy'
        response, lock_id = chaster_api_lockee.create_lock_from_shared_lock('64e69feb2f626eb789dafd6e', l)
        self.assertIsNotNone(lock_id)
        self.assertNotEqual(lock_id.lockId, '')

        response = chaster_api_lockee.set_keyholder_as_trusted(lock_id.lockId)
        self.assertEqual(response.status_code, 204)

        eh = extensions.ExtensionsHandler()
        ho = extensions.HygieneOpening()
        eh.add(ho)
        e = extensions.Extensions()
        e.extensions = eh.dump()
        response = chaster_api.add_extensions(lock_id.lockId, e)
        self.assertEqual(response.status_code, 201)

        response, locked_users = chaster_api.post_keyholder_locks_search()
        self.assertIsNotNone(locked_users)
        self.assertEqual(len(locked_users.locks), 1)
        lock_after = locked_users.locks[0]

        response, extensions_info = chaster_api.get_extension_information(lock_id.lockId, lock_after.extensions[0]._id)
        self.assertIsNotNone(extensions_info)
        self.assertIsNotNone(extensions_info.extension)

        _ = chaster_api.unlock(lock_id.lockId)

        response, lock_combo = chaster_api_lockee.get_lock_combination(lock_id.lockId)
        self.assertIsNotNone(lock_combo)

        response, lock_history = chaster_api_lockee.get_lock_history(lock_id.lockId)
        self.assertIsNotNone(lock_history)

        _ = chaster_api_lockee.archive_lock(lock_id.lockId)

    @unittest.SkipTest
    def test_create_lock_from_shared_lock(self):
        response, combination = chaster_api_lockee.upload_combination_image('./tests/test.png')
        self.assertIsNotNone(combination)
        self.assertNotEqual(combination.combinationId, '')

        l = lock.LockInfo()
        l.isTestLock = True
        l.combinationId = combination.combinationId
        l.password = 'puppy'
        response, lock_id = chaster_api_lockee.create_lock_from_shared_lock('64e69feb2f626eb789dafd6e', l)
        self.assertIsNotNone(lock_id)
        self.assertNotEqual(lock_id.lockId, '')

        response = chaster_api.unlock(lock_id.lockId)
        self.assertEqual(response.status_code, 204)

        response = chaster_api.archive_lock_as_keyholder(lock_id.lockId)
        self.assertEqual(response.status_code, 204)

        response, locked_users = chaster_api.post_keyholder_locks_search()
        self.assertIsNotNone(locked_users)
        self.assertEqual(len(locked_users.locks), 0)

        response = chaster_api_lockee.archive_lock(lock_id.lockId)
        self.assertEqual(response.status_code, 204)

        response, lock_data = chaster_api_lockee.get_locks()
        self.assertIsNotNone(lock_data)
        self.assertEqual(len(lock_data), 0)
        self.assertEqual(response.status_code, 200)

    """
    Profile
    """

    @unittest.SkipTest
    def test_get_your_profile(self):
        response, profile = chaster_api.get_your_profile()
        self.assertIsNotNone(profile)

        response, profile = chaster_api.update_profile()
        self.assertIsNotNone(profile)

        response, badges = chaster_api.get_badges()
        self.assertIsNotNone(badges)

        response, detailed_user = chaster_api.find_profile_detailed('PupHimbo')
        self.assertIsNotNone(detailed_user)

        response, user = chaster_api.find_profile('PupHimbo')
        self.assertIsNotNone(user)

        response, profile = chaster_api.get_profile(profile._id)
        self.assertIsNotNone(profile)

        response, locks = chaster_api.get_user_locks(profile._id)
        self.assertIsNotNone(locks)

    """
    Files
    """

    @unittest.SkipTest
    def test_upload_and_find_file(self):
        response, file_info = chaster_api.upload_file('./tests/test.png')
        self.assertIsNotNone(file_info)

        # now can use the file to send a message

    @unittest.SkipTest
    def test_find_file(self):
        self.assertTrue(False)

    """
    Combinations
    """

    """
    Extensions
    """

    @unittest.SkipTest
    def test_get_all_known_extensions(self):
        response, known_extensions = chaster_api.get_all_known_extensions()
        self.assertIsNotNone(known_extensions)

    """
    Session Offer
    """

    @unittest.SkipTest
    def test_accept_session_offer(self):
        _, combination = chaster_api_lockee.create_combination_code('1234')

        l = lock.CreateLock()
        l.minDuration = 0
        l.maxDuration = 1
        l.isTestLock = True
        l.combinationId = combination.combinationId
        _, lock_data = chaster_api_lockee.create_personal_lock(l)

        response, user = chaster_api.get_your_profile()

        response = chaster_api_lockee.create_keyholding_offer(lock_data.lockId, user.username)
        self.assertEqual(response.status_code, 201)

        response, user_offers = chaster_api_lockee.get_keyholding_offers(lock_data.lockId)
        self.assertIsNotNone(user_offers)
        self.assertGreaterEqual(len(user_offers), 1)

        response, offers = chaster_api.get_keyholding_offers_from_wearers()
        self.assertIsNotNone(offers)
        self.assertGreaterEqual(len(offers), 1)

        response = chaster_api.handle_keyholding_offer(offers[0]._id, True)
        self.assertEqual(response.status_code, 201)

        _ = chaster_api.unlock(lock_data.lockId)
        _ = chaster_api_lockee.archive_lock(lock_data.lockId)

    @unittest.SkipTest
    def test_refuse_session_offer(self):
        _, combination = chaster_api_lockee.create_combination_code('1234')

        l = lock.CreateLock()
        l.minDuration = 0
        l.maxDuration = 1
        l.isTestLock = True
        l.combinationId = combination.combinationId
        _, lock_data = chaster_api_lockee.create_personal_lock(l)

        response, user = chaster_api.get_your_profile()

        response = chaster_api_lockee.create_keyholding_offer(lock_data.lockId, user.username)
        self.assertEqual(response.status_code, 201)

        response, user_offers = chaster_api_lockee.get_keyholding_offers(lock_data.lockId)
        self.assertIsNotNone(user_offers)
        self.assertGreaterEqual(len(user_offers), 1)

        _, locks = chaster_api_lockee.get_locks()

        response, user_lock = chaster_api.retrieve_keyholder_request_lock_info(locks[0].offerToken)
        self.assertIsNotNone(user_lock)

        response = chaster_api.accept_keyholding_request(locks[0].offerToken)
        self.assertEqual(response.status_code, 200)

        _ = chaster_api.unlock(lock_data.lockId)
        _ = chaster_api_lockee.archive_lock(lock_data.lockId)

    @unittest.SkipTest
    def test_archive_session_offer(self):
        _, combination = chaster_api_lockee.create_combination_code('1234')

        l = lock.CreateLock()
        l.minDuration = 0
        l.maxDuration = 1
        l.isTestLock = True
        l.combinationId = combination.combinationId
        _, lock_data = chaster_api_lockee.create_personal_lock(l)

        response, user = chaster_api.get_your_profile()

        response = chaster_api_lockee.create_keyholding_offer(lock_data.lockId, user.username)
        self.assertEqual(response.status_code, 201)

        response, user_offers = chaster_api_lockee.get_keyholding_offers(lock_data.lockId)

        response = chaster_api_lockee.archive_keyholding_offer(user_offers[0]._id)
        self.assertEqual(response.status_code, 200)

        _ = chaster_api_lockee.unlock(lock_data.lockId)
        _ = chaster_api_lockee.archive_lock(lock_data.lockId)

    """
    Messaging
    """

    @unittest.SkipTest
    def test_conversations(self):
        response, conversations = chaster_api.get_conversations()
        self.assertIsNotNone(conversations)

        response, conversation = chaster_api.get_conversation(conversations.results[0]._id)
        self.assertIsNotNone(conversation)

        response, messages = chaster_api.get_conversation_messages(conversations.results[0]._id)
        self.assertIsNotNone(messages)

    @unittest.SkipTest
    def test_conversations_sending_messages(self):
        _, profile = chaster_api_lockee.get_your_profile()
        _, conversation = chaster_api.get_user_conversation(profile._id)
        self.assertIsNotNone(conversation)

        response, message = chaster_api.post_message(conversation._id, 'hello')
        self.assertIsNotNone(message)

        _, conversation = chaster_api.create_conversation(profile._id, 'create')
        self.assertIsNotNone(conversation)

        response = chaster_api.set_conversation_status(conversation._id, 'approved')
        self.assertEqual(response.status_code, 200)

        response = chaster_api.set_conversation_unread(conversation._id, True)
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    log_format = '%(asctime)s %(name)s %(levelname)s %(message)s'
    root_logger = logging.getLogger()
    logging.basicConfig(filename='./out.log',
                        format=log_format,
                        level=logging.DEBUG)

    stream_handler = logging.StreamHandler()
    root_logger.addHandler(stream_handler)
    stream_handler.setFormatter(logging.Formatter(log_format))
    unittest.main()
