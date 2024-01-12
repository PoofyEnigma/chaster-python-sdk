# Chaster Python SDK

## Layer 1 Progress

### API Calls

| API Group                         | Stubbed | Validated | Integrated | Mocked | Tutorial |
|-----------------------------------|---------|-----------|------------|--------|----------|
| Shared Locks                      | done    | done      | done       |        |
| Locks                             | done    | done      |            |        |
| trigger_extension_actions         | done    | done      |            |        |
| Lock Creation                     | done    | done      |            |        |
| profile                           | done    | done      |            |        |
| Files                             | done    |           |            |        |
| Combinations                      | done    |           |            |        |
| Extensions                        | done    | done      |            |        |
| Session Offer                     | done    | done      |            |        |
| Messaging                         | done    | done      |            |        |
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
- Templatize Result object to avoid returning a
  tuple? https://stackoverflow.com/questions/6725868/generics-templates-in-python

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

## Layer 2 Progress

To obfuscate the API calls into function calls on the object itself. For example, rather than having to call
the trigger API to spin the wheel of fortune, instead the interface would be lock.spin_wheel_of_fortune().

| API Group                         | OOP Actions | 
|-----------------------------------|-------------|
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

# Credits

Repository started with by using a https://github.com/AlexanderWillner/python-boilerplate
