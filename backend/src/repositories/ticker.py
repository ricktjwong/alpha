""" Defines the Ticker repository """

from models import Ticker


class TickerRepository:
    """ The repository for the user model """

    @staticmethod
    def get(symbol):
        """ Query a Ticker by symbol """
        return Ticker.query.filter_by(symbol=symbol).one()

    @staticmethod
    def get_all():
        """ Returns all Tickers """
        return Ticker.query.all()

    @staticmethod
    def create(symbol, mcap):
        """ Create a new Ticker """
        ticker = Ticker(symbol=symbol, mcap=mcap)

        return ticker.save()

    @staticmethod
    def drop():
        return Ticker.query.delete()
