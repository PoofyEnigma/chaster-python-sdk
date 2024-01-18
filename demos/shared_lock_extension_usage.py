# Print some data about your shared locks
import os
import logging
from chaster import api

logging.basicConfig()
logger = logging.getLogger()
logger.setLevel(logging.INFO)

chaster_api = api.ChasterAPI(os.environ.get('CHASTER_BEARER_TOKEN'), user_agent='PythonSDKDeveloplment/1.0')
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
