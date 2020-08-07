""" Defines the TickerOHLC repository """

from datetime import datetime

import pandas as pd
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
    def get_earliest_common_date(symbols):
        latest_date = datetime(1900, 1, 1)
        for symbol in symbols:
            current_date = (
                TickerOHLC.query.filter(TickerOHLC.symbol == symbol)
                .order_by(asc(TickerOHLC.datetime))
                .with_entities(TickerOHLC.datetime)
                .first()[0]
            )
            if current_date > latest_date:
                latest_date = current_date
        return latest_date

    @staticmethod
    def get_by_tickers(symbols, datetime):
        """ Get history of tickers based on symbols """
        results = (
            TickerOHLC.query.filter(TickerOHLC.datetime >= datetime)
            .filter(TickerOHLC.symbol.in_(symbols))
            .order_by(asc(TickerOHLC.datetime))
            .with_entities(TickerOHLC.symbol, TickerOHLC.adj_close, TickerOHLC.datetime)
            .all()
        )
        all_history = {}
        all_dates = set()
        for symbol in symbols:
            all_history[symbol] = []
        for row in results:
            all_history[row[0]].append(row[1])
            all_dates.add(row[2])

        df = pd.DataFrame(all_history)
        dates = list(all_dates)
        dates.sort(key=lambda date: date.timestamp())
        dates = [date.strftime("%Y/%m/%d") for date in dates] 
        return df, dates

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
