"""
This script will send a pleasant message from the individual running the script to
one of the SDK's service accounts.
"""

import os
from chaster import api

chaster_api = api.ChasterAPI(os.environ.get('CHASTER_BEARER_TOKEN'), user_agent='self_lock_creator/1.0')

chaster_sdk_service_account_id = '65873830075fc043537113ee'

_, conv = chaster_api.create_conversation(chaster_sdk_service_account_id, 'Hello from chaster python sdk example!')

chaster_api.send_message(conv._id, 'I hope you are having a wonderful day!')