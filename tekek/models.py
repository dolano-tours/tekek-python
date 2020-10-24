""" Tekek Models and Default Models Declaration

@author: Erlangga Ibrahim
"""
from datetime import datetime
from dataclasses import dataclass
from typing import List, Optional

from .types import RequestBodyType
from .types import MethodType


@dataclass
class Level:
    """ Level

    to store record's level information

    @param name:
    @type name: str
    @param importance:
    @type importance: int
    """
    name: str
    importance: int

    def __init__(self, name: str, importance: int):
        self.name = name
        self.importance = importance


LOG: Level = Level(name="LOG", importance=10)
DEBUG: Level = Level(name="DEBUG", importance=10)
INFO: Level = Level(name="INFO", importance=20)
WARNING: Level = Level(name="WARNING", importance=30)
ERROR: Level = Level(name="ERROR", importance=40)
EXCEPTION: Level = Level(name="EXCEPTION", importance=40)
CRITICAL: Level = Level(name="CRITICAL", importance=50)


@dataclass
class Record:
    """ Record Object

    Store log information
    """
    uuid: str
    timestamp: float
    identifier: str
    level: Level
    message: str

    def to_str(self):
        """ Format Attributes into a formatted string

        @todo: implement custom formatter
        @todo: create default formatter
        """
        return "[{}][{}][{}] {}".format(
            datetime.fromtimestamp(self.timestamp).strftime("%d%m%y-%H:%M:%S.%f"),
            self.identifier,
            self.level.name,
            self.message
        )


@dataclass
class RequestMeta:
    """ Request Configuration

    store request configuration
    """
    method_type: MethodType
    body_type: RequestBodyType
    host: str


DEFAULT_REQUEST_META: RequestMeta = RequestMeta(
    method_type=MethodType.POST,
    body_type=RequestBodyType.JSON,
    host="http://localhost:5000/tekek"
)


@dataclass
class LevelRequestModel:
    """ Request model for a Level

    configure the structure of a level to be sent as a body
    """
    name: str
    importance: str


@dataclass
class RequestModel:
    """ Generic Request Structure """
    uuid: str
    timestamp: str
    identifier: str
    message: str


@dataclass
class RequestModelJSON(RequestModel):
    """ Default JSON Request Body tructure """
    level: LevelRequestModel


DEFAULT_REQUEST_MODEL_JSON: RequestModelJSON = RequestModelJSON(
    uuid="uuid",
    timestamp="timestamp",
    identifier="identifier",
    message="message",
    level=LevelRequestModel(
        name="name",
        importance="importance"
    )
)


@dataclass
class RequestModelFORM(RequestModel):
    """ Default form or x-www-urlencoded Request Body Structure """
    level_name: str
    level_importance: str


DEFAULT_REQUEST_MODEL_FORM: RequestModelFORM = RequestModelFORM(
    uuid="uuid",
    timestamp="timestamp",
    identifier="identifier",
    message="message",
    level_name="level_name",
    level_importance="level_importance"
)


class Stack:
    """ Tekek Stack Engine

    used to store records inside memory before sending it to remote location or file
    """
    def __init__(self):
        self.__stacks: List[Record] = []

    def add(self, obj: Record) -> bool:
        """ Add Object to Stack

        @param obj: object to add
        @type obj: Record
        @return: Add Status
        @rtype: bool
        """
        self.__stacks.append(obj)
        return True

    def get(self) -> Optional[Record]:
        """ Get Object from stack

        @return: Pop Result
        @rtype: Record
        """
        if len(self.__stacks) <= 0:
            return None
        obj = self.__stacks.pop(0)
        return obj

    def is_empty(self) -> bool:
        """ Check if stack is empty

        @return: empty status
        @rtype: bool
        """
        return len(self.__stacks) == 0


@dataclass
class LevelModel:
    """ Level Model

    a model to store level model
    """
    model: Level
    request_meta: RequestMeta
    request_model: RequestModel
    queue: Stack = Stack()
