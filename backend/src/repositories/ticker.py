""" Defines the Ticker repository """

from models import Ticker


class TickerRepository:
    """ The repository for the user model """

    @staticmethod
    def get_all():
        """ Query a user by last and first name """
        return Ticker.query.all()

    @staticmethod
    def create(symbol):
        """ Create a new user """
        ticker = Ticker(symbol=symbol)

        return ticker.save()

    @staticmethod
    def drop():
        return Ticker.query.delete()
