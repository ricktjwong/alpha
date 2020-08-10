from flask_script import Command, Option
from flask_sqlalchemy import SQLAlchemy

from .download import download_ohlc
from .download import download_covariance
from .seed import seed_covariance, seed_tickers, prune_tickers


class Batch(Command):
    option_list = (Option("--data", "-d", dest="data"),)

    def __init__(self, app, db):
        self.app = app
        self.db = db

    def run(self, data):
        if data == "seed_tickers":
            seed_tickers()
        elif data == "prune_tickers":
            prune_tickers(self.db)
        elif data == "download_ohlc":
            download_ohlc()
        elif data == "download_covariance":
            download_covariance()
        else:
            print("Requested batch job not found.")
