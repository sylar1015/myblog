#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import unittest
import sys
sys.path.append('../')
from webapp.models import *
from webapp import create_app, db
from config import config
from datetime import datetime

class ModelTestCase(unittest.TestCase):

    def test_init_category(self):
        app = create_app(config['default'])
        ctx = app.app_context()
        ctx.push()

        items = [ ('About', '/about'), ('Flask', '/flask'), ('Scraper', '/scraper')]

        for item in items:
            c = Category.query.filter_by(name=item[0]).first()
            if c:
                continue
            c = Category()
            c.name = item[0]
            c.link = item[1]
            db.session.add(c)
            db.session.commit()

        cs = Category.get_all()
        self.assertTrue(len(items) == len(items))

    def test_init_user(self):
        #app = create_app(config['default'])
        #ctx = app.app_context()
        #ctx.push()

        user = User.get_user('admin')
        if not user:
            user = User()
            user.username = 'admin'
            user.set_password('admin')
            db.session.add(user)
            db.session.commit()

        self.assertTrue(user.verify_password('admin'))

if __name__ == '__main__':
    unittest.main()
