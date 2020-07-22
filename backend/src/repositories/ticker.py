""" Defines the Ticker repository """

from models import Ticker


class TickerRepository:
    """ The repository for the user model """

    @staticmethod
    def get_all():
        """ Query a user by last and first name """
        return Ticker.query.all()

    @staticmethod
    def create(symbol, mcap):
        """ Create a new user """
        ticker = Ticker(symbol=symbol, mcap=mcap)

        return ticker.save()

    @staticmethod
    def drop():
        return Ticker.query.delete()
