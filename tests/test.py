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

        items = Category.get_all()
        if not items:
            item = Category()
            item.name = 'About'
            item.link = '/about'
            db.session.add(item)
            db.session.commit()

            item = Category()
            item.name = 'Flask'
            item.link = '/flask'
            db.session.add(item)
            db.session.commit()

            item = Category()
            item.name = 'Scraper'
            item.link = '/scraper'
            db.session.add(item)
            db.session.commit()

        items = Category.get_all()
        self.assertTrue(len(items) == 3)

if __name__ == '__main__':
    unittest.main()
