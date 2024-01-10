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
| Messaging                         | ip      |           |            |        |
| Extensions - Temporary Opening    |         |           |            |        |
| Community Events                  |         |           |            |        |
| Partner Extensions                |         |           |            |        |
| Settings                          |         |           |            |        |
| Users                             |         |           |            |        |
| Keyholder                         |         |           |            |        |
| Reports                           |         |           |            |        |
| Partner Configurations            |         |           |            |        |
| Public Locks                      |         |           |            |        |
| Extensions - Verification Picture |         |           |            |        |

Stubbed - API call functions, DTOs defined<br>
Validated - tested with mocked chaster http response<br>
Integrated - Integration tests written and requests pre-validated for common 400 causing errors<br>
Mocked - API call has a mock equivalent allowing for local development of bots and functions are documented
Tutorial - A tutorial demonstrating usage of the function written and the SDK pypi docs published

### HTTP

- measure I/O
- connection pool
- cancellation tokens, do I need them?
- circuit breaker
- test and tweak retry
- change delay function into an internal rate limiter?
- query builder
- match headers with Chaster's headers
- implement w3c tracing protocol

### File/Class Organization

- Reduce number of files
- dumps and update in every obj
- update to array as a global function in the class it creates and array of
- more debug logging

### Testing

- needs two dedicated accounts for integration testing

### Authentication

- Credentials stack object
- Other authentication support

# Credits

Repository started with by using a https://github.com/AlexanderWillner/python-boilerplate
