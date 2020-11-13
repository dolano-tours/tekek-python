from logging import getLogger, Logger
from typing import List

from . import DEBUG, INFO, WARNING, ERROR, CRITICAL
from .models import Log, Debug, Info, Warning, Error, Critical


class Tekek:
    def __init__(
        self,
        name: str = "Tekek Default",
        level: int = DEBUG,
        logger: Logger = getLogger("Tekek Default")):
        """Your Companion for Debugging and Issue Pusher

        Args:
            name (str, optional): Your Module Name. Defaults to "Tekek Default".
            level (int, optional): Logging Level. Defaults to DEBUG.
            logger (Logger, optional): python builtins logger. Defaults to getLogger("Tekek Default").
        """

        self.name = name
        self.level = level
        self.logger = logger
        self.logger.setLevel(self.level)

        self.log_queue: List[Log] = []

    async def debug(message: str, position: str = None): ...
    async def info(message: str, position: str = None): ...
    async def warning(message: str, position: str = None): ...
    async def error(message: str, position: str = None): ...
    async def critical(message: str, position: str = None): ...
