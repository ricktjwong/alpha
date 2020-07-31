"""
Define the Ticker Covariance model
"""
from . import db
from .abc import BaseModel, MetaBaseModel


class TickerCovariance(db.Model, BaseModel, metaclass=MetaBaseModel):
    """ The Ticker Covariance model """

    __tablename__ = "ticker_covariance"

    symbol1 = db.Column(db.String(10), primary_key=True)
    symbol2 = db.Column(db.String(10), primary_key=True)
    covariance = db.Column(db.Float, nullable=False)

    def __init__(self, symbol1, symbol2, covariance):
        """ Create a new covariance relation """
        self.symbol1 = symbol1
        self.symbol2 = symbol2
        self.covariance = covariance
