import datetime
import unittest
from unittest.mock import MagicMock, Mock

from chaster import lock, extensions, api

from demos.trap_bot import app


class Unit(unittest.TestCase):
    def test_publish_shared_lock_success(self):
        chaster_api = Mock()
        response = Mock()
        response.status_code = 201
        chaster_api.create_shared_lock = MagicMock(return_value=(response, 'shared_lock_id'))
        response2 = Mock()
        response2.status_code = 200
        chaster_api.put_shared_lock_extensions = MagicMock(return_value=response2)
        sl = Mock()
        sl._id = 'shared_lock_id'
        chaster_api.get_shared_lock_details = MagicMock(return_value=(response2, sl))

        csl = lock.CreateSharedLock()
        ext = extensions.Extensions()
        out = app.publish_shared_lock(chaster_api, csl, ext)
        self.assertEqual(out._id, sl._id)
        chaster_api.create_shared_lock.assert_called_with(csl)
        chaster_api.put_shared_lock_extensions.assert_called_with('shared_lock_id', ext)
        chaster_api.get_shared_lock_details.assert_called_with('shared_lock_id')

    def test_publish_shared_lock_rollback(self):
        chaster_api = Mock()
        response = Mock()
        response.status_code = 201
        chaster_api.create_shared_lock = MagicMock(return_value=(response, 'shared_lock_id'))
        response2 = Mock()
        response2.status_code = 500
        chaster_api.put_shared_lock_extensions = MagicMock(return_value=response2)
        chaster_api.archive_shared_lock = MagicMock(return_value=response)

        csl = lock.CreateSharedLock()
        ext = extensions.Extensions()
        out = app.publish_shared_lock(chaster_api, csl, ext)
        self.assertIsNone(out)
        chaster_api.create_shared_lock.assert_called_with(csl)
        chaster_api.put_shared_lock_extensions.assert_called_with('shared_lock_id', ext)
        chaster_api.archive_shared_lock.assert_called_with('shared_lock_id')

    def test_resolve_shared_lock_success(self):
        psl = app.publish_shared_lock
        chaster_api = Mock()
        csl = lock.CreateSharedLock()
        ext = extensions.Extensions()

        # no shared locks present
        response = Mock()
        response.status_code = 200
        chaster_api.get_user_shared_locks = MagicMock(return_value=(response, []))
        sl = lock.SharedLock()
        sl.name = 'Bot Trap'
        sl.lastSavedAt = datetime.datetime.now().astimezone()
        app.publish_shared_lock = MagicMock(return_value=sl)

        rsl = app.resolve_shared_lock(chaster_api, csl, ext)
        self.assertEqual(sl.name, rsl.name)
        chaster_api.get_user_shared_locks.assert_called()
        app.publish_shared_lock.assert_called()

        # shared locks present but no trap bot
        response = Mock()
        response.status_code = 200
        nsl = lock.SharedLock()
        nsl.name = 'size lock'
        chaster_api.get_user_shared_locks = MagicMock(return_value=(response, [nsl]))
        sl = lock.SharedLock()
        sl.name = 'Bot Trap'
        sl.lastSavedAt = datetime.datetime.now().astimezone()
        app.publish_shared_lock = MagicMock(return_value=sl)

        rsl = app.resolve_shared_lock(chaster_api, csl, ext)
        self.assertEqual(sl.name, rsl.name)
        chaster_api.get_user_shared_locks.assert_called()
        app.publish_shared_lock.assert_called()

        # trap bot present amongst shared locks
        response = Mock()
        response.status_code = 200
        nsl = lock.SharedLock()
        nsl.name = 'size lock'
        sl = lock.SharedLock()
        sl.name = 'Bot Trap'
        sl.lastSavedAt = datetime.datetime.now().astimezone()
        app.publish_shared_lock = MagicMock(return_value=sl)
        chaster_api.get_user_shared_locks = MagicMock(return_value=(response, [nsl, sl]))

        rsl = app.resolve_shared_lock(chaster_api, csl, ext)
        self.assertEqual(sl.name, rsl.name)
        chaster_api.get_user_shared_locks.assert_called()
        app.publish_shared_lock.assert_not_called()

        # trap bot present amongst shared locks and is out of date
        response = Mock()
        response.status_code = 200
        nsl = lock.SharedLock()
        nsl.name = 'size lock'

        sl2 = lock.SharedLock()
        sl2._id = 'sl_id2'
        sl2.name = 'Bot Trap'

        app.publish_shared_lock = MagicMock(return_value=sl2)
        sl = lock.SharedLock()
        sl._id = 'sl_id'
        sl.name = 'Bot Trap'
        sl.lastSavedAt = datetime.datetime.now().astimezone() - datetime.timedelta(days=8)

        chaster_api.get_user_shared_locks = MagicMock(return_value=(response, [nsl, sl]))
        response2 = Mock()
        response2.status_code = 201
        chaster_api.archive_shared_lock = MagicMock(return_value=response2)

        rsl = app.resolve_shared_lock(chaster_api, csl, ext)
        self.assertEqual(sl.name, rsl.name)
        chaster_api.get_user_shared_locks.assert_called()
        app.publish_shared_lock.assert_called()
        chaster_api.archive_shared_lock.assert_called_with(sl._id)

        app.publish_shared_lock = psl

    def test_get_locked_users(self):
        chaster_api = Mock()

        # 0 pages
        lu = lock.LockedUsers()
        lu.pages = 0
        lu.total = 0
        lu.locks = []
        chaster_api.find_locked_users = MagicMock(return_value=(None, lu))
        chaster_api.update_lock_settings = MagicMock()
        app.get_locked_users(chaster_api)

        chaster_api.find_locked_users.assert_called_once()

        # 1 pages
        lu = lock.LockedUsers()
        lu.pages = 1
        lu.total = 0
        lu.locks = []
        chaster_api.find_locked_users = MagicMock(return_value=(None, lu))
        chaster_api.update_lock_settings = MagicMock()
        app.get_locked_users(chaster_api)

        chaster_api.find_locked_users.assert_called_once()

        # 2 page
        lu = lock.LockedUsers()
        lu.pages = 2
        lu.total = 0
        lu.locks = []
        chaster_api.find_locked_users = MagicMock(return_value=(None, lu))
        chaster_api.update_lock_settings = MagicMock()
        app.get_locked_users(chaster_api)

        self.assertEqual(chaster_api.find_locked_users.call_count, 2)

        # n page
        lu = lock.LockedUsers()
        lu.pages = 7
        lu.total = 0
        lu.locks = []
        chaster_api.find_locked_users = MagicMock(return_value=(None, lu))
        chaster_api.update_lock_settings = MagicMock()
        app.get_locked_users(chaster_api)

        self.assertEqual(chaster_api.find_locked_users.call_count, 7)

    def test_run_success(self):
        rsl = app.resolve_shared_lock
        glu = app.get_locked_users
        chaster_api = Mock()
        sl = lock.SharedLock()
        sl._id = 'sl_id'
        sl.name = 'Bot Trap'
        app.resolve_shared_lock = MagicMock(return_value=sl)

        # no locked users at all
        chaster_api.update_lock_settings = MagicMock()
        chaster_api.place_user_into_pillory = MagicMock()
        app.get_locked_users = MagicMock(return_value=[])
        app.run(chaster_api)
        app.get_locked_users.assert_called_once()
        app.resolve_shared_lock.assert_called()
        chaster_api.update_lock_settings.assert_not_called()
        chaster_api.place_user_into_pillory.assert_not_called()

        # no locked users in the lock
        chaster_api.update_lock_settings = MagicMock()
        chaster_api.place_user_into_pillory = MagicMock()
        l = lock.Lock()
        l.sharedLock = lock.SharedLock()
        l.sharedLock.name = 'not'
        app.get_locked_users = MagicMock(return_value=[l])
        app.run(chaster_api)
        app.get_locked_users.assert_called_once()
        app.resolve_shared_lock.assert_called()
        chaster_api.update_lock_settings.assert_not_called()
        chaster_api.place_user_into_pillory.assert_not_called()

        # locked users in the lock but all trapped
        chaster_api.update_lock_settings = MagicMock()
        chaster_api.place_user_into_pillory = MagicMock()
        l = lock.Lock()
        l.sharedLock = sl
        l.displayRemainingTime = False
        app.get_locked_users = MagicMock(return_value=[l])
        app.run(chaster_api)
        app.get_locked_users.assert_called_once()
        app.resolve_shared_lock.assert_called()
        chaster_api.update_lock_settings.assert_not_called()
        chaster_api.place_user_into_pillory.assert_not_called()

        # locked users in the lock and need trapped
        chaster_api.update_lock_settings = MagicMock()
        chaster_api.place_user_into_pillory = MagicMock()
        l = lock.Lock()
        l.sharedLock = sl
        l.displayRemainingTime = True
        p = MagicMock()
        p.slug = 'pillory'
        p._id = ''
        l.extensions = [p]
        app.get_locked_users = MagicMock(return_value=[l])
        app.run(chaster_api)
        app.get_locked_users.assert_called_once()
        app.resolve_shared_lock.assert_called()
        chaster_api.update_lock_settings.assert_called_once()
        chaster_api.place_user_into_pillory.assert_called_once()

        # multiple runs
        chaster_api.update_lock_settings = MagicMock()
        chaster_api.place_user_into_pillory = MagicMock()
        l = lock.Lock()
        l.sharedLock = sl
        l.displayRemainingTime = False
        app.get_locked_users = MagicMock(return_value=[l])
        app.run(chaster_api)
        app.run(chaster_api)
        app.run(chaster_api)
        app.get_locked_users.assert_called()
        app.resolve_shared_lock.assert_called()
        chaster_api.update_lock_settings.assert_not_called()
        chaster_api.place_user_into_pillory.assert_not_called()

        app.resolve_shared_lock = rsl
        app.get_locked_users = glu
