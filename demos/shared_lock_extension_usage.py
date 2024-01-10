# Print some data about your shared locks
import os
import src.api as api
import logging

logging.basicConfig()
logger = logging.getLogger()
logger.setLevel(logging.INFO)

chaster_api = api.ChasterAPI(os.environ.get('CHASTER_BEARER_TOKEN'), user_agent='PythonSDKDeveloplmentDemo/1.0')

response, your_locks = chaster_api.get_shared_locks(status='')
print(response.headers)

data = {}
for lock in your_locks:
    for extension in lock.extensions:
        if extension.slug not in data:
            data[extension.slug] = 0
        data[extension.slug] += 1
print(data)
