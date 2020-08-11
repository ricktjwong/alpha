import json
import unittest
from datetime import datetime

from models.abc import db
from repositories import TickerOHLCRepository
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

    def test_post(self):
        """ Tests the POST endpoint """

        date1 = datetime(1900, 1, 1)
        date2 = datetime(1900, 1, 2)
        date3 = datetime(1900, 1, 3)

        TickerOHLCRepository.create(date1, "symbol1", 0, 0, 0, 0, 0, 0)
        TickerOHLCRepository.create(date2, "symbol1", 0, 0, 0, 0, 1, 0)
        TickerOHLCRepository.create(date3, "symbol1", 0, 0, 0, 0, 2, 0)

        TickerOHLCRepository.create(date1, "symbol2", 0, 0, 0, 0, 0, 0)
        TickerOHLCRepository.create(date2, "symbol2", 0, 0, 0, 0, 1, 0)
        TickerOHLCRepository.create(date3, "symbol2", 0, 0, 0, 0, 2, 0)

        allocation = {"allocation": {"symbol1": 1 / 3, "symbol2": 2 / 3}}

        response = self.client.post(
            "/application/backtest",
            content_type="application/json",
            data=json.dumps(allocation),
        )
        self.assertEqual(response.status_code, 200)
        response_json = json.loads(response.data.decode("utf-8"))
        results_expected = {
            "results": {
                "returns": {
                    date1.strftime("%Y/%m/%d"): float(0),
                    date2.strftime("%Y/%m/%d"): float(1),
                    date3.strftime("%Y/%m/%d"): float(2),
                }
            }
        }
        self.assertEqual(response_json, results_expected)
