#!/usr/bin/env python3
#-*-coding:utf-8-*-

import os

class WebConfig:

    CSRF_ENABLED = True
    SECRET_KEY = 'you-will-never-guess'

    def init_app(self, app):
        pass

class DevConfig(WebConfig):

    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    basedir = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'dev.db')

class ProductConfig(WebConfig):

    SQLALCHEMY_TRACK_MODIFICATIONS = True

config = {

    'dev': DevConfig,
    'product' : ProductConfig,
    'default' : DevConfig,
}
