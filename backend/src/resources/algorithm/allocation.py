"""
Define the REST verbs relative to the allocation
"""
import numpy as np
import pandas as pd
from flasgger import swag_from
from flask.json import jsonify
from flask_restful import Resource
from flask_restful.reqparse import Argument
from numpy import matmul
from numpy.linalg import inv

from repositories import TickerCovarianceRepository, TickerRepository
from util import parse_dict, parse_params

market_risk_premium = 0.056  # Magic number


class AllocationResource(Resource):
    """ Verbs relative to the users """

    @staticmethod
    @parse_params(
        Argument(
            "stocks",
            location="json",
            required=True,
            help="Array of stocks intended to invest in.",
        ),
        Argument(
            "views",
            location="json",
            required=False,
            help="Dictionary of views held by investor.",
        ),
    )
    @swag_from("../../swagger/algorithm/allocation/POST.yml")
    def post(stocks, views):
        stocks = parse_dict(stocks)
        allocation = get_allocation(stocks)
        return jsonify({"allocation": allocation})


def get_allocation(stocks):
    cov_mat = TickerCovarianceRepository.get_covariance_matrix(stocks)
    market_cap_total = 0
    market_cap = {}
    for stock in stocks:
        current_mcap = TickerRepository.get(stock).mcap
        market_cap[stock] = current_mcap
        market_cap_total += current_mcap
    for stock in stocks:
        market_cap[stock] /= market_cap_total

    market_cap = pd.Series(market_cap)

    cov_mat = pd.DataFrame(cov_mat)
    cov_mat.columns = stocks
    cov_mat.set_index(pd.Index(stocks))
    cov_mat.index = cov_mat.columns

    implied_returns = market_risk_premium * cov_mat.dot(market_cap)

    # https://quant.stackexchange.com/questions/8594/derivation-of-the-tangency-maximum-sharpe-ratio-portfolio-in-markowitz-portfol
    inverse = inv(cov_mat)

    ones_inv_sigma = matmul(np.ones(len(stocks)), inv(cov_mat))  # 𝜄inv(Σ)
    ones_inv_sigma_mu = matmul(ones_inv_sigma, implied_returns.T)  # 𝜄inv(Σ)𝜇
    inv_sigma_mu = matmul(inverse, implied_returns.T)  # inv(Σ)𝜇
    max_sharpe_alloc = inv_sigma_mu / ones_inv_sigma_mu  # inv(Σ)𝜇 / 𝜄inv(Σ)𝜇

    allocation = {}
    for symbol, alloc in zip(stocks, max_sharpe_alloc):
        allocation[symbol] = alloc

    return allocation
