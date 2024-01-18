import datetime
import logging

import dateutil.parser
from . import lock


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

    @staticmethod
    def generate_array(obj_list):
        users = []
        for user in obj_list:
            users.append(User().update(user))
        return users


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
        self.sharedLocks: list[lock.SharedLock] = []
        self.chastikeyStats: ChastikeyStats = None

    def update(self, obj):
        self.__dict__ = obj.__dict__.copy()
        self.user = User().update(obj.user)
        self.sharedLocks = lock.SharedLock.generate_array(obj.sharedLocks)
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


class KeyholderOfferEntry:
    def __init__(self):
        self._id: str = ''
        self.keyholder: User = None
        self.lock: str = ''
        self.status: str = ''
        self.validatedAt: datetime.datetime = None
        self.archivedAt: datetime.datetime = None
        self.createdAt: datetime.datetime = None
        self.updatedAt: datetime.datetime = None

    def update(self, obj):
        self.__dict__ = obj.__dict__.copy()
        self.keyholder = User().update(obj.keyholder)
        if obj.validatedAt is not None:
            self.validatedAt = dateutil.parser.isoparse(obj.validatedAt)
        if obj.archivedAt is not None:
            self.archivedAt = dateutil.parser.isoparse(obj.archivedAt)
        if obj.createdAt is not None:
            self.createdAt = dateutil.parser.isoparse(obj.createdAt)
        if obj.updatedAt is not None:
            self.updatedAt = dateutil.parser.isoparse(obj.updatedAt)
        return self

    @staticmethod
    def generate_array(obj_list):
        out = []
        for item in obj_list:
            out.append(KeyholderOfferEntry().update(item))
        return out


class KeyholderRequestEntry:
    def __init__(self):
        self._id: str = ''
        self.keyholder: str = ''
        self.lock: lock.Lock = None
        self.status: str = ''
        self.validatedAt: datetime.datetime = None
        self.archivedAt: datetime.datetime = None
        self.createdAt: datetime.datetime = None
        self.updatedAt: datetime.datetime = None

    def update(self, obj):
        self.__dict__ = obj.__dict__.copy()
        self.lock = lock.Lock().update(obj.lock)
        if obj.validatedAt is not None:
            self.validatedAt = dateutil.parser.isoparse(obj.validatedAt)
        if obj.archivedAt is not None:
            self.archivedAt = dateutil.parser.isoparse(obj.archivedAt)
        if obj.createdAt is not None:
            self.createdAt = dateutil.parser.isoparse(obj.createdAt)
        if obj.updatedAt is not None:
            self.updatedAt = dateutil.parser.isoparse(obj.updatedAt)
        return self

    @staticmethod
    def generate_array(obj_list):
        out = []
        for item in obj_list:
            logging.getLogger().debug(item)
            out.append(KeyholderRequestEntry().update(item))
        return out


class CommunityEventAction:
    def __init__(self):
        self.name: str = ''
        self.title: str = ''
        self.description: str = ''
        self.points: int = 0
        self.maxPerPeriod: int = 0
        self.group: str = ''

    def update(self, obj):
        self.__dict__ = obj.__dict__.copy()
        return self

    @staticmethod
    def generate_array(obj_list):
        actions = []
        for action in obj_list:
            actions.append(CommunityEventAction().update(action))
        return actions


class CommunityEventCategory:
    def __init__(self):
        self.name: str = ''
        self.title: str = ''
        self.maxPoints: int = 0
        self.actions: list[CommunityEventAction] = []
        self.hidden: bool = False

    def update(self, obj):
        self.__dict__ = obj.__dict__.copy()
        self.actions = CommunityEventAction.generate_array(obj.actions)
        if 'hidden' not in obj.__dict__:
            self.hidden = False
        return self

    @staticmethod
    def generate_array(obj_list):
        cecs = []
        for cec in obj_list:
            cecs.append(CommunityEventCategory().update(cec))
        return cecs


class CommunityEventDetails:
    def __init__(self):
        self.categories: dict[str, int] = {}
        self.actions: dict[str, int] = {}
        self.start: datetime.datetime = None
        self.end: datetime.datetime = None

    def update(self, obj):
        self.__dict__ = obj.__dict__.copy()
        self.start = dateutil.parser.isoparse(obj.start)
        self.end = dateutil.parser.isoparse(obj.end)
        return self


class CommunityEventTier:
    def __init__(self):
        self.name: str = ''
        self.requiredPoints: int = 0

    def update(self, obj):
        self.__dict__ = obj.__dict__.copy()
        return self

    @staticmethod
    def generate_array(obj_list):
        tiers = []
        for tier in obj_list:
            tiers.append(CommunityEventTier().update(tier))
        return tiers


class CommunityEvent:
    def __init__(self):
        self.enabled: bool = True
        self.slug: str = ''
        self.name: str = ''
        self.color: str = ''
        self.lightColor: str = ''
        self.icon: str = ''
        self.tiers: list[CommunityEventTier] = []

    def update(self, obj):
        self.__dict__ = obj.__dict__.copy()
        self.tiers = CommunityEventTier.generate_array(obj.tiers)
        return self


class AppSettings:
    def __init__(self):
        self.features: list[str] = []
        self.features: list[str] = []
        self.nonPremiumMaxLocks: int = 0
        self.nonPremiumMaxExtensions: int = 0
        self.maxAttachments: int = 0
        self.registerRequiresAccessKey: bool = True
        self.recaptchaClientKey: str = ''
        self.time: datetime.datetime = None
        self.version: str = ''
        self.communityEvent: CommunityEvent = None
        self.stripePublicKey: str = ''

    def update(self, obj):
        self.__dict__ = obj.__dict__.copy()
        if self.communityEvent is not None:
            self.communityEvent = CommunityEvent().update(obj.communityEvent)
        self.time = dateutil.parser.isoparse(obj.time)
        return self


class FileToken:
    def __init__(self):
        self.token: str = ''

    def update(self, obj):
        self.__dict__ = obj.__dict__.copy()
        return self


class FileUrl:
    def __init__(self):
        self.url: str = ''

    def update(self, obj):
        self.__dict__ = obj.__dict__.copy()
        return self
