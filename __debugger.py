import asyncio

from typing import List, Any, Optional


from .__message import __Message as Message
from .__level import __Level as Level


class __Debugger:
    def __init__(
            self,
            verbosity: int = 1,
            log_to_console: bool = True,
            log_to_file: bool = False,
            log_to_server: bool = False
    ):
        self.__verbosity: int = verbosity
        self.__log_to_console: bool = log_to_console
        self.__log_to_file: bool = log_to_file
        self.__log_to_server: bool = log_to_server

        self.__queue: List[Message] = []

        asyncio.ensure_future(self.__start())

    async def __add_to_queue(self, message: Message) -> bool:
        """ Add to Queue

        :return bool:
        """
        try:
            self.__queue.append(message)
            return True
        except Exception as e:
            print("Failed to add to queue {}".format(e))
        return False

    async def __pop_from_queue(self, index: int) -> Optional[Message]:
        """ Pop from Queue

        :return Message:
        """
        try:
            msg: Message = self.__queue.pop(index)
            return msg
        except Exception as e:
            print("Failed to pop from queue {}".format(e))
        return None

    @staticmethod
    async def __to_console(message: Message):
        print(message)

    @staticmethod
    async def __to_file(message: Message):
        # TODO: Implement logging to file
        return

    @staticmethod
    async def __to_server(message: Message, tries: int = -1):
        # TODO: implement push logging to server
        return

    async def __log(self):
        # TODO: Implement smart logging, so the highest importance get pushed first
        msg: Message = self.__queue[len(self.__queue)-1]
        asyncio.ensure_future(self.__to_console(msg))
        asyncio.ensure_future(self.__to_file(msg))
        asyncio.ensure_future(self.__to_server(msg))

    async def __make_message(self, identifier: str, content: Any, level: Level) -> str:
        """ Make message class, add to queue and do the logging algorithm

        :param identifier:
        :param content:
        :param level:
        :return str:
        """
        msg: Message = Message(identifier, content, level)
        asyncio.ensure_future(self.__add_to_queue(msg))
        asyncio.ensure_future(self.__log())

        return str(msg)

    async def __timer(self):
        while True:
            if len(self.__queue) >= 1:
                print("Running Logger...")
                asyncio.ensure_future(self.__log())
            else:
                print("Skipping...")

            await asyncio.sleep(1)

    async def __start(self) -> bool:
        print("Debugger Started !")
        try:
            asyncio.ensure_future(self.__timer())
        except:
            return False

        return True

    async def log(self, identifier: str, content: Any) -> str:
        """ Log, an additional information, remainders, records

        :param identifier:
        :param content:
        :return:
        """
        return await self.__make_message(identifier, content, Level.LOG)

    async def info(self, identifier: str, content: Any):
        """ Information, must know without any urgency

        :param identifier:
        :param content:
        :return:
        """
        return await self.__make_message(identifier, content, Level.INFO)

    async def success(self, identifier: str, content: Any):
        """ Success Information, process has ben sucessfully ran

        :param identifier:
        :param content:
        :return:
        """
        return await self.__make_message(identifier, content, Level.SUCCESS)

    async def warning(self, identifier: str, content: Any):
        """ Warning, process(es) encounter something that not suppose to happen, but still can be handled

        :param identifier:
        :param content:
        :return:
        """
        return await self.__make_message(identifier, content, Level.WARNING)

    async def error(self, identifier: str, content: Any):
        """ Warning, process(es) errored out, still can be handled, but urgently need an attention

        :param identifier:
        :param content:
        :return:
        """
        return await self.__make_message(identifier, content, Level.ERROR)

    async def critical(self, identifier: str, content: Any):
        """ Warning, process(es) errored out, program exit unexpectedly

        :param identifier:
        :param content:
        :return:
        """
        return await self.__make_message(identifier, content, Level.CRITICAL)
