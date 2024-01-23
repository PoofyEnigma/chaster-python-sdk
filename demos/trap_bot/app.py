from chaster import api, extensions
import datetime
import logging
import os
import time

logging.basicConfig(filename='./log.txt')
logger = logging.getLogger()
logger.setLevel(logging.INFO)

while True:
    try:
        logger.warning('starting')
        chaster_api = api.ChasterAPI(os.environ.get('CHASTER_BEARER_TOKEN'), user_agent='puphimbo/1.0')
        lock_name = 'Bot Trap'

        resp, shared_locks = chaster_api.get_user_shared_locks()
        trap_shared_lock = None
        for shared_lock in shared_locks:
            if shared_lock.name == lock_name:
                trap_shared_lock = shared_lock
                break
        else:
            logger.warning('could not find the shared lock')
            continue

        # could also use the search function, but post_keyholder_locks_search needs revamped
        resp, locked_users_page = chaster_api.find_locked_users()
        locked_users = locked_users_page.locks
        for page in range(2, locked_users_page.pages):
            resp, locked_users_page = chaster_api.find_locked_users(page=page)
            locked_users.extend(locked_users_page.locks)

        for lock in locked_users:
            if lock.sharedLock.name == 'Bot Trap':
                if lock.displayRemainingTime:
                    chaster_api.update_lock_settings(lock._id, False, True)
                    eh = extensions.ExtensionsHandler()
                    eh.load_defined(lock.extensions)
                    chaster_api.place_user_into_pillory(lock._id, eh.pillories[0]._id, 'caught!',
                                                        datetime.timedelta(hours=2).total_seconds())
    except Exception as e:
        logger.error(f'error - {type(e).__name__} {e}')
    finally:
        time.sleep(datetime.timedelta(minutes=60).total_seconds())
