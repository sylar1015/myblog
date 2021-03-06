#!/usr/bin/env python3
#-*-coding:utf-8-*-

from flask import Flask
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_pagedown import PageDown
from flask_cache import Cache
from flask import request

app = Flask(__name__)
db = SQLAlchemy()
bootstrap = Bootstrap()
moment = Moment()
login_manager = LoginManager()
pagedown = PageDown()
cache = Cache()

def truncate_p(string):
    pos = string.find('<hr>')
    if pos < 0:
        return string
    return string[:pos]

def create_app(config):

    app.config.from_object(config)

    db.init_app(app)
    bootstrap.init_app(app)
    moment.init_app(app)
    pagedown.init_app(app)

    login_manager.session_protection = 'basic' #'strong'
    login_manager.login_view = 'login'
    #login_manager.anonymous_user = models.Guest
    login_manager.login_message = 'Please login to access this page'
    login_manager.login_message_category = "warning"
    login_manager.init_app(app)

    #cache
    cache.init_app(app)

    return app

def make_cache_key(*args, **kwargs):
    path = request.path
    args = str(hash(frozenset(request.args.items())))
    return (path + args).encode('utf-8')

from webapp import views
