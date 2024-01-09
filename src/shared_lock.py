from datetime import datetime
from . import extensions
from . import user
from dateutil.parser import isoparse



def shared_locks(obj):
    out = []
    for entry in obj:
        out.append(SharedLock().update(entry))
    return out


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
        self._id: str = '65827bb4d1f699fb821e915f'
        self.minDuration: int = 86400
        self.maxDuration: int  = 90000
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
        self.extensions = extensions.update(obj)
        if obj.maxDate is not None:
            self.maxDate = isoparse(obj.maxDate)
        if obj.minDate is not None:
            self.minDate = isoparse(obj.minDate)
        if obj.maxLimitDate is not None:
            self.maxLimitDate = isoparse(obj.maxLimitDate)
        if obj.lastSavedAt is not None:
            self.lastSavedAt = isoparse(obj.lastSavedAt)
        return self


class PageinatedSharedLockList:
    def __init__(self):
        self.lastId: str = ''
        self.hasMore: bool = True
        self.count: int = 0
        self.results: list[SharedLock] = []

    def update(self, obj):
        self.__dict__ = obj.__dict__.copy()
        self.results = []
        for item in obj.results:
            self.results.append(SharedLock().update(item))
        return self
