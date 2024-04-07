import datetime
import dateutil.parser

mode_non_cumulative = 'non_cumulative'
mode_cumulative = 'cumulative'
mode_unlimited = 'unlimited'


class Extension:
    def __init__(self):
        self._id: str = ''  # Lock only
        self.textConfig: str = ''
        self.name: str = None  # Shared lock only
        self.displayName: str = None  # Lock only
        self.createdAt: datetime.datetime = None  # Lock only
        self.updatedAt: datetime.datetime = None  # Lock only
        self.isPartner: bool = None  # Lock only
        self.nbActionsRemaining: int = None  # Lock only
        self.userData = None  # Lock only
        self.summary: str = None  # Lock only
        self.subtitle: str = None  # Lock only
        self.icon: str = None  # Lock only

    def get_name(self):
        if self.displayName is not None:
            return self.displayName
        if self.name is not None:
            return self.name
        return ''

    def update(self, obj):
        self.__dict__ = obj.__dict__.copy()
        if 'createdAt' in obj.__dict__ and obj.createdAt is not None:
            self.createdAt = dateutil.parser.isoparse(obj.createdAt)
        if 'updatedAt' in obj.__dict__ and obj.updatedAt is not None:
            self.updatedAt = dateutil.parser.isoparse(obj.updatedAt)
        return self

    @staticmethod
    def generate_array(obj_list):
        h = ExtensionsHandler()
        for extension in obj_list:
            h.add(extension)
        return h.generate_array()


class Extensions:
    def __init__(self):
        self.extensions = []

    def dump(self):
        obj = []
        for extension in self.extensions:
            obj.append(extension.dump())
        return {'extensions': obj}

    def update(self, obj):
        self.__dict__ = obj.__dict__.copy()
        return self


class ExtensionsHandler:

    # Do these need to be arrays?
    def __init__(self):
        self.share_links: list[ShareLinks] = []
        self.pillories: list[Pillory] = []
        self.hygiene_openings: list[HygieneOpening] = []
        self.dice: list[Dice] = []
        self.wheel_of_fortunes: list[WheelOfFortune] = []
        self.tasks: list[Tasks] = []
        self.penalties: list[Penalties] = []
        self.verification_pictures: list[VerificationPicture] = []
        self.random_events: list[RandomEvents] = []
        self.guess_timers: list[GuessTheTimer] = []

    def add_defined(self, extension):
        if extension.slug == 'link':
            self.share_links.append(extension)
        if extension.slug == 'pillory':
            self.pillories.append(extension)
        if extension.slug == 'temporary-opening':
            self.hygiene_openings.append(extension)
        if extension.slug == 'dice':
            self.dice.append(extension)
        if extension.slug == 'wheel-of-fortune':
            self.wheel_of_fortunes.append(extension)
        if extension.slug == 'tasks':
            self.tasks.append(extension)
        if extension.slug == 'penalty':
            self.penalties.append(extension)
        if extension.slug == 'verification-picture':
            self.verification_pictures.append(extension)
        if extension.slug == 'random-events':
            self.random_events.append(extension)
        if extension.slug == 'guess-timer':
            self.guess_timers.append(extension)

    def load_defined(self, extensions):
        for extension in extensions:
            self.add_defined(extension)
        return self

    def load(self, extensions):
        for extension in extensions:
            self.add(extension)
        return self

    def add(self, extension):
        if extension.slug == 'link':
            self.share_links.append(ShareLinks().update(extension))
        if extension.slug == 'pillory':
            self.pillories.append(Pillory().update(extension))
        if extension.slug == 'temporary-opening':
            self.hygiene_openings.append(HygieneOpening().update(extension))
        if extension.slug == 'dice':
            self.dice.append(Dice().update(extension))
        if extension.slug == 'wheel-of-fortune':
            self.wheel_of_fortunes.append(WheelOfFortune().update(extension))
        if extension.slug == 'tasks':
            self.tasks.append(Tasks().update(extension))
        if extension.slug == 'penalty':
            self.penalties.append(Penalties().update(extension))
        if extension.slug == 'verification-picture':
            self.verification_pictures.append(VerificationPicture().update(extension))
        if extension.slug == 'random-events':
            self.random_events.append(RandomEvents().update(extension))
        if extension.slug == 'guess-timer':
            self.guess_timers.append(GuessTheTimer().update(extension))

    def generate_array(self):
        extensions = []
        for item in self.__dict__:
            item = self.__dict__[item]
            for entry in item:
                extensions.append(entry)
        return extensions

    def dump(self):
        extensions = []
        for item in self.__dict__:
            item = self.__dict__[item]
            for entry in item:
                extensions.append(entry.dump())
        return extensions


def generate_punishment(punishment):
    if punishment.name == 'freeze':
        return PunishmentFreeze()
    if punishment.name == 'add_time':
        return PunishmentAddTime(punishment.params)
    if punishment.name == 'pillory':
        return PunishmentPillory(punishment.params.duration)


class PunishmentPilloryParams:
    def __init__(self, time):
        self.duration: int = time

    def dump(self):
        return self.__dict__.copy()


class Punishment:
    def __init__(self, name):
        self.name: str = name

    def get_time(self):
        pass

    def set_time(self, time: int):
        pass

    def dump(self):
        pass

    @staticmethod
    def generate_array(obj_list):
        return [generate_punishment(punishment) for punishment in obj_list]

    @staticmethod
    def dump_array(obj_list):
        return [punishment.dump() for punishment in obj_list]


class PunishmentPillory(Punishment):
    def __init__(self, pillory_duration):
        """

        :param pillory_duration: in seconds
        """
        super().__init__('pillory')
        self.params: PunishmentPilloryParams = PunishmentPilloryParams(pillory_duration)

    def get_time(self):
        return self.params.duration

    def set_time(self, time: int):
        self.params.duration = time

    def dump(self):
        obj = self.__dict__.copy()
        obj['params'] = self.params.dump()
        return obj


class PunishmentAddTime(Punishment):
    def __init__(self, time):
        super().__init__('add_time')
        self.params: int = time

    def get_time(self):
        return self.params

    def set_time(self, time: int):
        self.params = time

    def dump(self):
        return self.__dict__.copy()


class PunishmentFreeze(Punishment):
    def __init__(self):
        super().__init__('freeze')

    def dump(self):
        return self.__dict__.copy()


class ShareLinksConfig:
    def __init__(self):
        self.timeToAdd: int = 3600
        self.timeToRemove: int = 3600
        self.enableRandom: bool = True
        self.nbVisits: int = 25
        self.limitToLoggedUsers: bool = True

    def dump(self):
        return self.__dict__.copy()

    def update(self, obj):
        self.__dict__ = obj.__dict__.copy()
        return self


class ShareLinks(Extension):
    def __init__(self):
        super().__init__()
        self.slug: str = 'link'
        self.config: ShareLinksConfig = ShareLinksConfig()
        self.mode: str = mode_unlimited
        """
        options 'non_cumulative', 'cumulative', 'unlimited'
        """
        self.regularity: int = 3600

    def update(self, obj):
        super().update(obj)
        self.config = ShareLinksConfig().update(obj.config)
        return self

    def dump(self):
        obj = {}
        obj['slug'] = self.slug
        obj['mode'] = self.mode
        obj['regularity'] = self.regularity
        obj['config'] = self.config.dump()
        return obj


class PilloryConfig:
    def __init__(self):
        self.timeToAdd: int = 3600
        self.limitToLoggedUsers: bool = True

    def dump(self):
        return self.__dict__.copy()

    def update(self, obj):
        self.__dict__ = obj.__dict__.copy()
        return self


class Pillory(Extension):
    def __init__(self):
        super().__init__()
        self.slug: str = 'pillory'
        self.config: PilloryConfig = PilloryConfig()
        self.mode: str = mode_unlimited
        """
        options 'non_cumulative', 'cumulative', 'unlimited'
        """
        self.regularity: int = 3600

    def update(self, obj):
        super().update(obj)
        self.config = PilloryConfig().update(obj.config)
        return self

    def dump(self):
        obj = {}
        obj['slug'] = self.slug
        obj['mode'] = self.mode
        obj['regularity'] = self.regularity
        obj['config'] = self.config.dump()
        return obj


class HygieneOpeningConfig:
    def __init__(self):
        self.openingTime: int = 900
        self.penaltyTime: int = 43200
        self.allowOnlyKeyholderToOpen: bool = False

    def dump(self):
        return self.__dict__.copy()

    def update(self, obj):
        self.__dict__ = obj.__dict__.copy()
        return self


class HygieneOpening(Extension):
    def __init__(self):
        super().__init__()
        self.slug: str = 'temporary-opening'
        self.config: HygieneOpeningConfig = HygieneOpeningConfig()
        self.mode: str = mode_non_cumulative
        """
        options 'non_cumulative', 'cumulative', 'unlimited'
        """
        self.regularity: int = 172800

    def update(self, obj):
        super().update(obj)
        self.config = HygieneOpeningConfig().update(obj.config)
        return self

    def dump(self):
        obj = {}
        obj['slug'] = self.slug
        obj['mode'] = self.mode
        obj['regularity'] = self.regularity
        obj['config'] = self.config.dump()
        return obj


class DiceConfig:
    def __init__(self):
        self.multiplier: int = 3600

    def dump(self):
        return self.__dict__.copy()

    def update(self, obj):
        self.__dict__ = obj.__dict__.copy()
        return self


class Dice(Extension):
    def __init__(self):
        super().__init__()
        self.slug: str = 'dice'
        self.config: DiceConfig = DiceConfig()
        self.mode: mode_non_cumulative = mode_non_cumulative
        self.regularity: int = 1

    def update(self, obj):
        super().update(obj)
        self.config = DiceConfig().update(obj.config)
        return self

    def dump(self):
        obj = {}
        obj['slug'] = self.slug
        obj['mode'] = self.mode
        obj['config'] = self.config.dump()
        obj['regularity'] = self.regularity
        return obj


class WheelOfFortuneSegment:

    def __init__(self):
        self.type: str = ''
        """can equal one of the following: 
        'add-time' 
        'remove-time'
        'add-remove-time'
        'text'
        'set-freeze'
        'set-unfreeze'
        'pillory'
        'freeze' - this one toggles freeze
        """
        self.text: str = ''
        self.duration: int = 0

    def set_type(self, type):
        """

        :param type: can be one of the following:
        :return:
        """
        self.type = type

    def dump(self):
        return self.__dict__.copy()

    def update(self, obj):
        self.__dict__ = obj.__dict__.copy()
        return self

    @staticmethod
    def generate_array(obj_list):
        return [WheelOfFortuneSegment().update(item) for item in obj_list]


class WheelOfFortuneConfig:
    def __init__(self):
        self.segments: list[WheelOfFortuneSegment] = []

    def dump(self):
        obj = self.__dict__.copy()
        obj['segments'] = []
        for segment in self.segments:
            obj['segments'].append(segment.dump())
        return obj

    def update(self, obj):
        self.__dict__ = obj.__dict__.copy()
        self.segments = WheelOfFortuneSegment.generate_array(obj.segments)
        return self


class WheelOfFortune(Extension):
    def __init__(self):
        super().__init__()
        self.slug: str = "wheel-of-fortune"
        self.config: WheelOfFortuneConfig = WheelOfFortuneConfig()
        self.mode: str = mode_non_cumulative
        """
        options 'non_cumulative', 'cumulative', 'unlimited'
        """
        self.regularity: int = 3600

    def update(self, obj):
        super().update(obj)
        self.config = WheelOfFortuneConfig().update(obj.config)
        return self

    def dump(self):
        obj = {}
        obj['slug'] = self.slug
        obj['mode'] = self.mode
        obj['regularity'] = self.regularity
        obj['config'] = self.config.dump()
        return obj


class Task:
    def __init__(self):
        self.task: str = ''
        self.points: int = 0

    def update(self, obj):
        self.__dict__ = obj.__dict__.copy()
        return self

    def dump(self):
        return self.__dict__.copy()

    @staticmethod
    def generate_array(obj_list):
        return [Task().update(item) for item in obj_list]


class TasksConfig:
    def __init__(self):
        self.tasks: list[Task] = []
        self.voteEnabled: bool = True
        self.voteDuration: int = 3600
        self.startVoteAfterLastVote: bool = False
        self.enablePoints: bool = False
        self.pointsRequired: int = 0
        self.allowWearerToEditTasks: bool = False
        self.allowWearerToConfigureTasks: bool = False
        self.preventWearerFromAssigningTasks: bool = False
        self.allowWearerToChooseTasks: bool = True
        self.actionsOnAbandonedTask: list[Punishment] = []

    def update(self, obj):
        self.__dict__ = obj.__dict__.copy()
        self.actionsOnAbandonedTask = Punishment.generate_array(obj.actionsOnAbandonedTask)
        self.tasks = Task.generate_array(obj.tasks)
        return self

    def dump(self):
        obj = self.__dict__.copy()
        obj['tasks'] = []
        for task in self.tasks:
            obj['tasks'].append(task.dump())
        obj['actionsOnAbandonedTask'] = []
        for action in self.actionsOnAbandonedTask:
            obj['actionsOnAbandonedTask'].append(action.dump())
        return obj


class Tasks(Extension):
    def __init__(self):
        super().__init__()
        self.slug: str = 'tasks'
        self.config: TasksConfig = TasksConfig()
        self.mode: str = mode_non_cumulative
        """
        options 'non_cumulative', 'cumulative', 'unlimited'
        """
        self.regularity: int = 3600

    def update(self, obj):
        super().update(obj)
        self.config = TasksConfig().update(obj.config)
        return self

    def dump(self):
        obj = {}
        obj['slug'] = self.slug
        obj['mode'] = self.mode
        obj['regularity'] = self.regularity
        obj['config'] = self.config.dump()
        return obj


class PenaltyParams:
    def __init__(self):
        self.nbActions: int = 1
        self.frequency: int = 86400

    def dump(self):
        return self.__dict__.copy()


class Penalty:
    def __init__(self):
        self.prefix: str = 'default'
        self.name: str = 'tasks'
        """
        options: tasks, tasks_do_task, verification_picture_verify, dice_roll, wheel_of_fortune_turns, temporary_opening_open, temporary_opening_time_limit
        """
        self.params: PenaltyParams = PenaltyParams()
        self.punishments: list[Punishment] = []

    def update(self, obj):
        self.__dict__ = obj.__dict__.copy()
        self.punishments = Punishment.generate_array(obj.punishments)
        return self

    def dump(self):
        obj = self.__dict__.copy()
        obj['params'] = self.params.dump()
        obj['punishments'] = Punishment.dump_array(self.punishments)
        return obj

    @staticmethod
    def generate_array(obj_list):
        return [Penalty().update(penalty) for penalty in obj_list]

    @staticmethod
    def dump_array(obj_list):
        return [penalty.dump() for penalty in obj_list]


class PenaltiesConfig:
    def __init__(self):
        self.penalties: list[Penalty] = []

    def update(self, obj):
        self.penalties = Penalty.generate_array(obj.penalties)
        return self

    def dump(self):
        obj = self.__dict__.copy()
        obj['penalties'] = Penalty.dump_array(self.penalties)
        return obj


class Penalties(Extension):
    def __init__(self):
        super().__init__()
        self.slug: str = 'penalty'
        self.config: PenaltiesConfig = PenaltiesConfig()
        self.mode: str = mode_unlimited
        """
        options 'non_cumulative', 'cumulative', 'unlimited'
        """
        self.regularity: int = 3600

    def update(self, obj):
        self.__dict__ = obj.__dict__.copy()
        self.config = PenaltiesConfig().update(obj.config)
        return self

    def dump(self):
        obj = {}
        obj['slug'] = self.slug
        obj['mode'] = self.mode
        obj['regularity'] = self.regularity
        obj['config'] = self.config.dump()
        return obj


class PeerVerification:
    def __init__(self):
        self.punishments: list[Punishment] = []
        self.enabled: bool = False

    def update(self, obj):
        self.enabled = obj.enabled
        self.punishments = Punishment.generate_array(obj.punishments)
        return self

    def dump(self):
        obj = self.__dict__.copy()
        obj['punishments'] = Punishment.dump_array(self.punishments)
        return obj


class VerificationPictureConfig:
    def __init__(self):
        self.peerVerification: PeerVerification = PeerVerification()
        self.visibility: str = 'all'
        """can equal of the following:
        'all'
        'keyholder'
        """

    def update(self, obj):
        self.__dict__ = obj.__dict__
        self.peerVerification = PeerVerification().update(obj.peerVerification)
        return self

    def dump(self):
        obj = self.__dict__.copy()
        obj['peerVerification'] = self.peerVerification.dump()
        return obj


class VerificationPicture(Extension):
    def __init__(self):
        super().__init__()
        self.slug: str = "verification-picture"
        self.config: VerificationPictureConfig = VerificationPictureConfig()
        self.regularity: int = 3600
        self.mode: str = mode_non_cumulative
        """
        options 'non_cumulative', 'cumulative', 'unlimited'
        """

    def update(self, obj):
        super().update(obj)
        self.config = VerificationPictureConfig().update(obj.config)
        return self

    def dump(self):
        obj = {}
        obj['slug'] = self.slug
        obj['regularity'] = self.regularity
        obj['mode'] = self.mode
        obj['config'] = self.config.dump()
        return obj


difficulty_normal = 'normal'


class RandomEventsConfig:
    def __init__(self):
        self.difficulty: str = difficulty_normal

    def dump(self):
        return self.__dict__.copy()


class RandomEvents(Extension):
    def __init__(self):
        super().__init__()
        self.slug: str = 'random-events'
        self.config: RandomEventsConfig = RandomEventsConfig()
        self.mode: str = mode_unlimited
        """
        options 'non_cumulative', 'cumulative', 'unlimited'
        """
        self.regularity: int = 3600

    def update(self, obj):
        super().update(obj)
        return self

    def dump(self):
        obj = {}
        obj['mode'] = self.mode
        obj['regularity'] = self.regularity
        obj['slug'] = self.slug
        obj['config'] = self.config.dump()
        return obj


class GuessTheTimerConfig:
    def __init__(self):
        self.minRandomTime: int = 10800
        self.maxRandomTime: int = 21600

    def dump(self):
        return self.__dict__.copy()


class GuessTheTimer(Extension):
    def __init__(self):
        super().__init__()
        self.slug: str = 'guess-timer'
        self.config: GuessTheTimerConfig = GuessTheTimerConfig()
        self.mode: str = mode_unlimited
        """
        options 'non_cumulative', 'cumulative', 'unlimited'
        """
        self.regularity: int = 3600

    def update(self, obj):
        super().update(obj)
        return self

    def dump(self):
        obj = {}
        obj['slug'] = self.slug
        obj['mode'] = self.mode
        obj['regularity'] = self.regularity
        obj['config'] = self.config.dump()
        return obj


class KnownExtension:
    def __init__(self):
        self.defaultConfig: dict = {}
        self.partnerExtensionId: str = ''
        self.configIframeUrl: str = ''
        self.isTesting: bool = True
        self.isPartner: bool = True
        self.isDevelopedByCommunity: bool = False
        self.subtitle: str = ''
        self.summary: str = ''
        self.displayName: str = ''
        self.icon: str = ''
        self.slug: str = ''
        self.availableModes: list[str] = []
        self.defaultRegularity: int = 3600
        self.isEnabled: bool = True
        self.isPremium: bool = False
        self.isFeatured: bool = False
        self.isCountedInExtensionsLimit: bool = True
        self.hasActions: bool = True

    def update(self, obj):
        self.__dict__ = obj.__dict__.copy()
        if 'isDevelopedByCommunity' not in obj.__dict__:
            self.isDevelopedByCommunity = False
        return self

    def dump(self):
        obj = self.__dict__.copy()
        obj['defaultConfig'] = self.defaultConfig.__dict__.copy()
        return obj

    @staticmethod
    def generate_array(obj_list):
        return [KnownExtension().update(item) for item in obj_list]
