"""
Defines the route for the backtest
"""
from flask import Blueprint
from flask_restful import Api

from resources import BacktestResource

BACKTEST_BLUEPRINT = Blueprint("backtest", __name__)
Api(BACKTEST_BLUEPRINT).add_resource(BacktestResource, "/backtest")
