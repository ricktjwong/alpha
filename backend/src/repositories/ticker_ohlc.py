""" Defines the TickerOHLC repository """

from sqlalchemy import asc

from models import TickerOHLC


class TickerOHLCRepository:
    """ The repository for the user model """

    @staticmethod
    def get_all_symbols():
        return (
            TickerOHLC.query.distinct(TickerOHLC.symbol)
            .with_entities(TickerOHLC.symbol)
            .all()
        )

    @staticmethod
    def get_by_tickers(symbols, datetime):
        """ Get history of tickers based on symbols """

        return (
            TickerOHLC.query.filter(TickerOHLC.datetime >= datetime)
            .filter(TickerOHLC.symbol.in_(symbols))
            .order_by(asc(TickerOHLC.datetime))
            .with_entities(TickerOHLC.symbol, TickerOHLC.adj_close)
            .all()
        )

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
