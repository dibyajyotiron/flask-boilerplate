import os

DEBUG = True
APP_NAME = os.environ.get("APP_NAME_DEVELOPMENT")
SECRET_KEY = os.environ.get("SECRET_KEY_DEVELOPMENT")
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
HOST = 'localhost'
PORT = int(os.environ.get('PORT', 5000))
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ECHO = True

DB_HOST = os.getenv("DB_HOST_DEVELOPMENT")
POSTGRES = {
    "user": os.environ.get("POSTGRES_USER_DEVELOPMENT", "postgres"),
    "pw": os.environ.get("POSTGRES_PW_DEVELOPMENT", ""),
    "host": os.environ.get("POSTGRES_HOST_DEVELOPMENT", DB_HOST),
    "port": os.environ.get("POSTGRES_PORT_DEVELOPMENT", 5432),
    "db": os.environ.get("POSTGRES_DB_DEVELOPMENT", "postgres"),
}
DB_URI = "postgres://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s" % POSTGRES
