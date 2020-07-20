"""
Defines the route for the allocation
"""
from flask import Blueprint
from flask_restful import Api

from resources import AllocationResource

ALLOCATION_BLUEPRINT = Blueprint("allocation", __name__)
Api(ALLOCATION_BLUEPRINT).add_resource(AllocationResource, "/allocation")
