from enum import Enum


class MethodType(Enum):
    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    PATCH = "PATCH"
    DELETE = "DELETE"
    COPY = "COPY"
    HEAD = "HEAD"
    OPTIONS = "OPTIONS"
    LINK = "LINK"
    UNLINK = "UNLINK"
    PURGE = "PURGE"
    LOCK = "LOCK"
    UNLOCK = "UNLOCK"
    PROPFIND = "PROPFIND"
    VIEW = "VIEW"


class RequestBodyType(Enum):
    FORM_DATA = "FORM_DATA"
    X_WWW_FORM_URLENCODED = "X_WWW_FORM_URLENCODED"
    JSON = "JSON"
    TEXT = "TEXT"
    JS = "JS"
    HTML = "HTML"
    XML = "XML"
    BINARY = "BINARY"
