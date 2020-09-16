from typing import Any, List

import time

from .__level import __Level as Level


class __Message:
    identifier: str = None
    content: str = None
    level: Level = Level.INFO

    def __init__(self, identifier: str, content: Any, level: Level):
        self.identifier: str = identifier
        self.content: str = self.__convert_to_str(content)
        self.level: Level = level

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
            time.strftime("%H:%M:%S", time.localtime()),
            self.identifier,
            self.level,
            self.content
        )

    def __repr__(self):
        return self.__convert_to_content()

    def __str__(self):
        return self.__convert_to_content()
