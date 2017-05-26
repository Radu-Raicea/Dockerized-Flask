class BaseConfig(object):
    NAME = "FLASK-START"
    THREADED = True
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:postgres@postgres/my_db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProdConfig(BaseConfig):
    DEBUG = False

class DevConfig(BaseConfig):
    DEBUG = True
