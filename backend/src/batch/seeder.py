from flask_script import Command, Option

from .populate_symbols import populate_symbols


class Seeder(Command):
    option_list = (Option("--data", "-d", dest="data"),)

    def __init__(self, app, db):
        self.app = app
        self.db = db

    def run(self, data):
        if data == "symbol":
            populate_symbols()
        else:
            print("Data requested for seed not found.")
