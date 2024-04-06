import datetime

import dateutil.parser
from . import lock, util


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
        self.lastSeen: int = None
        self.isAdmin: bool = False
        self.isModerator: bool = False
        self.metadata: Metadata = None
        self.fullLocation: str = ''
        self.discordId: str = None
        self.discordUsername: str = None
        self.isDisabled: bool = False
        self.isSuspended: bool = False
        self.features = [],
        self.joinedAt: str = None
        self.isNewMember: bool = True
        self.isSuspendedOrDisabled: bool = False

    def update(self, obj):
        self.__dict__ = obj.__dict__.copy()
        self.metadata = Metadata().update(obj.metadata)
        return self

    def dump(self):
        obj = self.__dict__.copy()
        obj['metadata'] = self.metadata.dump()
        return obj

    @staticmethod
    def generate_array(obj_list):
        users = []
        for user in obj_list:
            users.append(User().update(user))
        return users

    @staticmethod
    def dump_array(obj_list):
        return [user.dump() for user in obj_list]


class Metadata:
    def __init__(self):
        self.locktober2020Points: int = 0
        self.locktober2021Points: int = 0
        self.chastityMonth2022Points: int = 0
        self.locktober2022Points: int = 0
        self.locktober2023Points: int = 0

    def update(self, obj):
        self.__dict__ = obj.__dict__.copy()
        return self

    def dump(self):
        return self.__dict__.copy()


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

    def dump(self):
        obj = self.__dict__.copy()
        util.safe_dump_time(self, 'createdAt', obj)
        util.safe_dump_time(self, 'updatedAt', obj)
        return obj


class Stats:
    def __init__(self):
        self.nbStartedLocks: int = 0
        self.nbEndedLocks: int = 0
        self.totalTimeLocked: int = 0
        self.maxTimeLocked: int = 0
        self.keyholderNbLocks: int = 0

    def update(self, obj):
        self.__dict__ = obj.__dict__.copy()
        return self

    def dump(self):
        return self.__dict__.copy()


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

    def update(self, obj):
        self.__dict__ = obj.__dict__.copy()
        return self

    def dump(self):
        return self.__dict__.copy()


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

    def update(self, obj):
        self.__dict__ = obj.__dict__.copy()
        return self

    def dump(self):
        return self.__dict__.copy()

    @staticmethod
    def generate_array(obj_list):
        return [Achievement().update(item) for item in obj_list]

    @staticmethod
    def dump_array(obj_list):
        return [item.dump() for item in obj_list]


class DetailedUser:
    def __init__(self):
        self.user: User = None
        self.stats: Stats = None
        self.achievements: list[Achievement] = []
        self.sharedLocks: list[lock.SharedLock] = []
        self.chastikeyStats: ChastikeyStats = None

    def update(self, obj):
        self.__dict__ = obj.__dict__.copy()
        if 'user' in obj.__dict__:
            self.user = User().update(obj.user)
        self.sharedLocks = lock.SharedLock.generate_array(obj.sharedLocks)
        self.achievements = Achievement.generate_array(obj.achievements)
        self.stats = Stats().update(obj.stats)
        if 'chastikeyStats' in obj.__dict__ and obj.chastikeyStats is not None:
            self.chastikeyStats = ChastikeyStats().update(obj.chastikeyStats)
        return self

    def dump(self):
        obj = self.__dict__.copy()
        if 'user' in self.__dict__:
            obj['user'] = self.user.dump()
        obj['sharedLocks'] = lock.SharedLock.dump_array(self.sharedLocks)
        obj['achievements'] = Achievement.dump_array(self.achievements)
        util.safe_dump_parameter(self, 'chastikeyStats', obj)
        util.safe_dump_parameter(self, 'stats', obj)
        return obj


class Badges:
    def __init__(self):
        self.pendingMessages: int = 0
        self.unreadMessages: int = 0
        self.keyholdingRequests: int = 0

    def update(self, obj):
        self.__dict__ = obj.__dict__.copy()
        return self

    def dump(self):
        return self.__dict__.copy()


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

    def update(self, obj):
        self.__dict__ = obj.__dict__.copy()
        return self

    def dump(self):
        return self.__dict__.copy()


class AuthProfileMetadata:
    def __init__(self):
        self.locktober2020Points: int = 0
        self.locktober2021Points: int = 0
        self.chastityMonth2022Points: int = 0
        self.locktober2022Points: int = 0
        self.locktober2023Points: int = 0

    def update(self, obj):
        self.__dict__ = obj.__dict__.copy()
        return self

    def dump(self):
        return self.__dict__.copy()


class AuthProfileRegion:
    def __init__(self):
        self.name: str = ''
        self.shortCode: str = ''

    def update(self, obj):
        self.__dict__ = obj.__dict__.copy()
        return self

    def dump(self):
        return self.__dict__.copy()

    @staticmethod
    def generate_array(obj_list):
        return [AuthProfileRegion().update(item) for item in obj_list]

    @staticmethod
    def dump_array(obj_list):
        return [item.dump() for item in obj_list]


class AuthProfileCountry:
    def __init__(self):
        self.countryName: str = ''
        self.countryShortCode: str = ''
        self.regions: list[AuthProfileRegion] = []

    def update(self, obj):
        self.__dict__ = obj.__dict__.copy()
        if 'regions' in obj.__dict__ and obj.regions is not None:
            self.regions = AuthProfileRegion.generate_array(obj.regions)
        return self

    def dump(self):
        obj = self.__dict__.copy()
        if 'regions' in self.__dict__ and self.regions is not None:
            obj['regions'] = AuthProfileRegion.dump_array(self.regions)
        return obj


class AuthProfilePrivateMetadata:
    def __init__(self):
        self.locktoberPlusModalPending: bool = True

    def update(self, obj):
        self.__dict__ = obj.__dict__.copy()
        return self

    def dump(self):
        return self.__dict__.copy()


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
        self.settings = AuthProfileSettings().update(obj.settings)
        self.metadata = AuthProfileMetadata().update(obj.metadata)
        util.safe_update_parameter(obj, 'country', self, AuthProfileCountry().update)
        util.safe_update_parameter(obj, 'region', self, AuthProfileRegion().update)
        util.safe_update_parameter(obj, 'privateMetadata', self, AuthProfilePrivateMetadata().update)
        if obj.subscriptionEnd is not None:
            self.subscriptionEnd = dateutil.parser.isoparse(obj.subscriptionEnd)
        if obj.customSubscriptionEnd is not None:
            self.customSubscriptionEnd = dateutil.parser.isoparse(obj.customSubscriptionEnd)
        if obj.birthDate is not None:
            self.birthDate = dateutil.parser.isoparse(obj.birthDate)
        return self

    def dump(self):
        obj = self.__dict__.copy()
        obj['settings'] = self.settings.dump()
        obj['metadata'] = self.metadata.dump()
        obj['country'] = self.country.dump()
        obj['region'] = self.region.dump()
        obj['privateMetadata'] = self.privateMetadata.dump()
        util.safe_dump_time(self, 'subscriptionEnd', obj)
        util.safe_dump_time(self, 'customSubscriptionEnd', obj)
        util.safe_dump_time(self, 'birthDate', obj)
        return obj


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

    def dump(self):
        obj = self.__dict__.copy()
        obj['keyholder'] = self.keyholder.dump()
        util.safe_dump_time(self, 'validatedAt', obj)
        util.safe_dump_time(self, 'archivedAt', obj)
        util.safe_dump_time(self, 'createdAt', obj)
        util.safe_dump_time(self, 'updatedAt', obj)
        return obj

    @staticmethod
    def generate_array(obj_list):
        return [KeyholderOfferEntry().update(item) for item in obj_list]


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
        return [KeyholderRequestEntry().update(item) for item in obj_list]


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

    def dump(self):
        return self.__dict__.copy()

    @staticmethod
    def generate_array(obj_list):
        return [CommunityEventAction().update(item) for item in obj_list]

    @staticmethod
    def dump_array(obj_list):
        return [item.dump() for item in obj_list]


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

    def dump(self):
        obj = self.__dict__.copy()
        obj['actions'] = CommunityEventAction.dump_array(self.actions)
        return obj

    @staticmethod
    def generate_array(obj_list):
        return [CommunityEventCategory().update(cec) for cec in obj_list]


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

    def dump(self):
        obj = self.__dict__.copy()
        util.safe_dump_time(self, 'start', obj)
        util.safe_dump_time(self, 'end', obj)
        return obj


class CommunityEventTier:
    def __init__(self):
        self.name: str = ''
        self.requiredPoints: int = 0

    def update(self, obj):
        self.__dict__ = obj.__dict__.copy()
        return self

    def dump(self):
        return self.__dict__.copy()

    @staticmethod
    def generate_array(obj_list):
        return [CommunityEventTier().update(tier) for tier in obj_list]

    @staticmethod
    def dump_array(obj_list):
        return [tier.dump for tier in obj_list]


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

    def dump(self):
        obj = self.__dict__.copy()
        obj['tiers'] = CommunityEventTier.dump_array(self.tiers)
        return obj


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
        if obj.communityEvent is not None:
            self.communityEvent = CommunityEvent().update(obj.communityEvent)
        self.time = dateutil.parser.isoparse(obj.time)
        return self

    def dump(self):
        obj = self.__dict__.copy()
        if self.communityEvent is not None:
            obj['communityEvent'] = self.communityEvent.dump()
        util.safe_dump_time(self, 'time', obj)
        return obj
