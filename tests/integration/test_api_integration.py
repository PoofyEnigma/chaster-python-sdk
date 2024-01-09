import datetime
import time

import src.api as api
import src.shared_lock as shared_lock
import unittest
import uuid
import logging
import os


chaster_api = api.ChasterAPI(os.environ.get('CHASTER_BEARER_TOKEN'))
other_user_id = '65873830075fc043537113ee'

class ApiTestCases(unittest.TestCase):

    def out_test(self, response, data):
        time.sleep(0)

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
        csl = shared_lock.CreateSharedLock()
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
    def test_archive_lock(self):
        self.assertFalse(True)

    @unittest.SkipTest
    def test_archive_lock_as_keyholder(self):
        self.assertFalse(True)

    @unittest.SkipTest
    def test_update_lock_time(self):
        self.assertFalse(True)

    @unittest.SkipTest
    def test_freeze_lock(self):
        self.assertFalse(True)

    @unittest.SkipTest
    def test_unlock(self):
        self.assertFalse(True)


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
