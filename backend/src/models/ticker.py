"""
Define the Ticker model
"""
from . import db
from .abc import BaseModel, MetaBaseModel


class Ticker(db.Model, BaseModel, metaclass=MetaBaseModel):
    """ The User model """

    __tablename__ = "ticker"

    symbol = db.Column(db.String(10), primary_key=True)
    mcap = db.Column(db.BigInteger, nullable=False)

    def __init__(self, symbol, mcap):
        """ Create a new User """
        self.symbol = symbol
        self.mcap = mcap
