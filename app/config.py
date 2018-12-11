# -*- coding: utf-8 -*-
import os


class Config(object):
    SECRET_KEY = os.getenv('SECRET_KEY') or 'quaie_flask'
    APP_DIR = os.path.dirname(os.path.realpath(__file__))
    STATIC_DIR = os.path.join(APP_DIR, 'static')
    IMAGES_DIR = os.path.join(STATIC_DIR, 'images')


class DevConfig(Config):
    DEBUG = True


class TestConfig(Config):
    TESTING = True


class ProdConfig(Config):
    pass


config = {
    'default': DevConfig,
    'development': DevConfig,
    'test': TestConfig,
    'production': ProdConfig
}
