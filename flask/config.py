# -----------------------------------------------------------------
# This stores all the possible configurations for the Flask app.
#
# For variable configurations like the secret key or the database
# url, they should be stored as environment variables and imported
# using the 'os' library in Python.
# -----------------------------------------------------------------


import os


class BaseConfig:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY')
    DEBUG = False
    TESTING = False


class TestingConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_TEST_URL')
    DEBUG = True
    TESTING = True


class DevelopmentConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    DEBUG = True


class ProductionConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    DEBUG = False
