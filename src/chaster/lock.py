import datetime

import dateutil.parser

from . import extensions, user, util
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
        obj = self.__dict__.copy()
        eh = extensions.ExtensionsHandler()
        eh.load_defined(self.extensions)
        obj['extensions'] = eh.dump()
        return obj


class Lock:
    def __init__(self):
        self._id: str = ''
        self.startDate: datetime.datetime = None
        self.endDate: datetime.datetime = None
        self.minDate: datetime.datetime = None
        self.maxDate: datetime.datetime = None
        self.maxLimitDate: datetime.datetime | None = None
        self.displayRemainingTime: bool = True
        self.limitLockTime: bool = False
        self.status: str = ''
        self.combination: str = ''
        self.sharedLock: SharedLock | None = None
        self.createdAt: datetime.datetime = None
        self.updatedAt: datetime.datetime = None
        self.unlockedAt: datetime.datetime | None = None
        self.archivedAt: datetime.datetime | None = None
        self.frozenAt: datetime.datetime | None = None
        self.keyholderArchivedAt: datetime.datetime = None
        self.totalDuration: int = 235422887
        self.allowSessionOffer: bool = False
        self.isTestLock: bool = False
        self.offerToken: str = ''
        self.hideTimeLogs: bool = True
        self.trusted: bool = False
        self.user: user.User = None
        self.keyholder: user.User = None
        self.isAllowedToViewTime: bool = True
        self.canBeUnlocked: bool = False
        self.canBeUnlockedByMaxLimitDate: bool = False
        self.isFrozen: bool = True
        self.extensions = []
        self.role: str = ''
        self.title: str = ''
        self.lastVerificationPicture: LastVerificationPicture = None
        self.availableHomeActions: list[AvailableHomeAction] = []
        self.reasonsPreventingUnlocking = []
        self.extensionsAllowUnlocking: bool = True
        self.deletedAt: datetime.datetime = None

    def dump(self):
        obj = self.__dict__.copy()
        obj['user'] = self.user.dump()
        if 'extensions' in self.__dict__ and self.extensions is not None:
            eh = extensions.ExtensionsHandler()
            eh.load_defined(self.extensions)
            obj['extensions'] = eh.dump()
        if 'availableHomeActions' in self.__dict__ and self.availableHomeActions is not None:
            obj['availableHomeActions'] = AvailableHomeAction.dump_array(self.availableHomeActions)
        if self.keyholder is not None:
            obj['keyholder'] = self.keyholder.dump()
        if self.lastVerificationPicture is not None:
            obj['lastVerificationPicture'] = self.lastVerificationPicture.dump()
        if self.sharedLock is not None:
            obj['sharedLock'] = self.sharedLock.dump()

        times = [
            'startDate',
            'endDate',
            'minDate',
            'maxDate',
            'maxLimitDate',
            'createdAt',
            'updatedAt',
            'unlockedAt',
            'archivedAt',
            'frozenAt',
            'keyholderArchivedAt',
            'deletedAt'
        ]

        for time in times:
            util.safe_dump_time(self, time, obj)
        return obj

    def update(self, obj):
        self.__dict__ = obj.__dict__.copy()
        self.user = user.User().update(obj.user)
        if 'extensions' in obj.__dict__:
            self.extensions = extensions.Extension.generate_array(obj.extensions)
        if 'availableHomeActions' in obj.__dict__:
            self.availableHomeActions = AvailableHomeAction.generate_array(obj.availableHomeActions)
        if 'keyholder' in obj.__dict__ and obj.keyholder is not None:
            self.keyholder = user.User().update(obj.keyholder)
        if 'lastVerificationPicture' in obj.__dict__ and obj.lastVerificationPicture is not None:
            self.lastVerificationPicture = LastVerificationPicture().update(obj.lastVerificationPicture)
        if 'sharedLock' in obj.__dict__ and obj.sharedLock is not None:
            self.sharedLock = SharedLock().update(obj.sharedLock)

        times = [
            'startDate',
            'endDate',
            'minDate',
            'maxDate',
            'maxLimitDate',
            'createdAt',
            'updatedAt',
            'unlockedAt',
            'archivedAt',
            'frozenAt',
            'keyholderArchivedAt',
            'deletedAt'
        ]

        for time in times:
            util.safe_update_time(obj, time, self)
        return self

    @staticmethod
    def generate_array(obj_list):
        return [Lock().update(lock) for lock in obj_list]

    @staticmethod
    def dump_array(locks):
        return [lock.dump() for lock in locks]


class LastVerificationPicture:
    def __init__(self):
        self.verificationCode: int = 0
        self.imageFile: str = ''
        self.peerVerificationId: str = ''
        self.imageKey: str = ''
        self.submittedAt: str = ''

    def update(self, obj):
        self.__dict__ = obj.__dict__.copy()
        return self

    def dump(self):
        return self.__dict__.copy()


class AvailableHomeAction:
    def __init__(self):
        self.slug: str = ''
        self.title: str = ''
        self.description: str = ''
        self.icon: str = ''
        self.extensionPartyId: str = ''
        self.badge: str = ''

    def update(self, obj):
        self.__dict__.update(obj.__dict__)
        return self

    def dump(self):
        return self.__dict__.copy()

    @staticmethod
    def generate_array(obj_list):
        return [AvailableHomeAction().update(availableHomeAction) for availableHomeAction in obj_list]

    @staticmethod
    def dump_array(obj_list):
        return [item.dump() for item in obj_list]


class LockedUsers:
    def __init__(self):
        self.pages: int = 0
        self.total: int = 0
        self.locks: list[Lock] = []

    def update(self, obj):
        self.__dict__.update(obj.__dict__)
        self.locks = Lock.generate_array(obj.locks)
        return self

    def dump(self):
        obj = self.__dict__.copy()
        obj['locks'] = Lock.dump_array(self.locks)
        return obj


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
        self.user: user.User | None = None

    def update(self, obj):
        self.__dict__ = obj.__dict__.copy()
        if obj.createdAt is not None:
            self.createdAt = dateutil.parser.isoparse(obj.createdAt)
        util.safe_update_parameter(obj, 'user', self, user.User().update)
        return self

    def dump(self):
        obj = self.__dict__.copy()
        obj['user'] = self.user.dump()
        util.safe_dump_time(self, 'createdAt', obj)
        obj['payload'] = self.payload.__dict__.copy()
        return obj

    @staticmethod
    def generate_array(obj_list):
        return [ActionLog().update(item) for item in obj_list]

    @staticmethod
    def dump_array(obj_list):
        return [item.dump() for item in obj_list]


class PaginatedLockHistory:
    def __init__(self):
        self.count: int = 0
        self.hasMore: bool = False
        self.results: list[ActionLog] = []

    def update(self, obj):
        self.__dict__ = obj.__dict__.copy()
        self.results = ActionLog.generate_array(obj.results)
        return self

    def dump(self):
        obj = self.__dict__.copy()
        obj['results'] = ActionLog.dump_array(self.results)
        return obj


class ExtensionInformation:
    def __init__(self):
        self.lock: Lock = None
        self.extension = None

    def update(self, obj):
        self.lock = Lock().update(obj.lock)
        eh = extensions.ExtensionsHandler()
        eh.add(obj.extension)
        self.extension = eh.generate_array()[0]
        return self

    def dump(self):
        obj = self.__dict__.copy()
        obj['lock'] = self.lock.dump()
        obj['extension'] = self.extension.dump()
        return obj


class LockInfo:
    def __init__(self):
        self.password: str = None
        self.combinationId: str = ''
        self.isTestLock: bool = False

    def dump(self):
        return self.__dict__.copy()

    def update(self, obj):
        self.__dict__ = obj.__dict__.copy()
        return self


class UnsplashPhoto:
    def __init__(self):
        self.id: str = ''
        self.name: str = ''
        self.url: str = ''
        self.username: str = ''

    def update(self, obj):
        self.__dict__ = obj.__dict__.copy()
        return self

    def dump(self):
        return self.__dict__.copy()


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
        util.safe_dump_time(self, 'maxDate', dictionary)
        util.safe_dump_time(self, 'minDate', dictionary)
        util.safe_dump_time(self, 'maxLimitDate', dictionary)
        return dictionary

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
        """
        Note: self.user is a string and not a user object when acquiring from ChasterAPI.get_user_shared_locks()
        """

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
        self.user: user.User = None
        self.durationMode: str = ''
        self.isFindom: bool = False
        self.calculatedMaxLimitDuration: int = None
        self.extensions = []
        self.joinRules: JoinRules = None  # Not present when getting the user's shared lock

    def update(self, obj):
        self.__dict__ = obj.__dict__.copy()
        if 'unsplashPhoto' in obj.__dict__ and obj.unsplashPhoto is not None:
            self.unsplashPhoto = UnsplashPhoto().update(obj.unsplashPhoto)
        if 'user' in obj.__dict__ and obj.__dict__['user'] is not None and type(obj.user) is not str:
            self.user = user.User().update(obj.user)
        if 'joinRules' in obj.__dict__:
            self.joinRules = JoinRules().update(obj.joinRules)
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

    def dump(self):
        obj = self.__dict__.copy()
        if 'extensions' in self.__dict__:
            eh = extensions.ExtensionsHandler()
            eh.load_defined(self.extensions)
            obj['extensions'] = eh.dump()
        if self.unsplashPhoto is not None:
            obj['unsplashPhoto'] = self.unsplashPhoto.dump()
        util.safe_dump_parameter(self, 'user', obj)
        if 'joinRules' in self.__dict__ and self.joinRules is not None:
            obj['joinRules'] = self.joinRules.dump()
        util.safe_dump_time(self, 'maxDate', obj)
        util.safe_dump_time(self, 'minDate', obj)
        util.safe_dump_time(self, 'maxLimitDate', obj)
        util.safe_dump_time(self, 'lastSavedAt', obj)
        return obj

    @staticmethod
    def generate_array(obj_list):
        return [SharedLock().update(entry) for entry in obj_list]

    @staticmethod
    def dump_array(shared_locks):
        return [entry.dump() for entry in shared_locks]


class PaginatedSharedLockList:
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

    def dump(self):
        obj = self.__dict__.copy()
        obj['results'] = SharedLock.dump_array(self.results)
        return obj


class JoinRules:
    def __init__(self):
        self.canBeJoined: bool = True
        self.containsPremiumExtension: bool = True
        self.exceedsExtensionLimit: bool = True
        self.oneOfExtensionsDisabled: bool = True

    def dump(self):
        return self.__dict__.copy()

    def update(self, obj):
        self.__dict__ = obj.__dict__.copy()
        return self


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
        self.unsplashPhoto = UnsplashPhoto().update(obj.unsplashPhoto)
        self.user = user.User().update(obj.user)
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
        if 'createdAt' in obj.__dict__ and obj.createdAt is not None:
            self.createdAt = isoparse(obj.createdAt)
        if 'updatedAt' in obj.__dict__ and obj.updatedAt is not None:
            self.createdAt = isoparse(obj.updatedAt)
        if 'unlockedAt' in obj.__dict__ and obj.unlockedAt is not None:
            self.unlockedAt = isoparse(obj.unlockedAt)
        if 'deletedAt' in obj.__dict__ and obj.deletedAt is not None:
            self.deletedAt = isoparse(obj.deletedAt)
        self.joinRules = JoinRules().update(obj.joinRules)

        return self

    def dump(self):
        obj = self.__dict__.copy()
        obj['unsplashPhoto'] = self.unsplashPhoto.dump()
        obj['joinRules'] = self.joinRules.dump()
        obj['user'] = self.user.dump()
        eh = extensions.ExtensionsHandler()
        eh.load_defined(self.extensions)
        obj['extensions'] = eh.dump()
        if 'locks' in self.__dict__:
            obj['locks'] = Lock.dump_array(self.locks)
        util.safe_dump_time(self, 'maxDate', obj)
        util.safe_dump_time(self, 'minDate', obj)
        util.safe_dump_time(self, 'maxLimitDate', obj)
        util.safe_dump_time(self, 'lastSavedAt', obj)
        util.safe_dump_time(self, 'createdAt', obj)
        util.safe_dump_time(self, 'updatedAt', obj)
        util.safe_dump_time(self, 'unlockedAt', obj)
        util.safe_dump_time(self, 'deletedAt', obj)
        return obj


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

    def dump(self):
        obj = self.__dict__.copy()
        obj['locks'] = Lock.dump_array(self.locks)
        return obj

    @staticmethod
    def generate_array(obj_list):
        return [ExplorePageLock().update(account) for account in obj_list]


class SearchPublicLockCriteriaDuration:
    def __init__(self):
        self.minDuration: int = -1
        self.maxDuration: int = -1

    def update(self, obj):
        self.__dict__ = obj.__dict__.copy()
        return self

    def dump(self):
        obj = self.__dict__.copy()
        return obj


class SearchPublicLockCriteriaExtensions:
    def __init__(self):
        self.extensions: list[str] = []
        self.all: bool = False

    def update(self, obj):
        self.__dict__ = obj.__dict__.copy()
        return self

    def dump(self):
        obj = self.__dict__.copy()
        return obj


class SearchPublicLockCriteriaFindom:
    def __init__(self):
        self.isFindom: bool = True

    def update(self, obj):
        self.__dict__ = obj.__dict__.copy()
        return self

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
        if 'extensions' in self.__dict__:
            obj['extensions'] = self.extensions.dump()
        if 'isFindom' in self.__dict__:
            obj['isFindom'] = self.isFindom.dump()
        if 'duration' in self.__dict__:
            obj['duration'] = self.duration.dump()
        return obj

    def update(self, obj):
        self.__dict__ = obj.__dict__.copy()
        if 'extensions' in obj.__dict__:
            self.extensions = SearchPublicLockCriteriaExtensions().update(obj.extensions)
        if 'isFindom' in obj.__dict__:
            self.isFindom = SearchPublicLockCriteriaFindom().update(obj.isFindom)
        if 'duration' in obj.__dict__:
            self.duration = SearchPublicLockCriteriaDuration().update(obj.duration)

        return self


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

    def update(self, obj):
        self.__dict__ = obj.__dict__.copy()
        self.criteria = SearchPublicLockCriteria().update(obj.criteria)
        return self


class VerificationPhotoHistoryVotes:
    def __init__(self):
        self.status: str = ''
        self._id: str = ''
        self.verifiedVotes: int = 0
        self.rejectedVotes: int = 0

    def update(self, obj):
        self.__dict__ = obj.__dict__.copy()
        return self

    def dump(self):
        return self.__dict__.copy()


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

    def dump(self):
        obj = self.__dict__.copy()
        util.safe_dump_time(self, 'submittedAt', obj)
        obj['votes'] = self.votes.dump()
        return obj

    @staticmethod
    def generate_array(obj_list):
        return [VerificationPhotoHistory().update(account) for account in obj_list]
