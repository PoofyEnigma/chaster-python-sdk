import datetime

import dateutil.parser

from . import extensions, user
from dateutil.parser import isoparse


class CreateLock:
    def __init__(self):
        self.minDuration: int = 0
        self.maxDuration: int = 0
        self.maxLimitDuration: int = 0
        self.displayRemainingTime: bool = True
        self.limitLockTime: bool = True
        self.combinationId: str = ''
        self.extensions = []
        self.allowSessionOffer: bool = True
        self.isTestLock: bool = False
        self.hideTimeLogs: bool = True

    def dump(self):
        return self.__dict__.copy()


class Lock:
    # TODO: Dates need to be datetime objects
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
        self.sharedLock: SharedLock = SharedLock()
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
        self.trusted: bool = False
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
        self.deletedAt: datetime.datetime = None

    # TODO: Figure this out. Would the extension handler have a reference to this
    # TODO cont.: object and be allowed to edit this object's extension array?
    def get_extension_handler(self):
        return extensions.ExtensionsHandler().load(self.extensions)

    def dump(self):
        obj = self.__dict__
        obj['shared_lock'] = self.sharedLock.__dict__
        if self.maxLimitDate is not None:
            obj['maxLimitDate'] = self.maxLimitDate.isoformat()
        if self.unlockedAt is not None:
            obj['unlockedAt'] = self.unlockedAt.isoformat()
        if self.archivedAt is not None:
            obj['archivedAt'] = self.archivedAt.isoformat()
        if self.keyholderArchivedAt is not None:
            obj['keyholderArchivedAt'] = self.keyholderArchivedAt.isoformat()

    def update(self, obj):
        self.__dict__ = obj.__dict__.copy()
        if 'extensions' in obj.__dict__:
            self.extensions = extensions.Extension.generate_array(obj.extensions)
        if 'availableHomeActions' in obj.__dict__:
            self.availableHomeActions = AvailableHomeAction.generate_array(obj.availableHomeActions)
        if 'maxLimitDate' in obj.__dict__ and obj.maxLimitDate is not None:
            self.maxLimitDate = isoparse(obj.maxLimitDate)
        if 'unlockedAt' in obj.__dict__ and obj.unlockedAt is not None:
            self.unlockedAt = isoparse(obj.unlockedAt)
        if 'archivedAt' in obj.__dict__ and obj.archivedAt is not None:
            self.archivedAt = isoparse(obj.archivedAt)
        if 'keyholderArchivedAt' in obj.__dict__ and obj.keyholderArchivedAt is not None:
            self.keyholderArchivedAt = isoparse(obj.keyholderArchivedAt)
        if 'deletedAt' in obj.__dict__ and obj.deletedAt is not None:
            self.keyholderArchivedAt = isoparse(obj.deletedAt)
        return self

    @staticmethod
    def generate_array(obj_list):
        locks = []
        for lock in obj_list:
            locks.append(Lock().update(lock))
        return locks


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

    @staticmethod
    def generate_array(obj_list):
        available_home_actions = []
        for availableHomeAction in obj_list:
            available_home_actions.append(AvailableHomeAction().update(availableHomeAction))
        return available_home_actions


class LockedUsers:
    def __init__(self):
        self.pages: int = 0
        self.total: int = 0
        self.locks: list[Lock] = []

    def update(self, obj):
        self.__dict__.update(obj.__dict__)
        self.locks = Lock.generate_array(obj.locks)
        return self


class ActionLog:
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

    @staticmethod
    def generate_array(obj_list):
        action_logs = []
        for item in obj_list:
            action_logs.append(ActionLog().update(item))
        return action_logs


class PageinatedLockHistory:
    def __init__(self):
        self.count: int = 0
        self.hasMore: bool = False
        self.results: list[ActionLog] = []

    def update(self, obj):
        self.__dict__ = obj.__dict__.copy()
        self.results = ActionLog.generate_array(obj.results)
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
        self.password: str = None
        self.combinationId: str = ''
        self.isTestLock: bool = False

    def dump(self):
        return self.__dict__.copy()


class UnsplashPhoto:
    def __init__(self):
        self.id: str = ''
        self.name: str = ''
        self.url: str = ''
        self.username: str = ''


class IdResponse:
    def __init__(self):
        self.id: str = ''

    def update(self, obj):
        self.__dict__ = obj.__dict__
        return self


class CreateSharedLock:
    def __init__(self):
        self.minDuration: int = 3600
        self.maxDuration: int = 7200
        self.maxLimitDuration: int = None
        self.minDate: datetime = None
        self.maxDate: datetime = None
        self.maxLimitDate: datetime = None
        self.displayRemainingTime: bool = True
        self.limitLockTime: bool = False
        self.maxLockedUsers: int = None
        self.isPublic: bool = True
        self.password = None
        self.requireContact: bool = False
        self.name: str = ''
        self.description: str = ''
        self.photoId: str = ''
        self.hideTimeLogs: bool = False
        self.isFindom: bool = False

    def dump(self):
        dictionary = self.__dict__.copy()
        if self.maxDate is not None:
            dictionary['maxDate'] = self.maxDate.isoformat()
        if self.minDate is not None:
            dictionary['minDate'] = self.minDate.isoformat()
        if self.maxLimitDate is not None:
            dictionary['maxLimitDate'] = self.maxLimitDate.isoformat()
        return dictionary

    def validate(self):
        # TODO: This may be an intended feature to remember the max limit date when you set the limit lock time to false
        if (self.maxLimitDuration is not None or self.maxLimitDate is not None) and not self.limitLockTime:
            raise ValueError('a max limit on the lock is set, limitLockTime should be true')
        if self.limitLockTime:
            if self.maxLimitDuration is not None and self.maxDuration > self.maxLimitDuration:
                raise ValueError('the max duration should not be greater than the limit duration')
            if self.maxLimitDate is not None and self.maxDate > self.maxLimitDate:
                raise ValueError('the max date should not be greater than the limit date')
        if self.minDuration > self.maxDuration:
            raise ValueError('the min duration should not be larger than the maximum duration')
        if self.maxDate is None and self.minDate is not None:
            raise ValueError('if min date is set max date must also be set')
        if self.maxDate is not None and self.minDate is None:
            raise ValueError('if max date is set then min date must also be set')
        if self.maxDate is not None and self.minDate is not None:
            if self.maxDate < self.minDate:
                raise ValueError('min date should not be larger than the max date')

    def update(self, obj):
        self.__dict__ = obj.__dict__
        if obj.maxDate is not None:
            self.maxDate = isoparse(obj.maxDate)
        if obj.minDate is not None:
            self.minDate = isoparse(obj.minDate)
        if obj.maxLimitDate is not None:
            self.maxLimitDate = isoparse(obj.maxLimitDate)
        return self


class SharedLock:
    def __init__(self):
        self._id: str = ''
        self.minDuration: int = 86400
        self.maxDuration: int = 90000
        self.maxLimitDuration: int = None
        self.minDate: datetime = None
        self.maxDate: datetime = None
        self.maxLimitDate: datetime = None
        self.displayRemainingTime: bool = True
        self.limitLockTime: bool = False
        self.maxLockedUsers: int = None
        self.isPublic: bool = True
        self.requireContact: bool = False
        self.name: str = ''
        self.password: str = None
        self.description: str = ''
        self.unsplashPhoto: UnsplashPhoto = UnsplashPhoto()
        self.hideTimeLogs: bool = False
        self.lastSavedAt: datetime = None
        self.requirePassword: bool = False
        self.user: user.User = user.User()
        self.durationMode: str = ''
        self.isFindom: bool = False
        self.calculatedMaxLimitDuration: int = None
        self.extensions = []

    def update(self, obj):
        self.__dict__ = obj.__dict__
        if 'extensions' in obj.__dict__:
            self.extensions = extensions.Extension.generate_array(obj.extensions)
        if obj.maxDate is not None:
            self.maxDate = isoparse(obj.maxDate)
        if obj.minDate is not None:
            self.minDate = isoparse(obj.minDate)
        if obj.maxLimitDate is not None:
            self.maxLimitDate = isoparse(obj.maxLimitDate)
        if obj.lastSavedAt is not None:
            self.lastSavedAt = isoparse(obj.lastSavedAt)
        return self

    @staticmethod
    def generate_array(obj_list):
        shared_locks = []
        for entry in obj_list:
            shared_locks.append(SharedLock().update(entry))
        return shared_locks


class PageinatedSharedLockList:
    def __init__(self):
        self.lastId: str = ''
        self.hasMore: bool = True
        self.count: int = 0
        self.results: list[SharedLock] = []

    def update(self, obj):
        self.__dict__ = obj.__dict__.copy()
        self.results = SharedLock.generate_array(obj.results)
        if 'lastId' not in obj.__dict__ and len(self.results) > 0:
            self.lastId = self.results[-1]._id
        return self


class JoinRules:
    def __init__(self):
        self.canBeJoined: bool = True
        self.containsPremiumExtension: bool = True
        self.exceedsExtensionLimit: bool = True
        self.oneOfExtensionsDisabled: bool = True


class PublicSharedLockInfo:
    def __init__(self):
        self.joinRules: JoinRules = None
        self.locks: list[Lock] = []
        self._id: str = ''
        self.minDuration: int = 86400
        self.maxDuration: int = 90000
        self.maxLimitDuration: int = None
        self.minDate: datetime = None
        self.maxDate: datetime = None
        self.maxLimitDate: datetime = None
        self.displayRemainingTime: bool = True
        self.limitLockTime: bool = False
        self.maxLockedUsers: int = None
        self.isPublic: bool = True
        self.requireContact: bool = False
        self.name: str = ''
        self.description: str = ''
        self.unsplashPhoto: UnsplashPhoto = UnsplashPhoto()
        self.hideTimeLogs: bool = False
        self.lastSavedAt: datetime = None
        self.requirePassword: bool = False
        self.user: user.User = user.User()
        self.durationMode: str = ''
        self.isFindom: bool = False
        self.calculatedMaxLimitDuration: int = None
        self.extensions = []
        self.createdAt: datetime.datetime = None
        self.updatedAt: datetime.datetime = None
        self.unlockedAt: datetime.datetime = None
        self.deletedAt: datetime.datetime = None

    def update(self, obj):
        self.__dict__ = obj.__dict__
        self.extensions = extensions.Extension.generate_array(obj.extensions)
        # TODO: Is locks actually in the return obj?
        if 'locks' in obj.__dict__:
            self.locks = Lock.generate_array(obj.locks)
        if obj.maxDate is not None:
            self.maxDate = isoparse(obj.maxDate)
        if obj.minDate is not None:
            self.minDate = isoparse(obj.minDate)
        if obj.maxLimitDate is not None:
            self.maxLimitDate = isoparse(obj.maxLimitDate)
        if obj.lastSavedAt is not None:
            self.lastSavedAt = isoparse(obj.lastSavedAt)
        if obj.maxLimitDate is not None:
            self.maxLimitDate = isoparse(obj.maxLimitDate)
        if 'unlockedAt' in obj.__dict__ and obj.unlockedAt is not None:
            self.unlockedAt = isoparse(obj.unlockedAt)
        if 'deletedAt' in obj.__dict__ and obj.deletedAt is not None:
            self.deletedAt = isoparse(obj.deletedAt)
        if 'createdAt' in obj.__dict__ and obj.createdAt is not None:
            self.createdAt = isoparse(obj.createdAt)
        return self


class ExplorePageLock:
    def __init__(self):
        self.locks: list[Lock] = []
        self._id: str = ''
        self.description: str = ''
        self.featured: bool = False
        self.nbItems: int = 0
        self.order: int = 0
        self.title: str = ''
        self.type: str = ''

    def update(self, obj):
        self.__dict__ = obj.__dict__.copy()
        self.locks = Lock.generate_array(obj.locks)
        return self

    @staticmethod
    def generate_array(obj_list):
        category = []
        for account in obj_list:
            category.append(ExplorePageLock().update(account))
        return category


class SearchPublicLockCriteriaDuration:
    def __init__(self):
        self.minDuration: int = -1
        self.maxDuration: int = -1

    def dump(self):
        obj = self.__dict__.copy()
        return obj


class SearchPublicLockCriteriaExtensions:
    def __init__(self):
        self.extensions: list[str] = []
        self.all: bool = False

    def dump(self):
        obj = self.__dict__.copy()
        return obj


class SearchPublicLockCriteriaFindom:
    def __init__(self):
        self.isFindom: bool = True

    def dump(self):
        obj = self.__dict__.copy()
        return obj


class SearchPublicLockCriteria:
    def __init__(self):
        self.extensions: SearchPublicLockCriteriaExtensions = None
        self.isFindom: SearchPublicLockCriteriaFindom = None
        self.duration: SearchPublicLockCriteriaDuration = None

    def dump(self):
        obj = {}
        if self.extensions is not None:
            obj['extensions'] = self.extensions.dump()
        if self.isFindom is not None:
            obj['isFindom'] = self.isFindom.dump()
        if self.duration is not None:
            obj['duration'] = self.duration.dump()
        return obj


class SearchPublicLock:
    def __init__(self):
        self.limit: int = 15
        self.lastId: str = None
        self.criteria: SearchPublicLockCriteria = None

    def dump(self):
        obj = self.__dict__.copy()
        obj['criteria'] = {}
        if self.criteria is not None:
            obj['criteria'] = self.criteria.dump()
        return obj


class VerificationPhotoHistoryVotes:
    def __init__(self):
        self.status: str = ''
        self._id: str = ''
        self.verifiedVotes: int = 0
        self.rejectedVotes: int = 0

    def update(self, obj):
        self.__dict__ = obj.__dict__.copy()
        return self


class VerificationPhotoHistory:
    def __init__(self):
        self.verificationCode: str = ''
        self.peerVerificationId: str = ''
        self.imageKey: str = ''
        self.submittedAt: datetime.datetime = None
        self.votes: VerificationPhotoHistoryVotes = None

    def update(self, obj):
        self.__dict__ = obj.__dict__.copy()
        self.submittedAt = dateutil.parser.isoparse(obj.submittedAt)
        if obj.votes is not None:
            self.votes = VerificationPhotoHistoryVotes().update(obj.votes)
        return self

    @staticmethod
    def generate_array(obj_list):
        history = []
        for account in obj_list:
            history.append(VerificationPhotoHistory().update(account))
        return history


class Combination:
    def __init__(self):
        self.combinationId: str = ''

    def update(self, obj):
        self.__dict__ = obj.__dict__.copy()
        return self
