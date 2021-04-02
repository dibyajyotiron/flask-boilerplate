from dotenv import load_dotenv
from os import environ

from src.app import create_app

from common.server_start_error import validate_before_server_start

load_dotenv()

FLASK_ENV = environ.get("FLASK_ENV")
validate_before_server_start(environ, FLASK_ENV)

app = create_app(f'config.{FLASK_ENV}')

if __name__ == '__main__':
    app.run(debug=True)
