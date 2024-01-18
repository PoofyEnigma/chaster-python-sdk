# Chaster Python SDK

## Layer 1 Progress

v0.1.0

### API Calls

| API Group                         | Stubbed | Validated | Integrated | Mocked | Tutorial |
|-----------------------------------|---------|-----------|------------|--------|----------|
| Shared Locks                      | done    | done      | done       |        |
| Locks                             | done    | done      | done       |        |
| trigger_extension_actions         | done    | done      |            |        |
| Lock Creation                     | done    | done      | done       |        |
| Profile                           | done    | done      | done       |        |
| Files                             | done    | done      | ip         |        |
| Combinations                      | done    | done      | done       |        |
| Extensions                        | done    | done      | done       |        |
| Session Offer                     | done    | done      | done       |        |
| Messaging                         | done    | done      |            |        |
| Extensions - Temporary Opening    | done    | done      |            |        |
| Community Events                  | done    | done      |            |        |
| Partner Extensions                |         |           |            |        |
| Settings                          | done    | done      |            |        |
| Users                             | done    | done      |            |        |
| Keyholder                         | done    | done      | ip         |        |
| Reports                           | N/A     | N/A       | N/A        | N/A    | N/A      |
| Partner Configurations            |         |           |            |        |
| Public Locks                      | done    | done      |            |        |
| Extensions - Verification Picture | done    | done      |            |        |

Stubbed - API call functions, DTOs defined<br>
Validated - tested with mocked chaster http response<br>
Integrated - Integration tests written and naming settled<br>
Mocked - API call has a mock equivalent allowing for local development of bots and functions are documented<br>
Tutorial - A tutorial demonstrating usage of the function written and the SDK pypi docs published<br>
Extension Objects - DTO Tested and Validated<br>
Extension Information API - C&C the extension information component vs. the extension info in the lock obj

## Layer 2 Progress

v0.2.0<br>

| API Group                         | OOP Actions | Tested | Mocked |
|-----------------------------------|-------------|--------|--------|
| Shared Locks                      |             |
| Locks                             |             |
| trigger_extension_actions         |             |
| Lock Creation                     |             |
| profile                           |             |
| Files                             |             |
| Combinations                      |             |
| Extensions                        |             |
| Session Offer                     |             |
| Messaging                         |             |
| Extensions - Temporary Opening    |             |
| Community Events                  |             |
| Partner Extensions                |             |
| Settings                          |             |
| Users                             |             |
| Keyholder                         |             |
| Reports                           |             |
| Partner Configurations            |             |
| Public Locks                      |             |
| Extensions - Verification Picture |             |

OOP Actions - To obfuscate the API calls into function calls on the object itself. For example, rather than having to
call
the trigger API to spin the wheel of fortune, instead the interface would be lock.spin_wheel_of_fortune().<br>
Tested - Test each function by mocking the chaster sdk object
Mocked - Similar spirit to mocking of layer 1 but instead simplify the interface to the data

### Releasing

| Housekeeping File       | Flushed Out | Documented |
|-------------------------|-------------|------------|
| ./src/__init__.py       |
| ./src/setup.py          |
| ./tests/__init__.py     |
| ./.coveragerc           |
| ./.gitignore            |
| ./.travis.yml           |
| ./__init__.py           |
| ./LICENSE               |
| ./Makefile              |
| ./pyproject.toml        |
| ./README_BOILERPLACE.md |
| ./requirements.txt      |

Understood - Validated it has a place in the deployment process and is functioning correctly.<br>
Documented - The file is document in a process doc

### Backlog

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

# Contributing

You want to? Nice! Hmu on Discord, username PupHimbo

# Credits

Repository started with by using a https://github.com/AlexanderWillner/python-boilerplate

