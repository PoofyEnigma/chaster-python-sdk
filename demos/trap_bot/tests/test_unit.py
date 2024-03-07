import unittest
from unittest.mock import MagicMock, Mock

from chaster import lock

from shared import shared
from trap_bot import app


class Unit(unittest.TestCase):
    def test_run_success(self):
        rsl = shared.resolve_shared_lock
        glu = shared.get_locked_users
        chaster_api = Mock()
        sl = lock.SharedLock()
        sl._id = 'sl_id'
        sl.name = 'Bot Trap'
        shared.resolve_shared_lock = MagicMock(return_value=sl)

        # no locked users at all
        chaster_api.update_lock_settings = MagicMock()
        chaster_api.place_user_into_pillory = MagicMock()
        shared.get_locked_users = MagicMock(return_value=[])
        app.run(chaster_api)
        shared.get_locked_users.assert_called_once()
        shared.resolve_shared_lock.assert_called()
        chaster_api.update_lock_settings.assert_not_called()
        chaster_api.place_user_into_pillory.assert_not_called()

        # no locked users in the lock
        chaster_api.update_lock_settings = MagicMock()
        chaster_api.place_user_into_pillory = MagicMock()
        l = lock.Lock()
        l.sharedLock = lock.SharedLock()
        l.sharedLock.name = 'not'
        shared.get_locked_users = MagicMock(return_value=[l])
        app.run(chaster_api)
        shared.get_locked_users.assert_called_once()
        shared.resolve_shared_lock.assert_called()
        chaster_api.update_lock_settings.assert_not_called()
        chaster_api.place_user_into_pillory.assert_not_called()

        # locked users in the lock but all trapped
        chaster_api.update_lock_settings = MagicMock()
        chaster_api.place_user_into_pillory = MagicMock()
        l = lock.Lock()
        l.sharedLock = sl
        l.displayRemainingTime = False
        shared.get_locked_users = MagicMock(return_value=[l])
        app.run(chaster_api)
        shared.get_locked_users.assert_called_once()
        shared.resolve_shared_lock.assert_called()
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
        shared.get_locked_users = MagicMock(return_value=[l])
        app.run(chaster_api)
        shared.get_locked_users.assert_called_once()
        shared.resolve_shared_lock.assert_called()
        chaster_api.update_lock_settings.assert_called_once()
        chaster_api.place_user_into_pillory.assert_called_once()

        # multiple runs
        chaster_api.update_lock_settings = MagicMock()
        chaster_api.place_user_into_pillory = MagicMock()
        l = lock.Lock()
        l.sharedLock = sl
        l.displayRemainingTime = False
        shared.get_locked_users = MagicMock(return_value=[l])
        app.run(chaster_api)
        app.run(chaster_api)
        app.run(chaster_api)
        shared.get_locked_users.assert_called()
        shared.resolve_shared_lock.assert_called()
        chaster_api.update_lock_settings.assert_not_called()
        chaster_api.place_user_into_pillory.assert_not_called()

        shared.resolve_shared_lock = rsl
        shared.get_locked_users = glu
