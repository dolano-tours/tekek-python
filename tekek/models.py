from datetime import datetime
from dataclasses import dataclass

from .types import RequestBodyType
from .types import MethodType


@dataclass
class Level:
    name: str
    importance: int


LOG: Level = Level(name="LOG", importance=10)
DEBUG: Level = Level(name="DEBUG", importance=10)
INFO: Level = Level(name="INFO", importance=20)
WARNING: Level = Level(name="WARNING", importance=30)
ERROR: Level = Level(name="ERROR", importance=40)
EXCEPTION: Level = Level(name="EXCEPTION", importance=40)
CRITICAL: Level = Level(name="CRITICAL", importance=50)


@dataclass
class Record:
    """ Default Record Structure """
    uuid: str
    timestamp: float
    identifier: str
    level: Level
    message: str

    def to_str(self):
        return "[{}][{}][{}] {}".format(
            datetime.fromtimestamp(self.timestamp).strftime("%d%m%y-%H:%M:%S.%f"),
            self.identifier,
            self.level.name,
            self.message
        )


@dataclass
class RequestMeta:
    """ Request Configuration """
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

from .stack import Stack


@dataclass
class LevelModel:
    model: Level
    request_meta: RequestMeta
    request_model: RequestModel
    queue: Stack = Stack(Level)
