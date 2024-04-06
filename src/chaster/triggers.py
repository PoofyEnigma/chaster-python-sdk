import datetime
from . import extensions, util
import dateutil.parser


def generic_trigger(action: str):
    return {
        'action': action,
        'payload': {}
    }


# share links
# vote
# request {"action":"vote","payload":{"action":"add","sessionId":"z3lyGWVABT6VYmXs"}}
# response {"duration":3600}
# request {"action":"vote","payload":{"action":"random","sessionId":"7VWL6WZivfwmbbrX"}}
# response {"duration":0}
# request {"action":"vote","payload":{"action":"remove","sessionId":"e6j0VGqWmOPi2bGs"}}
# response {"duration":-86400}
# get link to vote
# request {"action":"getLink","payload":{}}
# response {"link":"https://chaster.app/sessions/z3lyGWVABT6VYmXs"}
# get info
# request {"action":"getInfo","payload":{}}
# response {"lockId":"659ee2ce9e46da74718e5f2d","extensionId":"659ee2ce9e46da74718e5f34","votes":1,"minVotes":0,"canVote":false}

class ShareLinkInfoResponse:
    def __init__(self):
        self.lockId: str = ''
        self.extensionId: str = ''
        self.votes: int = 0
        self.minVotes: int = 0
        self.canVote: bool = False

    def update(self, obj):
        self.__dict__ = obj.__dict__.copy()
        return self

    def dump(self):
        return self.__dict__.copy()


# pillory
# put into pillory
# request {"action":"submit","payload":{"duration":900,"reason":"puppy was bad"}}
# get current pillory update
# request {"action":"getStatus","payload":{}}
# response {"votes":[{"_id":"659ee3029e46da74718e83b8","nbVotes":0,"totalDurationAdded":0,"voteEndsAt":"2024-01-10T18:48:38.396Z","canVote":true,"reason":"puppy was bad","createdAt":"2024-01-10T18:33:38.397Z"}]}

class Vote:
    def __init__(self):
        self._id: str = ''
        self.nbVotes: int = 0
        self.totalDurationAdded: int = 0
        self.voteEndsAt: int = 0
        self.canVote: bool = True
        self.reason: str = ''
        self.createdAt: datetime.datetime = None

    def update(self, obj):
        self.__dict__ = obj.__dict__.copy()
        if obj.createdAt is not None:
            self.createdAt = dateutil.parser.isoparse(obj.createdAt)
        return self

    def dump(self):
        obj = self.__dict__.copy()
        util.safe_dump_time(self, 'createdAt', obj)
        return obj

    @staticmethod
    def generate_array(obj_list):
        return [Vote().update(vote) for vote in obj_list]

    @staticmethod
    def dump_array(obj_list):
        return [vote.dump() for vote in obj_list]


class PilloryVotes:
    def __init__(self):
        self.votes: list[Vote] = []

    def update(self, obj):
        self.votes = Vote.generate_array(obj.votes)
        return self

    def dump(self):
        obj = self.__dict__.copy()
        obj['votes'] = Vote.dump_array(self.votes)
        return obj


# hygience opening
# unlock
# request {"action":"submit","payload":{}}
# request {"action":"keyholderOpen","payload":{}}


# dice
# to roll the dice
# request {"action":"submit","payload":{}}
# response {"adminDice":5,"playerDice":4,"duration":3600}
class DiceRollResult:
    def __init__(self):
        self.adminDice: int = 0
        self.playerDice: int = 0
        self.duration: int = 0

    def update(self, obj):
        self.__dict__ = obj.__dict__.copy()
        return self

    def dump(self):
        return self.__dict__.copy()


# wheel of fortune
# to spin the wheel of fortune
# request {"action":"submit","payload":{}}
# response {"index":0,"action":{"segment":{"type":"add-time","text":"","duration":3600}},"text":"Added 1 hour"}


class WheelOfFortuneAction:
    def __init__(self):
        self.segment: extensions.WheelOfFortuneSegment = None

    def update(self, obj):
        self.segment = extensions.WheelOfFortuneSegment().update(obj.segment)
        return self

    def dump(self):
        obj = self.__dict__.copy()
        obj['segment'] = self.segment.dump()
        return obj


class WheelOfFortuneResult:
    def __init__(self):
        self.index: int = 0
        self.action: WheelOfFortuneAction = None
        self.text: str = ''

    def update(self, obj):
        self.__dict__ = obj.__dict__.copy()
        self.action = WheelOfFortuneAction().update(obj.action)
        return self

    def dump(self):
        obj = self.__dict__.copy()
        obj['action'] = self.action.dump()
        return obj


# tasks
# get a random task
# {"action":"submit","payload":{"requestVote":false}}
# no response
# let other users choose
# request {"action":"submit","payload":{"requestVote":true,"voteDuration":3600}} <- A min of one hour?
# complete task
# {"action":"completeTask","payload":{"isCompleted":true}}
# fail task
# {"action":"completeTask","payload":{"isCompleted":false}}


# verification photo
# signal to submit new verification
# request {"action":"createVerificationRequest","payload":{}}


# Guess the Timer
# request {"action":"submit","payload":{}}
# response {"canBeUnlocked":false}

class GuessTheTimerResponse:
    def __init__(self):
        self.canBeUnlocked: bool = False

    def update(self, obj):
        self.__dict__ = obj.__dict__.copy()
        return self

    def dump(self):
        return self.__dict__.copy()
