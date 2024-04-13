import os
from chaster import api

chaster_api = api.ChasterAPI(os.environ.get(
    'CHASTER_BEARER_TOKEN'), user_agent='self_lock_creator/1.0')

developers_id = '65873830075fc043537113ee'

_, conv = chaster_api.create_conversation(
    '65873830075fc043537113ee', 'Hello from chaster python sdk example!')

chaster_api.send_message(conv._id, 'I hope you are having a wonderful day!')
