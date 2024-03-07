import logging
import datetime

from chaster import api, extensions, lock


def publish_shared_lock(chaster_api: api.ChasterAPI, create_shared_lock: lock.CreateSharedLock,
                        ext: extensions.Extensions) -> lock.SharedLock | None:
    logger = logging.getLogger()
    logger.debug(f'creating a new shared lock {create_shared_lock.name}')
    resp, shared_lock_id = chaster_api.create_shared_lock(create_shared_lock)
    if resp.status_code != 201:
        logger.error(f'could not create new shared lock for {create_shared_lock.name}')
        return None

    resp = chaster_api.put_shared_lock_extensions(shared_lock_id, ext)
    if resp.status_code != 200:
        logger.error(f'could not edit the extensions of the new lock for {create_shared_lock.name}')
        resp = chaster_api.archive_shared_lock(shared_lock_id)
        if resp.status_code != 201:
            logger.error(f'failed to archive newly created but invalid shared lock for {create_shared_lock.name}')
        return None

    resp, data = chaster_api.get_shared_lock_details(shared_lock_id)
    if resp.status_code != 200:
        logger.warning(f'failed to get the shared lock after creating it for {create_shared_lock.name}')
        return None
    return data


def resolve_shared_lock(chaster_api: api.ChasterAPI, create_shared_lock: lock.CreateSharedLock,
                        ext: extensions.Extensions, lock_name: str) -> lock.SharedLock | None:
    logger = logging.getLogger()
    resp, shared_locks = chaster_api.get_user_shared_locks()
    if resp.status_code != 200:
        logger.error('could not get shared locks')
        return None
    logger.debug(f'Finding the existing shared lock from {len(shared_locks)} shared locks')
    for shared_lock in shared_locks:
        if shared_lock.name == lock_name:
            trap_shared_lock = shared_lock
            break
    else:
        trap_shared_lock = publish_shared_lock(chaster_api, create_shared_lock, ext)

    if trap_shared_lock is None:
        logger.warning('could not resolve the shared lock')
        return trap_shared_lock

    if trap_shared_lock.lastSavedAt + datetime.timedelta(days=7) <= datetime.datetime.now().astimezone():
        logger.debug(f'shared lock {create_shared_lock.name} is out of date. Republishing.')
        resp = chaster_api.archive_shared_lock(trap_shared_lock._id)
        if resp.status_code != 201:
            logger.error(
                f'could not archive shared lock {trap_shared_lock.name} due to {resp.status_code} - {resp.text}')
            trap_shared_lock = None
        else:
            trap_shared_lock = publish_shared_lock(chaster_api, create_shared_lock, ext)

    return trap_shared_lock


def get_locked_users(chaster_api: api.ChasterAPI):
    logger = logging.getLogger()
    logger.debug(f'getting first page of locked users')
    resp, locked_users_page = chaster_api.find_locked_users()
    locked_users = locked_users_page.locks

    for page in range(1, locked_users_page.pages):
        logger.debug(f'getting page {page} of locked users')
        resp, locked_users_page = chaster_api.find_locked_users(page=page)
        locked_users.extend(locked_users_page.locks)

    return locked_users
