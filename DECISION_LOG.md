# Templatize Result object to avoid returning a tuple
Opted for returning a tuple where applicable vs. wrapping inside a generic object.

Embracing Tuples seems more of a python style while Generics are a C++/Java/C# style of coding.
There is less referencing calling when using tuples.


**Tuple**
```python

class Thing:
    def __int__(self):
        self.a = 0
        self.b = 0
        self.c = 0
        
class Api:
    def __init__(self):
        pass
    
    def call1(self) -> tuple[response, Thing]:
        r = s.get('http://...')
        return r, Thing()
    
    def call2(self, data)-> response:
        return s.post('', data)

api = Api()
response, data = api.call1()
print(data.id)
print(data.maxLimitDate)
response = api.call2()
```

**Tuple**
```python
from typing import TypeVar, Generic, List

T = TypeVar('T')

class ApiResponse(Generic[T]):
    def __init__(self):
        self.data: T = None
        self.response = None

class Thing:
    def __int__(self):
        self.a = 0
        self.b = 0
        self.c = 0
        
class Api:
    def __init__(self):
        pass
    
    def call1(self) -> ApiResponse[Thing]:
        r = ApiResponse()
        r.data = 2
        r.response = s.get('http://...')
        return r
    
    def call2(self, data)-> ApiResponse:
        return s.post('', data)

api = Api()
response = api.call1()
print(response.data.a)
print(response.data.b)
print(response.data.c)
response = api.call2({})
```


# async
Should the api calls in ChasterAPI be async?

As of right now, I'm opting for no. Async can be useful but it requires explicitly embracing async in the code which also 
requires addition syntax to get something operational. It is assumed the average use case for this SDK will not be for 
high performance operations that need to have off over millisecond. Likely such as service will be rate limited by Chaster
very quickly. Admittedly more research into Chaster's rate limiting needs to occur. The addition syntax needs for async
will create developed more difficult for writing chaster bots. 

# Circuit Breaker
https://github.com/danielfm/pybreaker. Opted against.
https://stackoverflow.com/questions/15431044/can-i-set-max-retries-for-requests-request requests library already does this?

# Cancellation Tokens
https://github.com/pomponchik/cantok. Opted against. Would be needed if async and circuit breakers were adapted.

# connection pool, thread safety of SDK
I am not sure if these will be necessary. I would not recommend parallel execute to Chaster's servers until more information
is acquired.

# measuring I/O
Going back on to the usecase for the sdk as mainly a toolset for writting chaster bots, providing metric tooling will 
likely not be necessary. Should a user want to do so, we could allow for custom request hooks functions to be brought into
the ChasterAPI constructor that would allow the user to see to that use case.

# utilizing W3C Level 2 Tracing Protocol
It is not embraced by Chaster so would only be used locally and would be handy if the chaster bot happened to use another
service that did embrace the protocol. The official python implementation for it seems unnecessarily bulky at the time
of researching and would add many additional code block indents. Decided not to utilize it for now.

# Pydantic
https://github.com/pydantic/pydantic could be very useful and would maybe remove the internal dump/update calls used by
the API if it works. Chaster APIs responses have some inconsistent quirks that may make that library not as usefull compare
to the dump/update pattern.

# Request prevalidation, yes or no? Yes
To let the user of the SDK do as they please and let the server send back a 404 or should the SDK do its own checking
before sending the request? Opting for checking for known 404 errors on the SDK side.