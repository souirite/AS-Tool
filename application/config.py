class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'this-really-needs-to-be-changed'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'
    RECAPTCHA_PUBLIC_KEY = '6Lf5-cAUAAAAAFJLKWWBdqfaGFRvJEHwwnhxgbOY'
    RECAPTCHA_PRIVATE_KEY = '6Lf5-cAUAAAAAGpkp8dTiLpoi3Fy0NxP4ckwCaYQ'


class DevelopmentConfig(Config):
    DEBUG = True
    TESTING = True


class TestingConfig(Config):
    DEBUG = False
    TESTING = True
