"""
Define the REST verbs relative to backtest
"""

from flasgger import swag_from
from flask.json import jsonify
from flask_restful import Resource


class BacktestResource(Resource):
    """ Verbs relative to the users """

    @staticmethod
    @swag_from("../swagger/backtest/POST.yml")
    def post():
        return jsonify(
            {
                "results": {
                    "returns": [0.0, 1.0, -0.5, 2.0, 0.3, -1.0],
                    "ratios": {"alpha": 0.302010, "beta": 1.31},
                }
            }
        )
