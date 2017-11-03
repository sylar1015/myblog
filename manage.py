#!/usr/bin/env python3

from flask_script import Manager
from flask_script.commands import Server, ShowUrls, Clean
from config import config
from webapp import db, create_app
from flask_migrate import Migrate, MigrateCommand

app = create_app(config['dev'])

manager = Manager(app)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)
manager.add_command('runserver', Server())
manager.add_command('showurls', ShowUrls())
manager.add_command('clean', Clean())

if __name__ == '__main__':
    manager.run()
