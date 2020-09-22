from _io import TextIOWrapper
import sys


class Tekek:
    def __init__(
        self,
        name: str,

        console_logging: bool = True,
        console_file: TextIOWrapper = sys.stderr,

        remote_logging: bool = False,
        remote_path: str = "",

        file_logging: bool = False,
        file_path: str = ""
    ):
        self.name = name

        # --- CONSOLE --- #
        self.console_logging: bool = console_logging
        self.console_file: TextIOWrapper = console_file

        # --- REMOTE --- #
        self.remote_logging: bool = remote_logging
        self.remote_path: str = remote_path

        # --- FILE --- #
        self.file_logging: bool = file_logging
        self.file_path: str = file_path

    def disable_console(self):
        ...

    def enable_console(self):
        ...

    def disable_remote(self):
        ...

    def enable_remote(self):
        ...

    def disable_file(self):
        ...

    def enable_file(self):
        ...

    # --- Logging Methods --- #

    def log(self):
        ...

    def debug(self):
        ...

    def info(self):
        ...

    def warning(self):
        ...

    def error(self):