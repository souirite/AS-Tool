class Config(object):
    DEBUG = True
    TESTING = False
    SECRET_KEY= 'shouldbesecret'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'

class ProductionConfig(Config):
    DEBUG = False

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True