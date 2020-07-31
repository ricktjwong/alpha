""" Defines the Ticker Covariance repository """

from models import TickerCovariance


class TickerCovarianceRepository:
    @staticmethod
    def get_covariance(symbol1, symbol2):
        larger = max(symbol1, symbol2)
        smaller = min(symbol1, symbol2)
        return (
            TickerCovariance.query.filter(TickerCovariance.symbol1 == larger)
            .filter(TickerCovariance.symbol2 == smaller)
            .one()
        )

    @staticmethod
    def create(symbol1, symbol2, covariance):
        larger = max(symbol1, symbol2)
        smaller = min(symbol1, symbol2)
        ticker_cov = TickerCovariance(larger, smaller, covariance)
        return ticker_cov.save()

    @staticmethod
    def drop():
        return TickerCovariance.query.delete()
