"""
Define the REST verbs relative to backtest
"""

import numpy as np
from flasgger import swag_from
from flask.json import jsonify
from flask_restful import Resource
from flask_restful.reqparse import Argument
from numpy import matmul

from repositories import TickerOHLCRepository
from util import parse_dict, parse_params


class BacktestResource(Resource):
    """ Verbs relative to the users """

    @staticmethod
    @parse_params(
        Argument(
            "allocation", location="json", required=True, help="Allocation of stocks."
        )
    )
    @swag_from("../swagger/backtest/POST.yml")
    def post(allocation):
        allocation = parse_dict(allocation)
        symbols = allocation.keys()

        start_date = TickerOHLCRepository.get_earliest_common_date(symbols)
        history, dates = TickerOHLCRepository.get_by_tickers(symbols, start_date)

        weight_vector = np.fromiter(allocation.values(), dtype=float)
        returns = matmul(weight_vector, history.to_numpy().T).tolist()

        results = {}
        for returnz, date in zip(returns, dates):
            results[date] = returnz

        return jsonify({"results": {"returns": results}})
