# Chaster Python SDK

## Progress

### API Calls

| API Group                         | Stubbed | Validated | Integrated | Mocked | Tutorial |
|-----------------------------------|---------|-----------|------------|--------|----------|
| Shared Locks                      | done    |           | done       |        |
| Locks                             | done    |           |            |        |
| trigger_extension_actions         | done    |           |            |        |
| Lock Creation                     | done    |           |            |        |
| profile                           | done    |           |            |        |
| Files                             |         |           |            |        |
| Combinations                      |         |           |            |        |
| Extensions                        | done    |           |            |        |
| Session Offer                     | done    |           |            |        |
| Messaging                         | done    |           |            |        |
| Extensions - Temporary Opening    |         |           |            |        |
| Community Events                  |         |           |            |        |
| Partner Extensions                |         |           |            |        |
| Settings                          |         |           |            |        |
| Users                             |         |           |            |        |
| Keyholder                         | ip      |           |            |        |
| Reports                           |         |           |            |        |
| Partner Configurations            |         |           |            |        |
| Public Locks                      |         |           |            |        |
| Extensions - Verification Picture |         |           |            |        |

Stubbed - API call functions, DTOs defined<br>
Validated - tested with mocked chaster http response<br>
Integrated - Integration tests written and requests pre-validated for common 400 causing errors<br>
Mocked - API call has a mock equivalent allowing for local development of bots and functions are documented
Tutorial - A tutorial demonstrating usage of the function written and the SDK pypi docs published

### File/Class Organization

- update to array as a global function in the class it creates and array of
- more debug logging
- https://github.com/pydantic/pydantic

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

# Credits

Repository started with by using a https://github.com/AlexanderWillner/python-boilerplate
