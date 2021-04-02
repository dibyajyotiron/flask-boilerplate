import logging

from flask import request

from .datacontainers import ErrorResponse
from .util import error_response

log = logging.getLogger(__name__)

def get_error_extra_data(error):
    return {
        'error_class': error.__class__.__qualname__
    }

def handle_api_exception(error):
    return error_response(error.to_dataclass())

def handle_bad_request_exception(error):
    log.info(error, exc_info=True)
    if hasattr(error, 'data'):
        message = error.data.get("message")
    else:
        message = ""
    error_resp = ErrorResponse(
        message=message,
        code=400,
        description=error.description
    )
    return error_response(error_resp), 400

def handle_not_found_exception(error):
    log.info("{} - path - {}".format(error, request.full_path), exc_info=True)
    error_resp = ErrorResponse(message=error.description, code=404,
                               description=error.description, extra=request.path)
    return error_response(error_resp)

def handle_method_not_allowed_exception(error):
    log.info(error, exc_info=True)
    error_resp = ErrorResponse(message="Method not allowed", code=405)
    return error_response(error_resp), 405

def handle_generic_exception(error):
    dependency_error_invoker = getattr(error, 'invoker', None)
    extra = dict(dependency_error_invoker=getattr(error, 'invoker', None)) if dependency_error_invoker else dict()
    log.error(error, exc_info=True, extra=extra)
    error_resp = ErrorResponse(message="Internal Server Error", code=500)
    return error_response(error_resp), 500
