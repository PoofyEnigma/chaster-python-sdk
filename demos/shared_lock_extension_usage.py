# Print some data about your shared locks
import os
import logging
from chaster import api

logging.basicConfig()
logger = logging.getLogger()
logger.setLevel(logging.INFO)

chaster_api = api.ChasterAPI(os.environ.get('CHASTER_BEARER_TOKEN'), user_agent='your_user_agent/1.0')

response, your_shared_locks = chaster_api.get_user_shared_locks()


data = {}
for shared_lock in your_shared_locks:
    for extension in shared_lock.extensions:
        if extension.slug not in data:
            data[extension.slug] = 0
        data[extension.slug] += 1
print(data)
