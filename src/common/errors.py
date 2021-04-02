from enum import auto

from .util import AutoNameEnum
from .datacontainers import ErrorResponse


class ApiExceptionCodeEnum(AutoNameEnum):
    unknown = auto()
    auth_fail = auto()
    bad_request = auto()
    not_found = auto()

class ApiException(Exception):
    def __init__(self, message, code=ApiExceptionCodeEnum.unknown, description=None, extra=None):
        self.message = message
        self.code = code.value
        self.description = description
        self.extra = extra

    def to_dataclass(self):
        return ErrorResponse(message=self.message, code=self.code, description=self.description, extra=self.extra)
