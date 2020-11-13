import time, json, hashlib
from uuid import NAMESPACE_X500, uuid5
from logging import Logger,  DEBUG, INFO, WARNING, ERROR, CRITICAL
from datetime import datetime
from pprint import pformat

import httpx

from .levels import *
from ..config import CONFIG

class Log:
    def __init__(self, message: str, position: str, level: Level, **kwargs):
        self.message = message
        self.position = position
        self.level = level

        self.tekek_logger = kwargs["tekek_logger_"]
        self.tekek_name = kwargs["tekek_name_"]

        self.console_success = False
        self.push_success = True if self.host else False
        self.file_success = True if self.file else False

    async def log_to_console(self):
        try:
            content = [
                pformat('  | Position: ' + self.position),
                pformat('  | Message: ' + self.message)
            ]
            if not self.tekek_logger:
                content = [f"[{datetime.utcnow()}][{self.level.name}]"] + content
                print("".join(content))
            else:
                self.tekek_logger.log(self.level.level, "\n" + "".join(content))

            self.console_success = True
        except:
            self.console_success = False

        return self.console_success

    async def log_to_remote(self):
        conf = getattr(CONFIG.REMOTE, self.level.name.upper())
        host = CONFIG.REMOTE.HOST + conf.ENDPOINT

        cur_time = time.time()
        cur_datetime = datetime.utcfromtimestamp(cur_time)
        content = {
            "client": self.tekek_name,
            "position": self.position,
            "message": self.message,
            "level": {
                "name": self.level.name,
                "importance": self.level.level
            }
        }
        content["uuid"] = uuid5(NAMESPACE_X500, f"client={},position={},message={},level_name={},level_importance={}".format(
            content["client"], content["position"], content["message"], content["level"]["name"], content["level"]["importance"]
        )).hex
        metadata = {
            "timestamp": {
                "unix": cur_time,
                "formatted": cur_datetime,
            },
            "size": len(json.dumps(content).encode("utf-8")),
            "signature": hashlib.sha512(json.dumps(content).encode("utf-8")).hexdigest()
        }

        async with httpx.AsyncClient() as client:
            f: client.get = getattr(client, conf.METHOD.lower())
            res = f(
                host,
                json={"content": content, "metadata": metadata}
            )

    async def log_to_file(self):
        ... # TOOD: Log to file

class Debug(Log):   # TODO: add kwargs handling for constructor
    def __init__(self, message: str, position: str, **kwargs):
        self.message = message
        self.position = position
        self.level = Debug
        super().__init__(message, position, self.level, **kwargs)

class Info(Log):    # TODO: add kwargs handling for constructor
    def __init__(self, message: str, position: str, **kwargs):
        self.message = message
        self.position = position
        self.level = Info
        super().__init__(message, position, self.level, **kwargs)

class Warning(Log): # TODO: add kwargs handling for constructor
    def __init__(self, message: str, position: str, **kwargs):
        self.message = message
        self.position = position
        self.level = Warning
        super().__init__(message, position, self.level, **kwargs)

class Error(Log):   # TODO: add kwargs handling for constructor
    def __init__(self, message: str, position: str, **kwargs):
        self.message = message
        self.position = position
        self.level = Error
        super().__init__(message, position, self.level, **kwargs)

class Critical(Log):    # TODO: add kwargs handling for constructor
    def __init__(self, message: str, position: str, **kwargs):
        self.message = message
        self.position = position
        self.level = Critical
        super().__init__(message, position, self.level, **kwargs)
