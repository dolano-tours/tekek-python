""" Tekek

client for sending debug message to debugger(tekek) server
"""

from .models import Record
from .models import LOG, DEBUG, INFO, WARNING, ERROR, EXCEPTION, CRITICAL
from .tekek import Tekek
