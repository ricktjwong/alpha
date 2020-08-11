'''
import json
import unittest

from models import Ticker
from models.abc import db
from server import server


class TestExampleRoute(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.client = server.test_client()

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_get(self):
        """ The GET on `/example` should return "Hello World" """
        response = self.client.get("/application/example")

        self.assertEqual(response.status_code, 200)
        response_json = json.loads(response.data.decode("utf-8"))
        self.assertEqual(response_json, {"example": "Hello World"})

    def test_post(self):
        """ Tests the POST endpoint """
        response = self.client.post(
            "/application/example/Doe/John",
            content_type="application/json",
            data=json.dumps({"age": 30}),
        )

    def test_put(self):
        """ Tests the PUT endpoint """
        response = self.client.put(
            "/application/example/Doe/John",
            content_type="application/json",
            data=json.dumps({"age": 30}),
        )
'''
