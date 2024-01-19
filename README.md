# Chaster Python SDK

`pip install --upgrade chaster-sdk`

```python
import os
import logging
from chaster import api

logging.basicConfig()
logger = logging.getLogger()
logger.setLevel(logging.INFO)

chaster_api = api.ChasterAPI(os.environ.get('CHASTER_BEARER_TOKEN'), user_agent='your_user_agent/1.0')
response, your_locks = chaster_api.get_shared_locks()
```

# Releases

| Release     | Conditionals                        | State |
|-------------|-------------------------------------|-------|
| v0.1.0.dev1 | Stubbed, Validated, Integrated      | done  |
| v0.1.0.a1   | Language, Documented                |       |
| v0.1.0.a2   | Mocked, Tutorial                    |       |
| v0.1.0      | 3 demos of a few hundred lines each |       |

# Layer 1 - API call wrappers and mocks<br>

| API Group                         | Stubbed | Validated | Integrated | Language | Documented | Mocked | Tutorial |
|-----------------------------------|---------|-----------|------------|----------|------------|--------|----------|
| Shared Locks                      | done    | done      | done       | done     | done       |        |          |
| Locks                             | done    | done      | done       | done     | done       |        |          |
| trigger_extension_actions         | done    | done      | done       | done     | done       |        |          |
| Lock Creation                     | done    | done      | done       | done     | done       |        |          |
| Profile                           | done    | done      | done       | done     | done       |        |          |
| Files                             | done    | done      | blocked    | done     | done       |        |          |
| Combinations                      | done    | done      | done       | done     | done       |        |          |
| Extensions                        | done    | done      | done       | done     | done       |        |          |
| Session Offer                     | done    | done      | done       | done     | done       |        |          |
| Messaging                         | done    | done      | done       | done     | done       |        |          |
| Extensions - Temporary Opening    | done    | done      | done       | done     | done       |        |          |
| Community Events                  | done    | done      | done       | done     | done       |        |          |
| Partner Extensions                |         |           |            |          |            |        |          |
| Settings                          | done    | done      | done       | done     | done       |        |          |
| Users                             | done    | done      | done       | done     | done       |        |          |
| Keyholder                         | done    | done      | done       | done     | done       |        |          |
| Reports                           | N/A     | N/A       | N/A        | N/A      | N/A        |        |          |
| Partner Configurations            |         |           |            |          |            |        |
| Public Locks                      | done    | done      | done       | done     | done       |        |          |
| Extensions - Verification Picture | done    | done      | done       | done     | done       |        |          |

Stubbed - API call functions, DTOs defined<br>
Validated - tested with mocked chaster http response<br>
Integrated - Integration tests written<br>
Language - Naming and interface refined and settled<br>
Documented - Functions are documented<br>
Mocked - API call has a mock equivalent allowing for local development of bots and functions are documented<br>
Tutorial - A tutorial demonstrating usage of the function written and the SDK pypi docs published<br>

## Layer 2 - OOP based calls and mocks

OOP Actions - To obfuscate the API calls into function calls on the object itself. For example, rather than having to
call
the trigger API to spin the wheel of fortune, instead the interface would be lock.spin_wheel_of_fortune().<br>
Tested - Test each function by mocking the chaster sdk object
Mocked - Similar spirit to mocking of layer 1 but instead simplify the interface to the data

### Backlog

- Extension Objects - DTO Tested and Validated<br>
- Extension Information API - C&C the extension information component vs. the extension info in the lock obj
- Probably remove bespoke objects as input to api functions, such as in triggers
- Redact bearer token from logs
- Remove delay and apply intelligent rate limiting reaction

## Research

- find a URL object hopefully with query building capabilities
- connection pool, thread safety of SDK
- test and tweak retry
- implement w3c tracing protocol
- measure I/O
- circuit breaker: https://github.com/danielfm/pybreaker
- cancellation tokens: https://github.com/pomponchik/cantok
- Enums vs. request validating vs. nothing
- https://github.com/pydantic/pydantic
- Templatize Result object to avoid returning a
  tuple? https://stackoverflow.com/questions/6725868/generics-templates-in-python
- need a wrapper for multipart/form-data requests
- async funcs
- Credentials stack object
- Other authentication support
- Chaster has a sequence of retry headers that may not be honored by the Retry library
- Retry library has been finicky to validate functionality. A bespoke method may be needed.
- abstract away success status codes to a wasSuccessful function?

# Ops

## Releasing

| Housekeeping File       | Flushed Out | Documented |
|-------------------------|-------------|------------|
| ./src/__init__.py       |             |            |
| ./src/setup.py          |             |            |
| ./tests/__init__.py     |             |            |
| ./.coveragerc           |             |            |
| ./.gitignore            |             |            |
| ./.travis.yml           |             |            |
| ./__init__.py           |             |            |
| ./LICENSE               |             |            |
| ./Makefile              |             |            |
| ./pyproject.toml        |             |            |
| ./README_BOILERPLACE.md |             |            |
| ./requirements.txt      |             |            |
| .pypirc                 |             |            |

Understood - Validated it has a place in the deployment process and is functioning correctly.<br>
Documented - The file is document in a process doc

# Contributing

You want to? Nice! Hmu on Discord, username PupHimbo

# Credits

Repository started with by using a https://github.com/AlexanderWillner/python-boilerplate