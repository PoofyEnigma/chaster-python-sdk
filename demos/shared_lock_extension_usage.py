# Print some data about your shared locks
import os
from datetime import datetime

import src.api as api
import logging

logging.basicConfig()
logger = logging.getLogger()
logger.setLevel(logging.INFO)

chaster_api = api.ChasterAPI(os.environ.get('CHASTER_BEARER_TOKEN'), user_agent='PythonSDKDeveloplment/1.0')

chaster_api_lockee = api.ChasterAPI(os.environ.get('CHASTER_BEARER_TOKEN_II'), user_agent='PythonSDKDeveloplment/1.0')
response, locked_users = chaster_api.post_keyholder_locks_search()
lock_after = locked_users.locks[0]
_ = chaster_api.unlock(lock_after._id)
_ = chaster_api_lockee.archive_lock(lock_after._id)
exit()

response, your_locks = chaster_api.get_shared_locks(status='')
print(response.status_code)
print(your_locks)

data = {}
for lock in your_locks:
    for extension in lock.extensions:
        if extension.slug not in data:
            data[extension.slug] = 0
        data[extension.slug] += 1
print(data)
