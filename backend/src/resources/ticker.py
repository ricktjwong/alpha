"""
Define the REST verbs relative to the tickers
"""

from flasgger import swag_from
from flask.json import jsonify
from flask_restful import Resource

from repositories import TickerRepository

class TickerResource(Resource):
    """ Verbs relative to the users """

    @staticmethod
    @swag_from("../swagger/ticker/GET.yml")
    def get():
        tickers = [ticker.json["symbol"] for ticker in TickerRepository.get_all()]
        return jsonify({"tickers": tickers})
