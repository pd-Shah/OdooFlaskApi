from os import environ


class Config:
    DEBUG = False
    TESTING = False


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
