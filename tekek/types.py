""" Tekek Enumeration and Static Types

@author: Erlangga Ibrahim
"""

from enum import Enum


class MethodType(Enum):
    """ Supported Method Type"""
    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    PATCH = "PATCH"
    DELETE = "DELETE"


class RequestBodyType(Enum):
    """ Supported Request Body Type Enumeration """
    FORM_DATA = "FORM_DATA"
    X_WWW_FORM_URLENCODED = "X_WWW_FORM_URLENCODED"
    JSON = "JSON"
    TEXT = "TEXT"
    JS = "JS"
    HTML = "HTML"
    XML = "XML"
    BINARY = "BINARY"
