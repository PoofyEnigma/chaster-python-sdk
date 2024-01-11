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
        id = '12345'
        response.json = MagicMock(
            return_value=json.loads('{"id": "' + id + '"}', object_hook=lambda d: SimpleNamespace(**d)))
        response.status_code = 201
        api._post = MagicMock(return_value=response)
        _, data = api.create_shared_lock(csl)
        self.assertEqual(data.id, id)

    def test_get_shared_lock_details(self):
        api = ChasterAPI('')
        response = Response()
        response.json = MagicMock(
            return_value=json.loads(response_examples.shared_lock_details, object_hook=lambda d: SimpleNamespace(**d)))
        response.status_code = 200
        api._get = MagicMock(return_value=response)
        _, data = api.get_shared_lock_details('65139d7d1a72a968b46338e4')
        self.assertEqual(data._id, '65139d7d1a72a968b46338e4')

    # def update_shared_lock(self, shared_lock_id: str, update: lock.CreateSharedLock) -> requests.models.Response:
    def test_update_shared_lock(self):
        csl = self.generate_csl()
        api = ChasterAPI('')
        response = Response()
        response.status_code = 200
        api._put = MagicMock(return_value=response)
        response = api.update_shared_lock('', csl)
        self.assertEqual(response.status_code, 200)

    # def archive_shared_lock(self, shared_lock_id: str):
    def test_archive_shared_lock(self):
        api = ChasterAPI('')
        response = Response()
        response.status_code = 200
        api._post = MagicMock(return_value=response)
        response = api.archive_shared_lock('')
        self.assertEqual(response.status_code, 200)

    # def check_if_favorited(self, shared_lock_id: str) -> tuple[requests.models.Response, bool]:
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


    # def favorite(self, shared_lock_id: str) -> requests.models.Response:
    def test_favorite(self):
        api = ChasterAPI('')
        response = Response()
        response.status_code = 200
        api._put = MagicMock(return_value=response)
        response = api.favorite('')
        self.assertEqual(response.status_code, 200)

    # def remove_favorite(self, shared_lock_id: str) -> requests.models.Response:
    def test_remove_favorite(self):
        api = ChasterAPI('')
        response = Response()
        response.status_code = 200
        api._delete = MagicMock(return_value=response)
        response = api.remove_favorite('')
        self.assertEqual(response.status_code, 200)

    # def get_favorited_shared_locks(self, limit: int = 15, lastId: str = None) -> tuple[
    def test_get_favorited_shared_locks(self):
        api = ChasterAPI('')
        response = Response()
        response.status_code = 201
        response.json = MagicMock(
            return_value=json.loads(response_examples.get_favorited_share_locks, object_hook=lambda d: SimpleNamespace(**d)))
        api._post = MagicMock(return_value=response)
        response, data = api.get_favorited_shared_locks()
        self.assertEqual(response.status_code, 201)
        self.assertEqual(len(data.results), 3)


if __name__ == '__main__':
    unittest.main()
