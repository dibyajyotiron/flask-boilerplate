from typing import Any
from dataclasses import dataclass

@dataclass
class ErrorResponse:
    message: Any
    code: int
    description: str = ""
    extra: Any = None


@dataclass
class Response:
    error: Any
    result: Any
    success: bool
