import datetime

import dateutil.parser

from . import extensions
from . import shared_lock
from . import user
from dateutil.parser import isoparse


def update(obj):
    locks = []
    if type(obj) is not list:
        for lock in obj.locks:
            locks.append(Lock().update(lock))
    else:
        for lock in obj:
            locks.append(Lock().update(lock))
    return locks


class Lock:
    def __init__(self):
        self._id: str = ''
        self.startDate: str = ''
        self.endDate: str = ''
        self.minDate: str = ''
        self.maxDate: str = ''
        self.maxLimitDate: datetime.datetime = None
        self.displayRemainingTime: bool = True
        self.limitLockTime: bool = False
        self.status: str = ''
        self.combination: str = ''
        self.shared_lock: shared_lock.SharedLock = shared_lock.SharedLock()
        self.createdAt: str = ''
        self.updatedAt: str = ''
        self.unlockedAt: datetime.datetime = None
        self.archivedAt: datetime.datetime = None
        self.frozenAt: str = ''
        self.keyholderArchivedAt: datetime.datetime = None
        self.totalDuration: int = 235422887
        self.allowSessionOffer: bool = False
        self.isTestLock: bool = False
        self.offerToken: str = ''
        self.hideTimeLogs: bool = True
        self.trusted: bool = True
        self.user = user.User()
        self.keyholder = user.User()
        self.isAllowedToViewTime: bool = True
        self.canBeUnlocked: bool = False
        self.canBeUnlockedByMaxLimitDate: bool = False
        self.isFrozen: bool = True
        self.extensions = []
        self.role: str = ''
        self.title: str = ''
        self.lastVerificationPicture = LastVerificationPicture()
        self.availableHomeActions: list[AvailableHomeAction] = []
        self.reasonsPreventingUnlocking = []
        self.extensionsAllowUnlocking: bool = True

    # TODO: Figure this out. Would the extension handler have a reference to this
    # TODO cont.: object and be allowed to edit this object's extension array?
    def get_extension_handler(self):
        return extensions.ExtensionsHandler().load(self.extensions)

    def dump(self):
        obj = self.__dict__
        obj['shared_lock'] = self.shared_lock.__dict__
        obj['maxLimitDate'] = self.maxLimitDate.isoformat()
        obj['unlockedAt'] = self.unlockedAt.isoformat()
        obj['archivedAt'] = self.archivedAt.isoformat()
        obj['keyholderArchivedAt'] = self.keyholderArchivedAt.isoformat()

    def update(self, obj):
        self.__dict__.update(obj.__dict__)
        self.extensions = extensions.update(obj)
        self.availableHomeActions = update_available_home_actions(obj)
        if obj.maxLimitDate is not None:
            self.maxLimitDate = isoparse(obj.maxLimitDate)
        if obj.unlockedAt is not None:
            self.unlockedAt = isoparse(obj.unlockedAt)
        if obj.archivedAt is not None:
            self.archivedAt = isoparse(obj.archivedAt)
        if obj.keyholderArchivedAt is not None:
            self.keyholderArchivedAt = isoparse(obj.keyholderArchivedAt)
        return self


class LastVerificationPicture:
    def __init__(self):
        self.verificationCode: int = 0
        self.imageFile: str = ''
        self.peerVerificationId: str = ''
        self.imageKey: str = ''
        self.submittedAt: str = ''


class AvailableHomeAction:
    def __init__(self):
        self.slug: str = ''
        self.title: str = ''
        self.description: str = ''
        self.icon: str = ''
        self.extensionPartyId: str = ''
        self.badge = None

    def update(self, obj):
        self.__dict__.update(obj.__dict__)
        return self


def update_available_home_actions(obj):
    available_home_actions = []
    if 'availableHomeActions' in obj.__dict__:
        for availableHomeAction in obj.availableHomeActions:
            available_home_actions.append(AvailableHomeAction().update(availableHomeAction))
    return available_home_actions


class LockedUsers:
    def __init__(self):
        self.pages: int = 0
        self.total: int = 0
        self.locks: list[Lock] = []

    def update(self, obj):
        self.__dict__.update(obj.__dict__)
        self.locks = update(obj)
        return self


"""
{
  "results": [

  ],
}
"""


class ActionLog:
    """

        {


    }
    """

    def __init__(self):
        self._id: str = ''
        self.type: str = ''
        self.payload: dict = {}
        self.lock: str = ''
        self.role = ''
        self.extension: str = ''
        self.title: str = ''
        self.description: str = ''
        self.color: str = ''
        self.createdAt: datetime.datetime = None
        self.icon: str = ''
        self.prefix: str = ''
        self.user: user.User = None

    def update(self, obj):
        self.__dict__ = obj.__dict__.copy()
        if obj.createdAt is not None:
            self.createdAt = dateutil.parser.isoparse(obj.createdAt)
        self.user = user.User().update(obj.user)
        return self


class PageinatedLockHistory:
    def __init__(self):
        self.count: int = 0
        self.hasMore: bool = False
        self.results: list[ActionLog] = []

    def update(self, obj):
        self.__dict__ = obj.__dict__.copy()
        self.results = []
        for result in obj.results:
            self.results.append(ActionLog().update(result))
        return self


class ExtensionInformation:
    def __init__(self):
        self.lock: Lock = None
        self.extension = None

    def update(self, obj):
        self.lock = Lock().update(obj.lock)
        eh = extensions.ExtensionsHandler()
        eh.add(obj.extension)
        self.extension = eh.dump()[0]
        return self


class LockId:
    def __init__(self):
        self.lockId: str = ''

    def update(self, obj):
        self.__dict__ = obj.__dict__
        return self


class LockInfo:
    def __init__(self):
        self.password: str = ''
        self.combinationId: str = ''
        self.isTestLock: bool = False

    def dump(self):
        return self.__dict__.copy()
