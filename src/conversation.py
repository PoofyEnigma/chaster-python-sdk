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
        self.lastMessage = isoparse(obj.lastMessage)
        self.lastMessageAt = isoparse(obj.lastMessageAt)
        return self


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


class ConversationMessages:
    def __init__(self):
        self.count: int = 12
        self.hasMore: bool = False
        self.results: list[Message] = []

    def update(self, obj):
        self.__dict__ = obj.__dict__
        self.results = []
        for result in obj.results:
            self.results.append(Message().update(result))
        return self
