import os


class BaseConfig:
    DEBUG = False
    TESTING = False
    USE_RELOADER = False


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    TESTING = False
    USE_RELOADER = True
    SECRET = os.getenv("SECRET_EXAMPLE", "default-secret")


class ProductionConfig(BaseConfig):
    DEBUG = False
    TESTING = False
    USE_RELOADER = False


class TestingConfig(BaseConfig):
    TESTING = True
    DEBUG = False
    USE_RELOADER = False
