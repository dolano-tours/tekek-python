import sys
import time
import types
import asyncio
import logging

from datetime import datetime
from _io import TextIOWrapper
from typing import Dict, Union, Callable, List, Tuple, Optional
from uuid import uuid4

from .models import Record
from .models import RequestMeta, RequestModel
from .models import Level, LevelModel
from .models import LOG, DEBUG, INFO, WARNING, ERROR, EXCEPTION, CRITICAL
from .models import DEFAULT_REQUEST_MODEL_JSON
from .models import DEFAULT_REQUEST_META


class Tekek:
    # TODO: support console formatter
    def __init__(
            self,
            name: str,

            console_logging: bool = True,
            console_file: TextIOWrapper = sys.stderr,

            remote_logging: bool = False,
            remote_path: str = "",

            file_logging: bool = False,
            file_path: str = "",

            logger: logging.Logger = None,
            refresh_time: float = 0.3,

            app=None
    ):
        self.name: str = name
        self.refresh_time: float = refresh_time
        self.running: bool = False

        # --- CONSOLE --- #
        if not logger:
            logger: logging.Logger = logging.Logger(self.name, 10)

        self.__logger: logging.Logger = logger
        self.__console_logging: bool = console_logging
        self.__console_file: TextIOWrapper = console_file

        # --- REMOTE --- #
        self.__remote_logging: bool = remote_logging
        self.__remote_path: str = remote_path

        self.request_meta: RequestMeta = DEFAULT_REQUEST_META
        self.request_meta.host = self.__remote_path

        # --- FILE --- #
        self.__file_logging: bool = file_logging
        self.__file_path: str = file_path

        # === RUNTIME === #
        self.request_model = DEFAULT_REQUEST_MODEL_JSON
        self.__levels: Dict[str, LevelModel] = {}

        # Add default Levels to __levels
        for i in [LOG, DEBUG, INFO, WARNING, ERROR, EXCEPTION, CRITICAL]:
            self.add_level(i)

        # TODO: Fix this compat_app thing
        if app:
            if hasattr(app, "__name__") or hasattr(app, "__class__"):
                if app.__class__.__name__ == "FastAPI":
                    print("Detected Compatible FastAPI App")
                    asyncio.ensure_future(self.start())
                elif app.__class__.__name__ == "Sanic":
                    print("Detected Compatible Sanic App")
                    app.add_task(self.start())
            self.compatibility_mode = True
        else:
            self.compatibility_mode = False

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.stop()

    async def start(self):  # I Swear to got i wrote this while i'm drunk, but it works tho wtf
        """ Start Coroutine """
        if self.refresh_time < 0.25:
            print("You set refresh time below 250ms, which hard to interrupt manually")
            print("Adding delay before starting...")
            await asyncio.sleep(5.75)

        try:
            self.__manager_task = asyncio.create_task(self.__manager())
        except Exception as e:
            print(f"Starting failed to Start ! {e}")
            return
        print("Tekek service Started!")
        self.running = True
        return self.__manager_task

    def stop(self):
        self.__manager_task.cancel()
        self.running = False

    async def __remote_log_manager(self, rec_list: List[Record]):
        """ Manage Records queue to send to remote server """
        while len(rec_list) > 0:
            rec: Record = rec_list.pop(0)
            for i in range(3):  # Try 3 times
                status = await self.__log_to_remote(rec)
                if status:
                    break

    async def __file_log_manager(self, rec_list: List[Record]):
        """ Manage Records queue to write to file"""
        while len(rec_list) > 0:
            rec: Record = rec_list.pop(0)
            for i in range(3):  # Try 3 times
                status = await self.__log_to_file(rec)
                if status:
                    break

    async def __manager(self):
        """ Run Asynchronous Watcher, Manager, Logger """
        try:  # Dude, i was really drunk. why do i need try clause again ?
            print("Manager Running")
            while True:
                q = []
                for i in self.__levels:
                    while not self.__levels[i].queue.is_empty():
                        q.append(self.__levels[i].queue.get())

                if q:
                    asyncio.create_task(self.__remote_log_manager(q))
                    asyncio.create_task(self.__file_log_manager(q))

                await asyncio.sleep(self.refresh_time)

                if not self.running:
                    return
        except asyncio.CancelledError:
            print("Manager Exited successfully")

    # --- Logging Methods --- #
    async def __record(
            self,
            message: str,
            identifier: str = None,
            timestamp: float = None,
            uuid: str = None,
            level: Level = None
    ):
        """ Create and Queue Record

        @param message: record message
        @type message: str
        @param identifier: record identifier
        @type identifier: str = None
        @param timestamp: record created timestamp
        @type timestamp: float = time.time()
        @param uuid: record uuid or id
        @type uuid: str = uuid4().hex
        @param level: record level
        @type level: Level = INFO
        """

        # if identifier not set, set to tekek name

        if not identifier:
            identifier = self.name

        if not timestamp:
            timestamp = time.time()

        if not uuid:
            uuid = uuid4().hex

        if not level:
            level = INFO

        assert type(message) == str
        assert type(timestamp) == float
        assert type(uuid) == str
        assert type(level) == Level

        rec: Record = Record(
            uuid=uuid,
            message=message,
            identifier=identifier,
            timestamp=timestamp,
            level=level
        )

        asyncio.ensure_future(self.__log_to_console(rec))
        self.__levels[rec.level.name].queue.add(rec)

    async def __log_to_console(self, record: Record) -> bool:
        """ Log Record to Console directly """
        if not self.__console_logging:
            return True

        try:
            time = datetime.strftime(datetime.fromtimestamp(record.timestamp), "%H:%M:%S %d-%m-%Y")
            level = record.level.name
            print(f"[{time}][{record.identifier}][{level}] {record.message}")  # TODO: Convert to Logger instead
            return True
        except:
            return False

    async def __log_to_remote(self, record: Record) -> bool:
        """ Log Record to Remote server """
        if not self.__remote_logging:
            return True

        try:
            return True  # TODO: Implement log to remote
        except:
            return False

    async def __log_to_file(self, record: Record) -> bool:
        """ Log Record to File """
        if not self.__file_logging:
            return True

        try:
            return True  # TODO: Implement log to file
        except:
            return False

    # --- Getter / Setter Methods --- #
    def __add_level_by_level(self, level: Level):
        """ Add new level using Level Object

        @param level: your new level
        @type level: Level
        """
        assert type(level.name) == str
        assert type(level.importance) == int

        _lm = LevelModel(
            model=level,
            request_meta=self.request_meta,
            request_model=self.request_model
        )

        self.__levels[level.name] = _lm

    def __add_level_by_level_model(self, level_model: LevelModel):
        """ Add new level using LevelModel Object

        @param level_model: LevelModel object for your new shiny level
        @type level_model: LevelModel
        """
        assert type(level_model.model) == Level
        assert type(level_model.request_meta) == RequestMeta
        assert type(level_model.request_model) == RequestModel

        self.__levels[level_model.model.name] = level_model

    def __logging_func_factory(self, level: Level) -> Callable:
        """ Create Simpler Logging function for existing and new level

        @param level: correspodent level
        @type level: Level
        @return: a function attached to the level
        @rtype: Callable
        """

        def __logging_func(self, message: str, identifier: str = None) -> Tuple[bool, Union[Exception, Level]]:
            """ Create Record and Queue for logging

            @param message: log message
            @type message: str
            @param identifier: where the log coming from, so server know where it came from
            @type identifier: str
            @return: for testing purposes
            @rtype: Tuple[bool, Union[Exception, Level]]
            """
            try:
                asyncio.ensure_future(self.__record(message, identifier, level=level))
                return True, level
            except Exception as e:
                return False, e

        return __logging_func

    def add_level(self, level: Union[Level, LevelModel]):
        """ Add New Level

        @param level:
        @type level: Level or LevelModel
        """
        if type(level) == Level:
            self.__add_level_by_level(level)
        elif type(level) == LevelModel:
            self.__add_level_by_level_model(level)
        else:
            raise TypeError("Unsupported type of {}. expected Level or LevelModel".format(type(level)))

        # TODO: implement save name, for example you cant have '-' as function name
        setattr(self, str(level.name).lower(), types.MethodType(self.__logging_func_factory(level), self))

    def set_request_meta(self, new_request_meta: RequestMeta):
        """ Set global request meta, applied to all of the levels

        @param new_request_meta: new request meta
        @type new_request_meta: RequestMeta
        """
        assert type(new_request_meta) == RequestMeta

        self.request_meta: RequestMeta = new_request_meta

    def set_request_model(self, new_request_model: RequestModel):
        """ Set global request model, applied to all of the levels\

        @param new_request_model: new request model
        @type new_request_model: RequestModel
        """
        assert type(new_request_model) == RequestModel

        self.request_model: RequestModel = new_request_model

    def set_level_request_meta(self, target_level: Level, new_request_meta: RequestMeta):
        """ Set level request meta, applied to targeted level only

        @param target_level: target level to be changed
        @type target_level: Level
        @param new_request_meta: new request meta
        @type new_request_meta: RequestMeta
        """
        assert type(target_level) == Level
        assert type(new_request_meta) == RequestMeta

        for i in self.__levels:
            if i == target_level:
                self.__levels[i].request_meta = new_request_meta

        raise ValueError("target_level:{} not found !".format(target_level))

    def set_level_request_model(self, target_level: Level, new_request_model: RequestModel):
        """ Set level request model, applied to targeted level only

        @param target_level: target level to be changed
        @type target_level: Level
        @param new_request_model: new request model
        @type new_request_model: RequestModel
        """
        assert type(target_level) == Level
        assert type(new_request_model) == RequestModel

        for i in self.__levels:
            if i == target_level:
                self.__levels[i].request_model = new_request_model

        raise ValueError("target_level:{} not found !".format(target_level))

    def disable_console(self) -> bool:
        """ Disable console logging

        @rtype: bool
        """
        self.__console_logging = False
        return self.__console_logging

    def enable_console(self) -> bool:
        """ Enable console logging

        @rtype: bool
        """
        self.__console_logging = True
        return self.__console_logging

    def disable_remote(self) -> bool:
        """ Disable remote logging

        @rtype: bool
        """
        self.__remote_logging = False
        return self.__remote_logging

    def enable_remote(self) -> bool:
        """ Enable remote logging

        @rtype: bool
        """
        self.__remote_logging = True
        return self.__remote_logging

    def disable_file(self) -> bool:
        """ Disable file logging

        @rtype: bool
        """
        self.__file_logging = False
        return self.__file_logging

    def enable_file(self) -> bool:
        """ Enable file logging

        @rtype: bool
        """
        self.__file_logging = True
        return self.__file_logging

    def set_logger(self, logger: logging.Logger):
        self.__logger = logger

