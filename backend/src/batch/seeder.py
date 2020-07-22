from flask_script import Command, Option

from .populate_tickers import populate_tickers


class Seeder(Command):
    option_list = (Option("--data", "-d", dest="data"),)

    def __init__(self, app, db):
        self.app = app
        self.db = db

    def run(self, data):
        if data == "ticker":
            populate_tickers()
        else:
            print("Data requested for seed not found.")
