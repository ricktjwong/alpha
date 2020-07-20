"""
Defines the route for the tickers
"""
from flask import Blueprint
from flask_restful import Api

from resources import TickerResource

TICKER_BLUEPRINT = Blueprint("ticker", __name__)
Api(TICKER_BLUEPRINT).add_resource(TickerResource, "/ticker")
