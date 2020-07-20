"""
Define the REST verbs relative to the allocation
"""

from flasgger import swag_from
from flask.json import jsonify
from flask_restful import Resource


class AllocationResource(Resource):
    """ Verbs relative to the users """

    @staticmethod
    @swag_from("../../swagger/algorithm/allocation/POST.yml")
    def post():
        return jsonify({"allocation": {"AMZN": "0.2", "FB": "0.3", "GOOG": "0.5"}})
