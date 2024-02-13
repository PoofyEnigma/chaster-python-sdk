from chaster import api, extensions, lock
import datetime
import logging
import os
import time

from shared import shared

logging.basicConfig(filename='./log.txt')
logger = logging.getLogger()
logger.setLevel(logging.INFO)
shared_lock_name = 'Bot Trap'

csl = lock.CreateSharedLock()
csl.minDuration = int(datetime.timedelta(minutes=30).total_seconds())
csl.maxDuration = int(datetime.timedelta(minutes=120).total_seconds())
csl.maxLimitDuration = int(datetime.timedelta(days=7).total_seconds())
csl.displayRemainingTime = True
csl.limitLockTime = True
csl.name = shared_lock_name
csl.description = 'Bot checks periodically and sleeps for long periods occasionally. Those caught will be pilloried. Lock up and have fun!'
csl.photoId = 'IYhFK0bne7Y'

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

e = extensions.Extensions()
e.extensions.append(verification)
e.extensions.append(p)


def run(chaster_api: api.ChasterAPI):
    logger.warning('starting')

    if shared.resolve_shared_lock(chaster_api, csl, e, shared_lock_name) is None:
        logger.error('could not resolve the shared lock')
        return

    locked_users = shared.get_locked_users(chaster_api)

    logger.debug(f'searching {len(locked_users)} locked users')
    for l_lock in locked_users:
        if l_lock.sharedLock.name == shared_lock_name:
            if l_lock.displayRemainingTime:
                logger.debug(f'found and trapping {l_lock.user.username}')
                chaster_api.update_lock_settings(l_lock._id, False, True)
                eh = extensions.ExtensionsHandler()
                eh.load_defined(l_lock.extensions)
                chaster_api.place_user_into_pillory(l_lock._id, eh.pillories[0]._id, 'caught!',
                                                    int(datetime.timedelta(hours=2).total_seconds()))


if __name__ == "__main__":
    chaster_api = api.ChasterAPI(os.environ.get('CHASTER_BEARER_TOKEN'), user_agent='puphimbo/1.0')
    while True:
        try:
            run(chaster_api)
        except Exception as e:
            logger.error(f'error - {type(e).__name__} {e}')
        finally:
            time.sleep(datetime.timedelta(minutes=60).total_seconds())
