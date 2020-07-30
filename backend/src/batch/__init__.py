from flask_script import Command, Option
from flask_sqlalchemy import SQLAlchemy

from .download.download_ohlc import download_ohlc
from .seed.seed_ohlc import seed_ohlc
from .seed.seed_tickers import seed_tickers


class Batch(Command):
    option_list = (Option("--data", "-d", dest="data"),)

    def __init__(self, app, db):
        self.app = app
        self.db = db

    def run(self, data):
        if data == "seed_tickers":
            seed_tickers()
        elif data == "seed_ohlc":
            seed_ohlc(self.db)
        elif data == "download_ohlc":
            download_ohlc()
        else:
            print("Requested batch job not found.")
