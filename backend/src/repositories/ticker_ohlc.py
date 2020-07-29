""" Defines the TickerOHLC repository """

from models import TickerOHLC


class TickerOHLCRepository:
    """ The repository for the user model """

    @staticmethod
    def get_by_tickers(symbols):
        """ Get history of tickers based on symbols """

        return TickerOHLC.query.filter_by(TickerOHLC.symbol in symbols).all()

    @staticmethod
    def create(datetime, symbol, openz, high, low, close, volume):
        """ Create a new user """
        ticker = TickerOHLC(
            datetime=datetime,
            symbol=symbol,
            openz=openz,
            high=high,
            low=low,
            close=close,
            adj_close=adj_close,
            volume=volume,
        )
        return ticker.save()

    @staticmethod
    def drop():
        return TickerOHLC.query.delete()
