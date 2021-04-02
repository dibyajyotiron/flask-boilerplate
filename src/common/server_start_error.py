# Don't import this anywhere else other than run.py file
import os  # imported for denoting type of var

def generate_server_run_error_message(ENV: str):
    return f"Please set {ENV} in .env file before running the application... Check config.py to verify var name."


def validate_before_server_start(environ, env_name):
    """
    Before the server runs, validate if the most important environment variables exist.
    Args:
        environ (os.environ)
        env_name (str)
    """
    if not env_name:
        raise Exception(generate_server_run_error_message("FLASK_ENV"))
    if not environ.get(f"APP_NAME_{env_name.upper()}"):
        raise Exception(generate_server_run_error_message(f"APP_NAME_{env_name.upper()}"))
    if not environ.get(f"SECRET_KEY_{env_name.upper()}"):
        raise Exception(generate_server_run_error_message(f"SECRET_KEY_{env_name.upper()}"))
    return
