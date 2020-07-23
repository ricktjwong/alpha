""" Defines the Ticker Covariance repository """

import sys

import numpy as np

from models import TickerCovariance


class TickerCovarianceRepository:
    @staticmethod
    def get_covariance_matrix(symbols):
        length = len(symbols)
        cov_mat = np.ndarray(shape=(length, length))
        for i in range(length):
            for j in range(i, length):
                covariance = TickerCovarianceRepository.get_covariance(
                    symbols[i], symbols[j]
                )
                cov_mat[i][j] = cov_mat[j][i] = covariance[0]
        return cov_mat

    @staticmethod
    def get_covariance(symbol1, symbol2):
        larger = max(symbol1, symbol2)
        smaller = min(symbol1, symbol2)
        return (
            TickerCovariance.query.filter(TickerCovariance.symbol1 == larger)
            .filter(TickerCovariance.symbol2 == smaller)
            .with_entities(TickerCovariance.covariance)
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
