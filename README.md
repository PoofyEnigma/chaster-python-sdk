# Chaster Python SDK
`pip install --upgrade chaster-sdk`

[pypi project](https://pypi.org/project/chaster-sdk/)

# Releases

| Release     | Conditionals                             | State |
|-------------|------------------------------------------|-------|
| v0.1.0.dev1 | Stubbed, Validated, Integrated           | done  |
| v0.1.0.a1   | Language, Documented                     | done  |
| v0.1.0.a2   | Backlog and TODOs work                   | done  |
| v0.1.0      | 95% coverage on unittest and integration | done  |

# Progress

| API Group                         | Stubbed | Validated | Integrated | Language | Documented | Tutorial |
|-----------------------------------|---------|-----------|------------|----------|------------|----------|
| Shared Locks                      | done    | done      | done       | done     | done       |          |
| Locks                             | done    | done      | done       | done     | done       |          |
| trigger_extension_actions         | done    | done      | done       | done     | done       |          |
| Lock Creation                     | done    | done      | done       | done     | done       |          |
| Profile                           | done    | done      | done       | done     | done       |          |
| Files                             | done    | done      | blocked    | done     | done       |          |
| Combinations                      | done    | done      | done       | done     | done       |          |
| Extensions                        | done    | done      | done       | done     | done       |          |
| Session Offer                     | done    | done      | done       | done     | done       |          |
| Messaging                         | done    | done      | done       | done     | done       |          |
| Extensions - Temporary Opening    | done    | done      | done       | done     | done       |          |
| Community Events                  | done    | done      | done       | done     | done       |          |
| Partner Extensions                |         |           |            |          |            |          |
| Settings                          | done    | done      | done       | done     | done       |          |
| Users                             | done    | done      | done       | done     | done       |          |
| Keyholder                         | done    | done      | done       | done     | done       |          |
| Reports                           | N/A     | N/A       | N/A        | N/A      | N/A        |          |
| Partner Configurations            |         |           |            |          |            |          |
| Public Locks                      | done    | done      | done       | done     | done       |          |
| Extensions - Verification Picture | done    | done      | done       | done     | done       |          |

### Backlog
- need more/better extension dump handling. May need to reformat extension handler. Need to handle unknown extensions
  better.
- util.safe_dump_parameter
- http://jsonpickle.github.io/
- datetime.timedelta().total_seconds returns a float
- pagination is how it is spelled

#### Rate limiting and Delaying

- Chaster has a sequence of retry headers that may not be honored by the Retry library. I should do more handling in
  this regard and provide functions for to interface with the current state of the retries
- Remove delay and apply intelligent rate limiting reaction

#### Authentication and Safe Logging

Would need to utilize a credentials stack object in order to simplify finding credentials should
the SDK open to support more types of authentication.
support clientId/clientSecret unsupported authentication

- abstract away success status codes to a wasSuccessful function?
    - I would leverage logging instead
    - Redact bearer token from logs

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

## Linting

`make lint | wc -l`

# Contributing

You want to? Nice! Hmu on Discord, username PupHimbo

# Credits

Repository started with by using a https://github.com/AlexanderWillner/python-boilerplate