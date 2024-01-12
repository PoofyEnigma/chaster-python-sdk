# Chaster Python SDK

## Progress

### API Calls

| API Group                         | Stubbed | Validated | Integrated | Mocked | Tutorial |
|-----------------------------------|---------|-----------|------------|--------|----------|
| Shared Locks                      | done    | done      | done       |        |
| Locks                             | done    | done      |            |        |
| trigger_extension_actions         | done    |           |            |        |
| Lock Creation                     | done    |           |            |        |
| profile                           | done    |           |            |        |
| Files                             | done    |           |            |        |
| Combinations                      | done    |           |            |        |
| Extensions                        | done    |           |            |        |
| Session Offer                     | done    |           |            |        |
| Messaging                         | done    |           |            |        |
| Extensions - Temporary Opening    | done    |           |            |        |
| Community Events                  | done    |           |            |        |
| Partner Extensions                |         |           |            |        |
| Settings                          | done    |           |            |        |
| Users                             | done    |           |            |        |
| Keyholder                         | done    |           |            |        |
| Reports                           | done    | done      | done       | done   | done     |
| Partner Configurations            |         |           |            |        |
| Public Locks                      | done    |           |            |        |
| Extensions - Verification Picture | done    |           |            |        |

Stubbed - API call functions, DTOs defined<br>
Validated - tested with mocked chaster http response<br>
Integrated - Integration tests written<br>
Mocked - API call has a mock equivalent allowing for local development of bots and functions are documented
Tutorial - A tutorial demonstrating usage of the function written and the SDK pypi docs published

### HTTP

- async funcs?
- play with swagger codegen
- how to handle files?

### File/Class Organization

- more debug logging
- https://github.com/pydantic/pydantic
- Enums?
- Templatize Result object to avoid returning a tuple? https://stackoverflow.com/questions/6725868/generics-templates-in-python

### Testing

- needs two dedicated accounts for integration testing

### Authentication

- Credentials stack object
- Other authentication support
- Need to cycle your bearer token

### Backlog

- find a URL object hopefully with query building capabilities
- connection pool, thread safety of SDK
- test and tweak retry
- implement w3c tracing protocol
- measure I/O
- circuit breaker: https://github.com/danielfm/pybreaker
- cancellation tokens: https://github.com/pomponchik/cantok
- validate sdk against the

# Credits

Repository started with by using a https://github.com/AlexanderWillner/python-boilerplate
