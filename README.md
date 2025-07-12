# 07/12/2025 

This project was built with the passion of assisting hobbyist developers in the creations of bot locks 
for Chaster. I am really proud of what the community has created with this project, of the many amazing
projects I am proud that this project helps power the amazing locks [Size Group Challenge Lock](https://chaster.app/explore/67d1be23dfcbbbb1d797ea56) 
and [miqu loves you](https://chaster.app/explore/6603dd811100b631ea6942e7) that have provided many entertaining and
frustrating hours for so many Chaster users.

At this point I am considering the future of this SDK. A manually written SDK is very
difficult to maintain. Ideally SDKs should be auto generated via the Chaster swagger file. This 
was the original path but unfortunately the swagger file is not complete enough to auto generate
a functional SDK with one click.

As to the future of this project, I am unsure. There are many directions to go in terms of 
maintainability, performance, and expansion of features. I do feel that the repo's original
goal of enabling hobbyists has not reached as many individuals as I would have hoped. 
[Enteofdeath's](https://chaster.app/user/Enteofdeath) Programmable Lock Extension has definitely 
done more enablement for hobbyists than this project has. 

Alternative projects such as [ChasterSharp](https://github.com/tensorc/ChasterSharp) does seem to
be deprecated as it's owner has stepped away from Chaster. This is one problem with maintaining an
SDK in that it needs a community to maintain the repository, to keep it living an alive as 
members come and go due to waning interests or fluctuating availability to work on the repository 
from different members.

I personally don't have much passion to keep this repo maintained, so for now the project in on
pause and very well likely will be deprecated. Thank you all so much to the community who has embraced
this work to lock up some many kinksters.

# Chaster Python SDK
`pip install --upgrade chaster-sdk`

```python
from chaster import api
import os
chaster_api = api.ChasterAPI(os.environ.get('CHASTER_BEARER_TOKEN'), user_agent='your_username/1.0')
```

See the [demos](https://github.com/PoofyEnigma/chaster-python-sdk/tree/main/demos) folder for examples of utilizing the SDK. 

[pypi project](https://pypi.org/project/chaster-sdk/)

# Contributing

You want to? Nice! Hmu on Discord, username PupHimbo

# Credits

Repository started by copying [this python boilerplate](https://github.com/AlexanderWillner/python-boilerplate)
