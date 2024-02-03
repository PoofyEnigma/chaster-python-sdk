import os
from pprint import pprint

from chaster import api

chaster_api = api.ChasterAPI(os.environ.get('CHASTER_BEARER_TOKEN'), user_agent='check_rate_limit_behavior_for_sdk/1.0',
                             delay=0)

_, locks = chaster_api.get_user_locks()
lock_id = locks[0]._id

data = {}
data['x-ratelimit-limit'] = []
data['x-ratelimit-remaining'] = []
data['x-ratelimit-reset'] = []
data['retry-after'] = []

for i in range(0, 10):
    response = chaster_api.update_lock_duration(lock_id, 1)
    data['x-ratelimit-limit'].append(response.headers['x-ratelimit-limit'])
    data['x-ratelimit-remaining'] .append(response.headers['x-ratelimit-remaining'])
    data['x-ratelimit-reset'].append(response.headers['x-ratelimit-reset'])
    data['retry-after'].append(response.headers['retry-after'])

pprint(data)
