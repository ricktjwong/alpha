"""
Define the REST verbs relative to the tickers
"""

from flasgger import swag_from
from flask.json import jsonify
from flask_restful import Resource


class TickerResource(Resource):
    """ Verbs relative to the users """

    @staticmethod
    @swag_from("../swagger/ticker/GET.yml")
    def get():
        return jsonify({"tickers": ["abc", "def", "xyz"]})
