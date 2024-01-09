#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Module documentation goes here."""
import datetime
import unittest
from unittest.mock import MagicMock
from requests import Response
import json
from src.api import ChasterAPI
import src.shared_lock as shared_lock
from types import SimpleNamespace


class MyTestCase(unittest.TestCase):

    def test_get_shared_locks_success(self):
        tests = [
            ("""[
  {
    "_id": "65872d75d061f19e4e4a0a55",
    "minDuration": 345600,
    "maxDuration": 345600,
    "maxLimitDuration": 604800,
    "minDate": null,
    "maxDate": null,
    "maxLimitDate": null,
    "displayRemainingTime": false,
    "limitLockTime": true,
    "maxLockedUsers": 3,
    "isPublic": false,
    "requireContact": true,
    "name": "🟧 The Foundry: Assimilation ⬛⬛",
    "password": "IWantToBeADrone",
    "description": "The Foundry is looking for Drone Candidates.Here you will become a pup drone. Your assimilation will be guided by The Foundry's central AI. Join and become One. Kinks: Dronification, identity loss, humiliation Gear needed: dildo, butt plug, chastity cagePassword:IWantToBeADroneNotes:Responses to the bot are always start with TRANSACTION: #. Bot will give response examples to each task. Bot will have a deliberate delay from the completion of one task to the next.What will happen is you'll get a message that is a task and you'll have to complete it. The bot checks in every half hour and delays between tasks to start the next on. You'll get your first message within 30 min of joining.",
    "unsplashPhoto": {
      "id": "Sj_3Jdr19L4",
      "name": "Alek Kalinowski",
      "url": "https://images.unsplash.com/flagged/photo-1595524288414-a7fda0a12d0c?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3wxMzE4NDZ8MHwxfGFsbHx8fHx8fHx8fDE3MDMzNTc4MTN8&ixlib=rb-4.0.3&q=80&w=1080",
      "username": "alekversusworld"
    },
    "hideTimeLogs": true,
    "lastSavedAt": "2024-01-03T19:13:59.683Z",
    "requirePassword": true,
    "user": "64e5b481b533a5ccfe61567f",
    "durationMode": "duration",
    "isFindom": false,
    "calculatedMaxLimitDuration": 604800,
    "extensions": []
  },
  {
    "_id": "6583af7cb03643ca3e788e7f",
    "minDuration": 3600,
    "maxDuration": 7200,
    "maxLimitDuration": null,
    "minDate": null,
    "maxDate": null,
    "maxLimitDate": null,
    "displayRemainingTime": true,
    "limitLockTime": false,
    "maxLockedUsers": null,
    "isPublic": false,
    "requireContact": true,
    "name": "test api call",
    "password": "asdf",
    "description": "test api call",
    "unsplashPhoto": {
      "id": "tXq0AMYB4WQ",
      "name": "Viktor Bystrov",
      "url": "https://images.unsplash.com/photo-1542895947-dec6fb64f71e?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3wxMzE4NDZ8MHwxfGFsbHx8fHx8fHx8fDE3MDMxMjg5NTZ8&ixlib=rb-4.0.3&q=80&w=1080",
      "username": "xokvictor"
    },
    "hideTimeLogs": false,
    "lastSavedAt": "2023-12-21T06:08:20.146Z",
    "requirePassword": true,
    "user": "64e5b481b533a5ccfe61567f",
    "durationMode": "duration",
    "isFindom": false,
    "calculatedMaxLimitDuration": null,
    "extensions": [
      {
        "slug": "verification-picture",
        "config": {
          "visibility": "keyholder",
          "peerVerification": {
            "enabled": true,
            "punishments": [
              {
                "name": "add_time",
                "params": 3600
              },
              {
                "name": "freeze"
              },
              {
                "name": "pillory",
                "params": {
                  "duration": 900
                }
              }
            ]
          }
        },
        "mode": "non_cumulative",
        "regularity": 86400,
        "name": "Verification picture",
        "textConfig": ""
      },
      {
        "slug": "pillory",
        "config": {
          "timeToAdd": 3600,
          "limitToLoggedUsers": true
        },
        "mode": "unlimited",
        "regularity": 3600,
        "name": "Pillory",
        "textConfig": "1 hour added per vote"
      }
    ]
  },
  {
    "_id": "65827bb4d1f699fb821e915f",
    "minDuration": 86400,
    "maxDuration": 90000,
    "maxLimitDuration": null,
    "minDate": null,
    "maxDate": null,
    "maxLimitDate": null,
    "displayRemainingTime": true,
    "limitLockTime": false,
    "maxLockedUsers": null,
    "isPublic": false,
    "requireContact": true,
    "name": "Bark Bot",
    "password": "done",
    "description": "Bark! A bot controlled lock.Looking for beta testers.Bark will do random things to your lock. A human will be there to make sure everything stays safe.Trust after entering.",
    "unsplashPhoto": {
      "id": "U32jeOdkgfA",
      "name": "Brett Jordan",
      "url": "https://images.unsplash.com/photo-1559715541-d4fc97b8d6dd?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3wxMzE4NDZ8MHwxfGFsbHx8fHx8fHx8fDE3MDMwNTAxNjR8&ixlib=rb-4.0.3&q=80&w=1080",
      "username": "brett_jordan"
    },
    "hideTimeLogs": false,
    "lastSavedAt": "2023-12-25T20:06:26.219Z",
    "requirePassword": true,
    "user": "64e5b481b533a5ccfe61567f",
    "durationMode": "duration",
    "isFindom": false,
    "calculatedMaxLimitDuration": null,
    "extensions": []
  },
  {
    "_id": "65584f37f173429ea76c40b6",
    "minDuration": 86400,
    "maxDuration": 259200,
    "maxLimitDuration": null,
    "minDate": null,
    "maxDate": null,
    "maxLimitDate": null,
    "displayRemainingTime": true,
    "limitLockTime": false,
    "maxLockedUsers": null,
    "isPublic": false,
    "requireContact": true,
    "name": "Femboy Pups",
    "password": "nope",
    "description": "Come be a good girl and join my lock! That means you too, the curious one who clicked on this and thinks they aren't a good girl. Interaction based lock.",
    "unsplashPhoto": {
      "id": "ZPwTWULq9xw",
      "name": "Gursimrat Ganda",
      "url": "https://images.unsplash.com/photo-1608113239923-a0bf3a1e873f?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3wxMzE4NDZ8MHwxfGFsbHx8fHx8fHx8fDE3MDAyODYyNjN8&ixlib=rb-4.0.3&q=80&w=1080",
      "username": "gurysimrat"
    },
    "hideTimeLogs": false,
    "lastSavedAt": "2023-12-25T21:50:47.117Z",
    "requirePassword": true,
    "user": "64e5b481b533a5ccfe61567f",
    "durationMode": "duration",
    "isFindom": false,
    "calculatedMaxLimitDuration": null,
    "extensions": [
      {
        "slug": "verification-picture",
        "config": {
          "visibility": "all",
          "peerVerification": {
            "enabled": false,
            "punishments": []
          }
        },
        "mode": "non_cumulative",
        "regularity": 86400,
        "name": "Verification picture",
        "textConfig": ""
      }
    ]
  },
  {
    "_id": "654d9cd9f5da1eca165ee734",
    "minDuration": 86400,
    "maxDuration": 259200,
    "maxLimitDuration": null,
    "minDate": null,
    "maxDate": null,
    "maxLimitDate": null,
    "displayRemainingTime": true,
    "limitLockTime": false,
    "maxLockedUsers": null,
    "isPublic": false,
    "requireContact": true,
    "name": "For my amusement ",
    "password": "nope",
    "description": "Join and become my new toy. Expect to end up begging. Message me about how grateful you are to be in the lock before you join.",
    "unsplashPhoto": {
      "id": "F3Dde_9thd8",
      "name": "NordWood Themes",
      "url": "https://images.unsplash.com/photo-1510127034890-ba27508e9f1c?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3wxMzE4NDZ8MHwxfGFsbHx8fHx8fHx8fDE2OTk1ODUyNDF8&ixlib=rb-4.0.3&q=80&w=1080",
      "username": "nordwood"
    },
    "hideTimeLogs": false,
    "lastSavedAt": "2023-12-25T21:50:59.581Z",
    "requirePassword": true,
    "user": "64e5b481b533a5ccfe61567f",
    "durationMode": "duration",
    "isFindom": false,
    "calculatedMaxLimitDuration": null,
    "extensions": [
      {
        "slug": "verification-picture",
        "config": {
          "visibility": "all",
          "peerVerification": {
            "enabled": false,
            "punishments": []
          }
        },
        "mode": "non_cumulative",
        "regularity": 86400,
        "name": "Verification picture",
        "textConfig": ""
      }
    ]
  },
  {
    "_id": "65139d7d1a72a968b46338e4",
    "minDuration": 0,
    "maxDuration": 0,
    "maxLimitDuration": null,
    "minDate": "2023-11-01T06:59:00.000Z",
    "maxDate": "2023-11-01T06:59:02.312Z",
    "maxLimitDate": null,
    "displayRemainingTime": true,
    "limitLockTime": true,
    "maxLockedUsers": null,
    "isPublic": true,
    "requireContact": false,
    "name": "Pup Locktober",
    "password": null,
    "description": "",
    "unsplashPhoto": {
      "id": "4cirNi6WvRg",
      "name": "David Izquierdo",
      "url": "https://images.unsplash.com/photo-1572290603512-cd1d7dad06e5?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3wxMzE4NDZ8MHwxfGFsbHx8fHx8fHx8fDE2OTU3ODQzMTd8&ixlib=rb-4.0.3&q=80&w=1080",
      "username": "davidiz"
    },
    "hideTimeLogs": false,
    "lastSavedAt": "2023-09-27T03:11:57.595Z",
    "requirePassword": false,
    "user": "64e5b481b533a5ccfe61567f",
    "durationMode": "date",
    "isFindom": false,
    "calculatedMaxLimitDuration": 0,
    "extensions": [
      {
        "slug": "temporary-opening",
        "config": {
          "openingTime": 900,
          "penaltyTime": 43200,
          "allowOnlyKeyholderToOpen": false
        },
        "mode": "non_cumulative",
        "regularity": 172800,
        "name": "Hygiene opening",
        "textConfig": "Time allowed: 15 minutes, penalty for exceeding time: 12 hours"
      }
    ]
  },
  {
    "_id": "64e69feb2f626eb789dafd6e",
    "minDuration": 14400,
    "maxDuration": 86400,
    "maxLimitDuration": 86400,
    "minDate": null,
    "maxDate": null,
    "maxLimitDate": null,
    "displayRemainingTime": true,
    "limitLockTime": true,
    "maxLockedUsers": null,
    "isPublic": false,
    "requireContact": true,
    "name": "Pup Search Lock",
    "password": "nope",
    "description": "Hmu pups! And join the lock if you like.",
    "unsplashPhoto": {
      "id": "WSAOGHKEqFc",
      "name": "Bruce Warrington",
      "url": "https://images.unsplash.com/photo-1556866261-8763a7662333?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3wxMzE4NDZ8MHwxfGFsbHx8fHx8fHx8fDE2OTI4MzU4MTl8&ixlib=rb-4.0.3&q=80&w=1080",
      "username": "brucebmax"
    },
    "hideTimeLogs": false,
    "lastSavedAt": "2023-12-25T21:51:09.511Z",
    "requirePassword": true,
    "user": "64e5b481b533a5ccfe61567f",
    "durationMode": "duration",
    "isFindom": false,
    "calculatedMaxLimitDuration": 86400,
    "extensions": []
  }
]""", 7),
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
        csl = shared_lock.CreateSharedLock()
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
        json_in = """
        {
  "_id": "65139d7d1a72a968b46338e4",
  "minDuration": 0,
  "maxDuration": 0,
  "maxLimitDuration": null,
  "minDate": "2023-11-01T06:59:00.000Z",
  "maxDate": "2023-11-01T06:59:02.312Z",
  "maxLimitDate": null,
  "displayRemainingTime": true,
  "limitLockTime": true,
  "maxLockedUsers": null,
  "isPublic": true,
  "requireContact": false,
  "name": "Pup Locktober",
  "password": null,
  "description": "",
  "unsplashPhoto": {
    "id": "4cirNi6WvRg",
    "name": "David Izquierdo",
    "url": "https://images.unsplash.com/photo-1572290603512-cd1d7dad06e5?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3wxMzE4NDZ8MHwxfGFsbHx8fHx8fHx8fDE2OTU3ODQzMTd8&ixlib=rb-4.0.3&q=80&w=1080",
    "username": "davidiz"
  },
  "hideTimeLogs": false,
  "lastSavedAt": "2023-09-27T03:11:57.595Z",
  "requirePassword": false,
  "user": {
    "_id": "64e5b481b533a5ccfe61567f",
    "username": "PupHimbo",
    "isPremium": false,
    "description": "Pup looking for more friends, cuddles, and cum, and maybe a cage. Aspiring to be a slutty Himbo pup",
    "location": "San Francisco ",
    "gender": "Male",
    "age": 27,
    "role": "switch",
    "isFindom": false,
    "avatarUrl": "https://cdn01.chaster.app/app/uploads/avatars/EfcMg0h1HiLUc67j.jpg",
    "online": false,
    "lastSeen": null,
    "isAdmin": false,
    "isModerator": false,
    "metadata": {
      "locktober2020Points": 0,
      "locktober2021Points": 0,
      "chastityMonth2022Points": 0,
      "locktober2022Points": 0,
      "locktober2023Points": 1240
    },
    "fullLocation": "San Francisco , California, United States",
    "discordId": "1153172669559214141",
    "discordUsername": "puphimbo",
    "isDisabled": false,
    "isSuspended": false,
    "features": [],
    "joinedAt": "2023-08",
    "isNewMember": false,
    "isSuspendedOrDisabled": false
  },
  "durationMode": "date",
  "isFindom": false,
  "calculatedMaxLimitDuration": 0,
  "extensions": [
    {
      "slug": "temporary-opening",
      "config": {
        "openingTime": 900,
        "penaltyTime": 43200,
        "allowOnlyKeyholderToOpen": false
      },
      "mode": "non_cumulative",
      "regularity": 172800,
      "name": "Hygiene opening",
      "textConfig": "Time allowed: 15 minutes, penalty for exceeding time: 12 hours"
    }
  ]
}
        """
        api = ChasterAPI('')
        response = Response()
        response.json = MagicMock(
            return_value=json.loads(json_in, object_hook=lambda d: SimpleNamespace(**d)))
        response.status_code = 200
        api._get = MagicMock(return_value=response)
        _, data = api.get_shared_lock_details('65139d7d1a72a968b46338e4')
        self.assertEqual(data._id, '65139d7d1a72a968b46338e4')


if __name__ == '__main__':
    unittest.main()
