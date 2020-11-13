import logging


class Level:
    def __init__(self, level: int, name: str):
        self.level = level
        self.name = name

class Debug(Level):
    def __init__(self):
        self.level = logging.DEBUG
        self.name = "DEBUG"
        super().__init__(self.level, self.name)

class Info(Level):
    def __init__(self):
        self.level = logging.INFO
        self.name = "INFO"
        super().__init__(self.level, self.name)

class Warning(Level):
    def __init__(self):
        self.level = logging.WARNING
        self.name = "DEBUG"
        super().__init__(self.level, self.name)

class Error(Level):
    def __init__(self):
        self.level = logging.ERROR
        self.name = "ERROR"
        super().__init__(self.level, self.name)

class Critical(Level):
    def __init__(self):
        self.level = logging.CRITICAL
        self.name = "CRITICAL"
        super().__init__(self.level, self.name)


__all__ = [
    "Level",
    "Debug",
    "Info",
    "Warning",
    "Error",
    "Critical"
]
