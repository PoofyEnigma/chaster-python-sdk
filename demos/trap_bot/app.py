from chaster import api, extensions, lock
import datetime
import logging
import os
import time

logging.basicConfig(filename='./log.txt')
logger = logging.getLogger()
logger.setLevel(logging.INFO)
shared_lock_name = 'Bot Trap'


def publish_shared_lock() -> lock.SharedLock | None:
    global shared_lock_name
    csl = lock.CreateSharedLock()
    csl.minDuration = int(datetime.timedelta(minutes=30).total_seconds())
    csl.maxDuration = int(datetime.timedelta(minutes=120).total_seconds())
    csl.maxLimitDuration = int(datetime.timedelta(days=7).total_seconds())
    csl.displayRemainingTime = True
    csl.limitLockTime = True
    csl.name = shared_lock_name
    csl.description = 'Bot checks periodically and sleeps for long periods occasionally. Those caught will be pilloried. Lock up and have fun!'
    csl.photoId = 'IYhFK0bne7Y'
    resp, id = chaster_api.create_shared_lock(csl)
    if resp.status_code != 201:
        logger.error(f'could not create new shared lock')
        return None

    p = extensions.Pillory()
    p.config = extensions.PilloryConfig()
    p.config.timeToAdd = int(datetime.timedelta(hours=2).total_seconds())
    p.config.limitToLoggedUsers = False

    verification = extensions.VerificationPicture()
    verification.config = extensions.VerificationPictureConfig()
    verification.regularity = int(datetime.timedelta(days=1).total_seconds())
    verification.config.visibility = 'all'
    verification.config.peerVerification = extensions.PeerVerification()
    verification.config.peerVerification.enabled = True
    pillory_punishment = extensions.PunishmentPillory(datetime.timedelta(hours=1).total_seconds())
    verification.config.peerVerification.punishments.append(pillory_punishment)

    eh = extensions.ExtensionsHandler()
    eh.add_defined(p)
    eh.add_defined(verification)

    resp = chaster_api.edit_extensions()
    eh.generate_array()

def readvertise_shared_lock(shared_lock: lock.SharedLock) -> lock.SharedLock | None:
    resp = chaster_api.archive_shared_lock(shared_lock._id)
    if resp.status_code != 201:
        logger.error(f'could not archive shared lock {shared_lock.name} due to {resp.status_code} - {resp.text}')
        return None
    return publish_shared_lock()


while True:
    global shared_lock_name
    try:
        logger.warning('starting')
        chaster_api = api.ChasterAPI(os.environ.get('CHASTER_BEARER_TOKEN'), user_agent='puphimbo/1.0')
        lock_name = shared_lock_name

        resp, shared_locks = chaster_api.get_user_shared_locks()
        trap_shared_lock: lock.SharedLock = None
        for shared_lock in shared_locks:
            if shared_lock.name == lock_name:
                trap_shared_lock = shared_lock
                break
        else:
            trap_shared_lock = publish_shared_lock()

        if trap_shared_lock is None:
            logger.warning('could not resolve the shared lock')
            continue

        if trap_shared_lock.lastSavedAt + datetime.timedelta(days=7) <= datetime.datetime.now():
            readvertise_shared_lock(trap_shared_lock)

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
