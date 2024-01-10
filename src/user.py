import datetime
from . import shared_lock
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


class Stats:
    def __init__(self):
        self.nbStartedLocks: int = 0
        self.nbEndedLocks: int = 0
        self.totalTimeLocked: int = 0
        self.maxTimeLocked: int = 0
        self.keyholderNbLocks: int = 0


class ChastikeyStats:
    def __init__(self):
        self._id: str = ''
        self.totalLocksManaged: int = 0
        self.cumulativeSecondsLocked: int = 0
        self.averageTimeLockedInSeconds: int = 0
        self.longestCompletedLockInSeconds: int = 0
        self.totalNoOfCompletedLocks: int = 0
        self.username: str = ''
        self.mainRole: str = ''


class Achievement:
    def __init__(self):
        self.slug: str = ''
        self.granted: bool = True
        self.progress: int = 0
        self.total: int = 0
        self.grantedAt: str = ''
        self.name: str = ''
        self.description: str = ''
        self.category: str = ''
        self.progressEnabled: bool = True
        self.hideIfNotGranted: bool = True


class DetailedUser:
    def __init__(self):
        self.user: User = None
        self.stats: Stats = None
        self.achievements: list[Achievement] = []
        self.sharedLocks: list[shared_lock.SharedLock] = []
        self.chastikeyStats: ChastikeyStats = None

    def update(self, obj):
        self.__dict__ = obj.__dict__.copy()
        self.user = User().update(obj.user)
        self.sharedLocks = shared_lock.shared_locks(obj.sharedLocks)
        return self


class Badges:
    def __init__(self):
        self.pendingMessages: int = 0
        self.unreadMessages: int = 0
        self.keyholdingRequests: int = 0

    def update(self, obj):
        self.__dict__ = obj.__dict__.copy()
        return self


class AuthProfileSettings:
    def __init__(self):
        self.showLocksOnProfile: bool = True
        self.showOnlineStatus: bool = True
        self.showDiscordOnProfile: bool = True
        self.emailOnWearerUsesSharedLock: bool = True
        self.messageOnWearerUsesSharedLock: bool = True
        self.discordNotifications: bool = True
        self.discordMessagingNotifications: bool = True
        self.displayNsfw: bool = True
        self.showAge: bool = True


class AuthProfileMetadata:
    def __init__(self):
        self.locktober2020Points: int = 0
        self.locktober2021Points: int = 0
        self.chastityMonth2022Points: int = 0
        self.locktober2022Points: int = 0
        self.locktober2023Points: int = 0


class AuthProfileRegion:
    def __init__(self):
        self.name: str = ''
        self.shortCode: str = ''


class AuthProfileCountry:
    def __init__(self):
        self.countryName: str = ''
        self.countryShortCode: str = ''
        self.regions: list[AuthProfileRegion] = []


class AuthProfilePrivateMetadata:
    def __init__(self):
        self.locktoberPlusModalPending: bool = True


class AuthProfile:
    def __init__(self):
        self.features: list[str] = []
        self.canEditUsername: bool = True
        self.email: str = ''
        self.keycloakId: str = ''
        self.username: str = ''
        self.subscriptionEnd: datetime.datetime = None
        self.customSubscriptionEnd: datetime.datetime = None
        self.hasPastDueSubscription: bool = True
        self.description: str = ''
        self.location: str = ''
        self.gender: str = ''
        self.birthDate: datetime.datetime = None
        self.role: str = ''
        self.emailVerified: bool = True
        self.isDeveloper: bool = True
        self.isModerator: bool = True
        self.subscriptionCancelAfterEnd: bool = True
        self.discordId: str = ''
        self.discordUsername: str = ''
        self.isAdmin: bool = True
        self.isFindom: bool = True
        self.hasAcceptedCommunityRules: bool = True
        self._id: str = ''
        self.avatarUrl: str = ''
        self.isPremium: bool = True
        self.needsDiscordMigration: bool = True
        self.settings: AuthProfileSettings = None
        self.metadata: AuthProfileMetadata = None
        self.country: AuthProfileCountry = None
        self.region: AuthProfileRegion = None
        self.privateMetadata: AuthProfilePrivateMetadata = None

    def update(self, obj):
        self.__dict__ = obj.__dict__.copy()
        if obj.subscriptionEnd is not None:
            self.subscriptionEnd = dateutil.parser.isoparse(obj.subscriptionEnd)
        if obj.customSubscriptionEnd is not None:
            self.customSubscriptionEnd = dateutil.parser.isoparse(obj.customSubscriptionEnd)
        if obj.birthDate is not None:
            self.birthDate = dateutil.parser.isoparse(obj.birthDate)
        return self


def keyholder_offer_list_update(obj):
    out = []
    for item in obj:
        out.append(KeyholderOfferEntry().update(item))
    return out


class KeyholderOfferEntry:
    def __init__(self):
        self.keyholder: User = None
        self.lock: str = ''
        self.status: str = ''
        self.validatedAt: datetime.datetime = None
        self.archivedAt: datetime.datetime = None

    def update(self, obj):
        self.__dict__ = obj.__dict__.copy()
        self.keyholder = User().update(obj.keyholder)
        if obj.validatedAt is not None:
            self.validatedAt = dateutil.parser.isoparse(obj.validatedAt)
        if obj.archivedAt is not None:
            self.archivedAt = dateutil.parser.isoparse(obj.archivedAt)
        return self

