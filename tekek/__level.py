from enum import Enum, unique


@unique
class __Level(Enum):
    """ Enumeration of different levels of debug message """
    LOG = "LOG"
    INFO = "INFO"
    SUCCESS = "SUCCESS"
    WARNING = "WARNING"
    ERROR = "ERROR"
    CRITICAL = "CRITICAL"
