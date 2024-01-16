import datetime
import time

import src.api as api
import src.lock as lock
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

    @unittest.SkipTest
    def test_get_lock_combination(self):
        self.assertFalse(True)

    @unittest.SkipTest
    def test_get_lock_history(self):
        self.assertFalse(True)

    @unittest.SkipTest
    def test_get_extension_information(self):
        self.assertFalse(True)

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
        self.assertFalse(True)

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

    """
    Files
    """

    """
    Combinations
    """


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
