# Print some data about your shared locks
import os
from datetime import datetime

import src.api as api
import logging

logging.basicConfig()
logger = logging.getLogger()
logger.setLevel(logging.INFO)


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
