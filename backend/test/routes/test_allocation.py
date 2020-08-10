import json
import unittest

from models.abc import db
from repositories import TickerCovarianceRepository, TickerRepository
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

    def test_post(self):
        """ The POST on `/algorithm/allocation` should return an allocation """
        TickerRepository.create("symbol1", 10000)
        TickerRepository.create("symbol2", 20000)

        TickerCovarianceRepository.create("symbol1", "symbol1", 1)
        TickerCovarianceRepository.create("symbol2", "symbol2", 4)
        TickerCovarianceRepository.create("symbol1", "symbol2", 0)  # no correlation

        response = self.client.post(
            "/application/allocation",
            content_type="application/json",
            data=json.dumps({"stocks": ["symbol1", "symbol2"]}),
        )

        self.assertEqual(response.status_code, 200)
        response_json = json.loads(response.data.decode("utf-8"))
        allocation_expected = {"allocation": {"symbol1": 1 / 3, "symbol2": 2 / 3}}
        self.assertEqual(response_json, allocation_expected)
