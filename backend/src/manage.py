from flask import Flask
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

import config
from batch import Batch
from models import db

server = Flask(__name__)
server.debug = config.DEBUG
server.config["SQLALCHEMY_DATABASE_URI"] = config.DB_URI
server.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
server.config["SQLALCHEMY_POOL_RECYCLE"] = 2000
db.init_app(server)

migrate = Migrate(server, db)
manager = Manager(server)

batch = Batch(server, db)

manager.add_command("db", MigrateCommand)
manager.add_command("batch", batch)

if __name__ == "__main__":
    manager.run()
