import datetime

import dateutil.parser


def update(obj):
    users = []

    for user in obj.users:
        users.append(User().update(user))

    return users


class User:
    def __init__(self):
        self._id: str = ''
        self.username: str = ''
        self.isPremium: str = ''
        self.description: str = ''
        self.location: str = ''
        self.gender: str = ''
        self.age: int = None
        self.role: str = ''
        self.isFindom: bool = False
        self.avatarUrl: str = ''
        self.online: bool = True
        self.lastSeen = None  # TODO type
        self.isAdmin: bool = False
        self.isModerator: bool = False
        self.metadata: Metadata = None
        self.fullLocation: str = ''
        self.discordId: str = None
        self.discordUsername: str = None
        self.isDisabled: bool = False
        self.isSuspended: bool = False
        self.features = [],
        self.joinedAt = None  # TODO type
        self.isNewMember: bool = True
        self.isSuspendedOrDisabled: bool = False

    def update(self, obj):
        self.__dict__ = obj.__dict__
        return self


class Metadata:
    def __init__(self):
        self.locktober2020Points: int = 0
        self.locktober2021Points: int = 0
        self.chastityMonth2022Points: int = 0
        self.locktober2022Points: int = 0
        self.locktober2023Points: int = 0


class LockCombination:
    def __init__(self):
        self._id: str = ''
        self.user: str = ''
        self.checkStatus: str = ''
        self.type: str = ''
        self.code: str = ''
        self.imageFullUrl: str = ''
        self.createdAt: datetime.datetime = None
        self.updatedAt: datetime.datetime = None
        self.enableManualCheck: bool = True

    def update(self, obj):
        self.__dict__ = obj.__dict__.copy()
        if obj.createdAt is not None:
            self.createdAt = dateutil.parser.isoparse(obj.createdAt)
        if obj.updatedAt is not None:
            self.updatedAt = dateutil.parser.isoparse(obj.updatedAt)
        return self
