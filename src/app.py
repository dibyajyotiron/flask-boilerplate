import logging
from flask import Flask, request as req

from .common.errors import ApiException
from .common import error_handlers as eh
from .models import db

from .controllers import users

def create_app(config_filename):
    app = Flask(__name__)
    app.config.from_object(config_filename)
    app.register_blueprint(users.blueprint)

    app.logger.setLevel(logging.DEBUG)

    app.config['ERROR_404_HELP'] = False
    app.config['TRAP_HTTP_EXCEPTIONS'] = True

    app.config["SQLALCHEMY_DATABASE_URI"] = app.config.get("DB_URI")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = app.config.get("SQLALCHEMY_TRACK_MODIFICATIONS")
    app.config["SQLALCHEMY_ECHO"] = app.config.get("SQLALCHEMY_ECHO")

    db.init_app(app)

    app.register_error_handler(ApiException, eh.handle_api_exception)
    app.register_error_handler(400, eh.handle_bad_request_exception)
    app.register_error_handler(404, eh.handle_not_found_exception)
    app.register_error_handler(405, eh.handle_method_not_allowed_exception)
    app.register_error_handler(Exception, eh.handle_generic_exception)

    @app.after_request
    def log_response(resp):
        app.logger.info(f"{req.method} {req.url} {req.data}")
        return resp

    return app
