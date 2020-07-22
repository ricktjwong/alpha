"""
Define the Ticker model
"""
from . import db
from .abc import BaseModel, MetaBaseModel


class Ticker(db.Model, BaseModel, metaclass=MetaBaseModel):
    """ The User model """

    __tablename__ = "ticker"

    symbol = db.Column(db.String(10), primary_key=True)

    def __init__(self, symbol):
        """ Create a new User """
        self.symbol = symbol
