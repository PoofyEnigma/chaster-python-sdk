import datetime
from . import user
from dateutil.parser import isoparse


class LastMessage:
    def __init__(self):
        self._id: str = ''
        self.message: str = ''


class Conversation:
    def __init__(self):
        self._id: str = ''
        self.users: list[user.User] = []
        self.type: str = ''
        self.lastMessage: LastMessage = LastMessage()
        self.lastMessageAt: datetime.datetime = None
        self.createdAt: datetime.datetime = None
        self.unread: bool = False
        self.status: str = 'approved'
        self.isSenderBanned: bool = False
        self.isMember: bool = True

    def update(self, obj):
        self.__dict__.update(obj.__dict__)
        self.users = user.update(obj)
        self.lastMessageAt = isoparse(obj.lastMessageAt)
        return self

    @staticmethod
    def generate_array(obj_list):
        conversations = []
        for item in obj_list:
            conversations.append(Conversation().update(item))
        return conversations


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

    @staticmethod
    def generate_array(obj_list):
        messages = []
        for item in obj_list:
            messages.append(Message().update(item))
        return messages


class ConversationMessages:
    def __init__(self):
        self.count: int = 12
        self.hasMore: bool = False
        self.results: list[Message] = []

    def update(self, obj):
        self.__dict__ = obj.__dict__
        self.results = Message.generate_array(obj.results)
        return self


class Conversations:
    def __init__(self):
        self.count: int = 12
        self.hasMore: bool = False
        self.results: list[Message] = []

    def update(self, obj):
        self.__dict__ = obj.__dict__
        self.results = Conversation.generate_array(obj.results)
        return self
