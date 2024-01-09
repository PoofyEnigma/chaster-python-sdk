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


"""
{


  "sharedLocks": [
    {
      "durationMode": "duration",
      "maxLimitDuration: int = 0
      "minDate": "2024-01-09T20:54:14.292Z",
      "maxDate": "2024-01-09T20:54:14.292Z",
      "maxLimitDate": "2024-01-09T20:54:14.292Z",
      "displayRemainingTime: bool = True
      "limitLockTime: bool = True
      "maxLockedUsers": 1,
      "isPublic: bool = True
      "requireContact: bool = True
      "name: str = ''
      "description: str = ''
      "unsplashPhoto": {
self.id: str = ''
self.username: str = ''
self.name: str = ''
self.url": "string"
      },
      "hideTimeLogs: bool = True
      "isFindom: bool = True
      "lastSavedAt": "2024-01-09T20:54:14.292Z",
      "_id: str = ''
      "calculatedMaxLimitDuration: int = 0
      "extensions": [
        {
  self.slug: str = ''
  self.config": {},
  self.name: str = ''
  self.textConfig: str = ''
  self.mode": "cumulative",
  self.regularity": 0
        }
      ],
      "createdAt: str = ''
      "updatedAt: str = ''
      "deletedAt: str = ''
      "archivedAt: str = ''
      "locks": [
        {
  self.status": "locked",
  self._id: str = ''
  self.endDate": "2024-01-09T20:54:14.292Z",
  self.title: str = ''
  self.totalDuration: int = 0
  self.user": {
    self.role": "keyholder",
    self.features": [
      self.partner_extensions"
            ],
    self._id: str = ''
    self.username: str = ''
    self.isPremium: bool = True
    self.description: str = ''
    self.location: str = ''
    self.gender: str = ''
    self.age: int = 0
    self.isFindom: bool = True
    self.avatarUrl: str = ''
    self.online: bool = True
    self.lastSeen: int = 0
    self.isAdmin: bool = True
    self.isModerator: bool = True
    self.metadata": {
      self.locktober2020Points: int = 0
      self.locktober2021Points: int = 0
      self.chastityMonth2022Points: int = 0
      self.locktober2022Points: int = 0
      self.locktober2023Points": 0
            },
    self.fullLocation: str = ''
    self.discordId: str = ''
    self.discordUsername: str = ''
    self.isDisabled: bool = True
    self.isSuspended: bool = True
    self.joinedAt: str = ''
    self.isNewMember: bool = True
    self.isSuspendedOrDisabled": true
          },
  self.keyholder": {
    self.role": "keyholder",
    self.features": [
      self.partner_extensions"
            ],
    self._id: str = ''
    self.username: str = ''
    self.isPremium: bool = True
    self.description: str = ''
    self.location: str = ''
    self.gender: str = ''
    self.age: int = 0
    self.isFindom: bool = True
    self.avatarUrl: str = ''
    self.online: bool = True
    self.lastSeen: int = 0
    self.isAdmin: bool = True
    self.isModerator: bool = True
    self.metadata": {
      self.locktober2020Points: int = 0
      self.locktober2021Points: int = 0
      self.chastityMonth2022Points: int = 0
      self.locktober2022Points: int = 0
      self.locktober2023Points": 0
            },
    self.fullLocation: str = ''
    self.discordId: str = ''
    self.discordUsername: str = ''
    self.isDisabled: bool = True
    self.isSuspended: bool = True
    self.joinedAt: str = ''
    self.isNewMember: bool = True
    self.isSuspendedOrDisabled": true
          },
  self.sharedLock": {
    self.durationMode": "duration",
    self._id: str = ''
    self.minDuration: int = 0
    self.maxDuration: int = 0
    self.calculatedMaxLimitDuration: int = 0
    self.user": {
      self.role": "keyholder",
      self.features": [
        self.partner_extensions"
              ],
      self._id: str = ''
      self.username: str = ''
      self.isPremium: bool = True
      self.description: str = ''
      self.location: str = ''
      self.gender: str = ''
      self.age: int = 0
      self.isFindom: bool = True
      self.avatarUrl: str = ''
      self.online: bool = True
      self.lastSeen: int = 0
      self.isAdmin: bool = True
      self.isModerator: bool = True
      self.metadata": {
        self.locktober2020Points: int = 0
        self.locktober2021Points: int = 0
        self.chastityMonth2022Points: int = 0
        self.locktober2022Points: int = 0
        self.locktober2023Points": 0
              },
      self.fullLocation: str = ''
      self.discordId: str = ''
      self.discordUsername: str = ''
      self.isDisabled: bool = True
      self.isSuspended: bool = True
      self.joinedAt: str = ''
      self.isNewMember: bool = True
      self.isSuspendedOrDisabled": true
            },
    self.unsplashPhoto": {
      self.id: str = ''
      self.username: str = ''
      self.name: str = ''
      self.url": "string"
            },
    self.extensions": [
              {
        self.slug: str = ''
        self.config": {},
        self.name: str = ''
        self.textConfig: str = ''
        self.mode": "cumulative",
        self.regularity": 0
              }
            ],
    self.createdAt: str = ''
    self.updatedAt: str = ''
    self.deletedAt: str = ''
    self.archivedAt: str = ''
    self.locks": [
      self.string"
            ],
    self.requirePassword: bool = True
    self.password: str = ''
    self.maxLimitDuration: int = 0
    self.minDate": "2024-01-09T20:54:14.292Z",
    self.maxDate": "2024-01-09T20:54:14.292Z",
    self.maxLimitDate": "2024-01-09T20:54:14.292Z",
    self.displayRemainingTime: bool = True
    self.limitLockTime: bool = True
    self.maxLockedUsers": 1,
    self.isPublic: bool = True
    self.requireContact: bool = True
    self.name: str = ''
    self.description: str = ''
    self.hideTimeLogs: bool = True
    self.isFindom: bool = True
    self.lastSavedAt": "2024-01-09T20:54:14.292Z"
          },
  self.isAllowedToViewTime: bool = True
  self.canBeUnlocked: bool = True
  self.canBeUnlockedByMaxLimitDate: bool = True
  self.isFrozen: bool = True
  self.role": "keyholder",
  self.extensions": [
            {
      self.slug: str = ''
      self.config": {},
      self._id: str = ''
      self.displayName: str = ''
      self.summary: str = ''
      self.subtitle: str = ''
      self.icon: str = ''
      self.mode": "cumulative",
      self.userData": {},
      self.regularity: int = 0
      self.nbActionsRemaining: int = 0
      self.nextActionDate: str = ''
      self.isPartner: bool = True
      self.textConfig: str = ''
      self.createdAt: str = ''
      self.updatedAt": "string"
            }
          ],
  self.combination: str = ''
  self.availableHomeActions": [
            {
      self.extensionPartyId: str = ''
      self.slug: str = ''
      self.title: str = ''
      self.description: str = ''
      self.icon: str = ''
      self.badge": "string"
            }
          ],
  self.reasonsPreventingUnlocking": [
            {
      self.reason: str = ''
      self.icon": "string"
            }
          ],
  self.extensionsAllowUnlocking: bool = True
  self.lastVerificationPicture": {
    self.imageKey: str = ''
    self.submittedAt": "2024-01-09T20:54:14.293Z",
    self.verificationCode: str = ''
    self.filename: str = ''
    self.peerVerificationId": "string"
          },
  self.createdAt": "2024-01-09T20:54:14.293Z",
  self.updatedAt": "2024-01-09T20:54:14.293Z",
  self.startDate": "2024-01-09T20:54:14.293Z",
  self.minDate": "2024-01-09T20:54:14.293Z",
  self.maxDate": "2024-01-09T20:54:14.293Z",
  self.maxLimitDate": "2024-01-09T20:54:14.293Z",
  self.displayRemainingTime: bool = True
  self.limitLockTime: bool = True
  self.deletedAt": "2024-01-09T20:54:14.293Z",
  self.unlockedAt": "2024-01-09T20:54:14.293Z",
  self.archivedAt": "2024-01-09T20:54:14.293Z",
  self.frozenAt": "2024-01-09T20:54:14.293Z",
  self.keyholderArchivedAt": "2024-01-09T20:54:14.293Z",
  self.allowSessionOffer: bool = True
  self.isTestLock: bool = True
  self.offerToken: str = ''
  self.hideTimeLogs: bool = True
  self.trusted": true
        }
      ],
      "requirePassword: bool = True
      "minDuration: int = 0
      "maxDuration: int = 0
      "joinRules": {
self.canBeJoined: bool = True
self.containsPremiumExtension: bool = True
self.exceedsExtensionLimit: bool = True
self.oneOfExtensionsDisabled": true
      }
    }
  ],

}
"""


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
        return self