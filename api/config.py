import os

import dotenv

DEFAULTS = {
    'CHECK_UPDATE_URL': '',
    'HOSTED_FETCH_APP_TEMPLATES_MODE': 'builtin',
}


def get_env(key):
    return os.environ.get(key, DEFAULTS.get(key))


def get_bool_env(key):
    value = get_env(key)
    return value.lower() == 'true' if value is not None else False


def get_cors_allow_origins(env, default):
    cors_allow_origins = []
    if get_env(env):
        for origin in get_env(env).split(','):
            cors_allow_origins.append(origin)
    else:
        cors_allow_origins = [default]

    return cors_allow_origins


class Config:
    """Application configuration class."""

    def __init__(self):
        dotenv.load_dotenv()

        self.TESTING = False

        # cors settings
        self.CONSOLE_CORS_ALLOW_ORIGINS = get_cors_allow_origins(
            'CONSOLE_CORS_ALLOW_ORIGINS', get_env('CONSOLE_WEB_URL'))
        self.WEB_API_CORS_ALLOW_ORIGINS = get_cors_allow_origins(
            'WEB_API_CORS_ALLOW_ORIGINS', '*')
        self.CUSTOM_CLIENT_ID = get_env('CUSTOM_CLIENT_ID')
        self.CUSTOM_CLIENT_SECRET = get_env('CUSTOM_CLIENT_SECRET')
        self.CUSTOM_HOST = get_env('CUSTOM_HOST')

