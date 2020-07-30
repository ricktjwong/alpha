"""
Define the Ticker OHLC model
"""
from . import db
from .abc import BaseModel, MetaBaseModel


class TickerOHLC(db.Model, BaseModel, metaclass=MetaBaseModel):
    """ The User model """

    __tablename__ = "ticker_ohlc"

    datetime = db.Column(db.DateTime, primary_key=True)
    symbol = db.Column(db.String(10), primary_key=True)
    openz = db.Column(db.Float, nullable=False)  # Open is keyword in python
    high = db.Column(db.Float, nullable=False)
    low = db.Column(db.Float, nullable=False)
    close = db.Column(db.Float, nullable=False)
    adj_close = db.Column(db.Float, nullable=False)
    volume = db.Column(db.BigInteger, nullable=False)

    def __init__(self, datetime, symbol, openz, high, low, close, adj_close, volume):
        """ Create a new User """
        self.datetime = datetime
        self.symbol = symbol
        self.openz = openz
        self.high = high
        self.low = low
        self.close = close
        self.adj_close = adj_close
        self.volume = volume
