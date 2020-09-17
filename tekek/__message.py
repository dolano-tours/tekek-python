import time

from datetime import datetime
from typing import Any, List
from enum import Enum

from .__level import __Level as Level


class MessageStructure(Enum):
    TIMESTAMP = time.struct_time,
    IDENTIFIER = str,
    CONTENT = Any,
    LEVEL = Level


class __Message:
    identifier: str = None
    content: str = None
    level: Level = Level.INFO

    def __init__(
            self,
            timestamp: MessageStructure.TIMESTAMP.value,
            identifier: MessageStructure.IDENTIFIER.value,
            content: MessageStructure.CONTENT.value,
            level: MessageStructure.LEVEL.value
    ):
        self.timestamp: MessageStructure.TIMESTAMP.value = timestamp
        self.identifier: MessageStructure.IDENTIFIER.value = identifier
        self.content: MessageStructure.CONTENT.value = self.__convert_to_str(content)
        self.level: MessageStructure.LEVEL.value = level

    @staticmethod
    def __convert_to_str(content: Any) -> str:
        c = None
        try:
            c = str(content)
        except:
            try:
                c = repr(content)
            except:
                ...

        return c

    def __convert_to_content(self) -> str:
        return "[{}][{}][{}] {}".format(
            time.strftime("%d-%m %H:%M:%S", self.timestamp),
            self.identifier,
            self.level.value,
            self.content
        )

    def __repr__(self):
        return self.__convert_to_content()

    def __str__(self):
        return self.__convert_to_content()
