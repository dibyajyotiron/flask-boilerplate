import flask
import json
from typing import Any
from enum import Enum

from dataclasses import asdict, is_dataclass
from . import datacontainers as dc

class AutoNameEnum(Enum):
    def _generate_next_value_(name, start, count, last_values):
        return name

    @classmethod
    def has(cls, value):
        return any(value == item.value for item in cls)

def success_response(result: Any) -> flask.Response:
    return dataclass_to_response(dc.Response(result=result, success=True, error=None))

def error_response(error: dc.ErrorResponse) -> flask.Response:
    return dataclass_to_response(dc.Response(result=None, success=False, error=error,))

def dataclass_to_response(data: dc.Response) -> flask.Response:
    return flask.Response(response=super_json(data), mimetype="application/json", status=200)

def super_json(obj) -> str:
    return json.dumps(obj, default=_serialize_all)

def _serialize_all(obj):
    if is_dataclass(obj):
        return asdict(obj)
    else:
        return str(obj)
