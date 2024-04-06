import datetime
from . import user, util
from dateutil.parser import isoparse


class LastMessage:
    def __init__(self):
        self._id: str = ''
        self.message: str = ''

    def update(self, obj):
        self.__dict__ = obj.__dict__.copy()
        return self

    def dump(self):
        return self.__dict__.copy()


class Conversation:
    def __init__(self):
        self._id: str = ''
        self.users: list[user.User] = []
        self.type: str = ''
        self.lastMessage: LastMessage = None
        self.lastMessageAt: datetime.datetime = None
        self.createdAt: datetime.datetime = None
        self.unread: bool = False
        self.status: str = 'approved'
        self.isSenderBanned: bool = False
        self.isMember: bool = True

    def update(self, obj):
        self.__dict__ = obj.__dict__.copy()
        self.users = user.User.generate_array(obj.users)
        util.safe_update_parameter(obj, 'lastMessage', self, LastMessage().update)
        self.lastMessageAt = isoparse(obj.lastMessageAt)
        self.createdAt = isoparse(obj.createdAt)
        return self

    def dump(self):
        obj = self.__dict__.copy()
        obj['users'] = user.User.dump_array(self.users)
        util.safe_dump_parameter(self, 'lastMessage', obj)
        util.safe_dump_time(self, 'lastMessageAt', obj)
        util.safe_dump_time(self, 'createdAt', obj)
        return obj

    @staticmethod
    def generate_array(obj_list):
        return [Conversation().update(item) for item in obj_list]

    @staticmethod
    def dump_array(obj_list):
        return [item.dump() for item in obj_list]


class Message:
    def __init__(self):
        self._id: str = ''
        self.type: str = ''
        self.message: str = ''
        self.createdAt: datetime.datetime = None
        self.updatedAt: datetime.datetime = None
        self.conversation: str = ''
        self.user: str = ''
        self.attachments = []

    def update(self, obj):
        self.__dict__ = obj.__dict__
        self.createdAt = isoparse(obj.updatedAt)
        self.updatedAt = isoparse(obj.updatedAt)
        return self

    def dump(self):
        obj = self.__dict__.copy()
        util.safe_dump_time(self, 'createdAt', obj)
        util.safe_dump_time(self, 'updatedAt', obj)
        return obj

    @staticmethod
    def generate_array(obj_list):
        return [Message().update(item) for item in obj_list]

    @staticmethod
    def dump_array(obj_list):
        return [item.dump() for item in obj_list]


class ConversationMessages:
    def __init__(self):
        self.count: int = 12
        self.hasMore: bool = False
        self.results: list[Message] = []

    def update(self, obj):
        self.__dict__ = obj.__dict__
        self.results = Message.generate_array(obj.results)
        return self

    def dump(self):
        obj = self.__dict__.copy()
        obj['results'] = Message.dump_array(self.results)
        return obj


class Conversations:
    def __init__(self):
        self.count: int = 12
        self.hasMore: bool = False
        self.results: list[Conversation] = []

    def update(self, obj):
        self.__dict__ = obj.__dict__
        self.results = Conversation.generate_array(obj.results)
        return self

    def dump(self):
        obj = self.__dict__.copy()
        obj['results'] = Conversation.dump_array(self.results)
        return obj
