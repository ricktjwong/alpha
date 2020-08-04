import json
import unittest

from models import Ticker
from models.abc import db
from repositories import TickerRepository
from server import server


class TestTicker(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.client = server.test_client()

    def setUp(self):
        db.create_all()

    def tearDown(self):
        TickerRepository.drop()
        db.session.remove()
        db.drop_all()

    def test_get(self):
        """ The GET on `/user` should return an user """
        TickerRepository.create("Test1", 12345)
        response = self.client.get("/application/ticker")

        self.assertEqual(response.status_code, 200)
        response_json = json.loads(response.data.decode("utf-8"))
        self.assertEqual(response_json, {"tickers": ["Test1"]})
