from os import environ


class Config:
    DEBUG = False
    TESTING = False
    O_URL = 'http://192.168.4.6:8069'
    O_DB = 'Rakhshan2'
    SECRET_KEY = b'6hc/_gsh,./;2ZZx3c6_s,1//'


class ProductionConfig(Config):
    FLASK_ENV = "production"


class DevelopmentConfig(Config):
    DEBUG = True
    FLASK_ENV = 'development'


class TestingConfig(Config):
    TESTING = True


configs = {
    'development': 'settings.DevelopmentConfig',
    'testing': 'settings.TestConfig',
    'production': 'settings.ProductionConfig'
}

config = configs[environ.get("FLASK_ENV", default='production')]
