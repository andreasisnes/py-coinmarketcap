# -*- coding: utf-8 -*-

import unittest
import pprint

from datetime import datetime
from context import coinmarketcap

pp = pprint.PrettyPrinter(indent=4).pprint


class TestCryptocurrency(unittest.TestCase):
    def setUp(self):
        self.sandbox = coinmarketcap.Client(sandbox=True).cryptocurrency

    def test_info_id(self):
        data_1 = self.sandbox.info.id(1)
        data_2 = self.sandbox.info.id("2")
        self.assertIsInstance(data_1, dict)
        self.assertIsInstance(data_2, dict)

        data_3 = self.sandbox.info.id([1, 2])
        data_4 = self.sandbox.info.id(["1", "2"])
        self.assertEqual(data_3["data"], data_4["data"])

    def test_info_symbol(self):
        data_1 = self.sandbox.info.symbol("BTC")
        data_2 = self.sandbox.info.symbol("ETH")
        self.assertIsInstance(data_1, dict)
        self.assertIsInstance(data_2, dict)

    def test_map_active_start(self):
        data_1 = self.sandbox.map.active_start()
        data_2 = self.sandbox.map.active_start(start=100, limit=200)
        self.assertIsInstance(data_1, dict)
        self.assertIsInstance(data_2, dict)
        self.assertEqual(len(data_1["data"]), 100)
        self.assertEqual(len(data_2["data"]), 200)

    def test_map_active_symbol(self):
        data_1 = self.sandbox.map.active_symbol("BTC")
        data_2 = self.sandbox.map.active_symbol(["BTC", "ETH"])
        self.assertEqual(len(data_1["data"]), 1)
        self.assertEqual(len(data_2["data"]), 2)
        self.assertIsInstance(data_1, dict)
        self.assertIsInstance(data_2, dict)

    def test_map_inactive(self):
        data = self.sandbox.map.inactive()
        self.assertIsInstance(data, dict)

    def test_listings_historical_start(self):
        # not implemented
        with self.assertRaises(NotImplementedError):
            self.sandbox.listings.historical_start()

    def test_listings_latest_start(self):
        data_1 = self.sandbox.listings.latest_start()
        data_2 = self.sandbox.listings.latest_start(start=100, limit=200)
        data_3 = self.sandbox.listings.latest_start(convert="EUR")
        data_4 = self.sandbox.listings.latest_start(sort="name")
        data_5 = self.sandbox.listings.latest_start(sort_dir="asc")
        data_6 = self.sandbox.listings.latest_start(cryptocurrency_type="tokens")

        self.assertIsInstance(data_1, dict)
        self.assertIsInstance(data_2, dict)
        self.assertIsInstance(data_3, dict)
        self.assertIsInstance(data_4, dict)
        self.assertIsInstance(data_5, dict)
        self.assertIsInstance(data_6, dict)

        self.assertEqual(len(data_1["data"]), 100)
        self.assertEqual(len(data_2["data"]), 200)
        self.assertEqual(len(data_3["data"]), 100)
        self.assertEqual(len(data_4["data"]), 100)
        self.assertEqual(len(data_5["data"]), 100)

    def test_pairs_id(self):
        data_1 = self.sandbox.pairs.id(1)
        data_2 = self.sandbox.pairs.id("2")

        self.assertIsInstance(data_1, dict)
        self.assertIsInstance(data_2, dict)

    def test_pairs_symbol(self):
        data = self.sandbox.pairs.symbol("BTC")
        self.assertIsInstance(data, dict)

    # Test ohlcv
    def test_ohlcv_historical_id(self):
        start = datetime.strptime("2018-12-20", "%Y-%m-%d")
        end = datetime.strptime("2018-12-21", "%Y-%m-%d")
        data_1 = self.sandbox.ohlcv.historical_id(1, start, end)

        start = datetime.strptime("2018-12-20", "%Y-%m-%d").timestamp()
        end = datetime.strptime("2018-12-21", "%Y-%m-%d").timestamp()
        data_2 = self.sandbox.ohlcv.historical_id("1", start, end)

        self.assertIsInstance(data_1["data"], dict)
        self.assertIsInstance(data_2["data"], dict)
        self.assertEqual(data_1["data"], data_2["data"])

    def test_ohlcv_historical_symbol(self):
        start = datetime.strptime("2018-12-20", "%Y-%m-%d")
        end = datetime.strptime("2018-12-21", "%Y-%m-%d")
        data = self.sandbox.ohlcv.historical_symbol("BTC", start, end)
        self.assertIsInstance(data["data"], dict)

        start = datetime.strptime("2018-12-20", "%Y-%m-%d").timestamp()
        end = datetime.strptime("2018-12-21", "%Y-%m-%d").timestamp()
        data = self.sandbox.ohlcv.historical_symbol("BTC", start, end)
        self.assertIsInstance(data["data"], dict)

    def test_ohlcv_latest_id(self):
        data_1 = self.sandbox.ohlcv.latest_id(1)
        data_2 = self.sandbox.ohlcv.latest_id([1, 2])
        data_3 = self.sandbox.ohlcv.latest_id([1, 2], convert=["USD", "EUR"])

        self.assertIsInstance(data_1["data"], dict)
        self.assertIsInstance(data_2["data"], dict)
        self.assertIsInstance(data_3["data"], dict)

        self.assertEqual(len(data_1["data"]), 1)
        self.assertEqual(len(data_2["data"]), 2)
        self.assertEqual(len(data_3["data"]["1"]["quote"]), 2)

    def test_ohlcv_latest_symbol(self):
        data_1 = self.sandbox.ohlcv.latest_symbol("BTC")
        data_2 = self.sandbox.ohlcv.latest_symbol(["BTC", "ETH"])
        data_3 = self.sandbox.ohlcv.latest_symbol(
            ["BTC", "ETH"], convert=["USD", "EUR"]
        )

        self.assertIsInstance(data_1["data"], dict)
        self.assertIsInstance(data_2["data"], dict)
        self.assertIsInstance(data_3["data"], dict)

        self.assertEqual(len(data_1["data"]), 1)
        self.assertEqual(len(data_2["data"]), 2)
        self.assertEqual(len(data_3["data"]["BTC"]["quote"]), 2)

    # Test Quotes
    def test_quotes_historical_id(self):
        start = datetime.strptime("2018-12-20", "%Y-%m-%d")
        end = datetime.strptime("2018-12-21", "%Y-%m-%d")
        data_1 = self.sandbox.quotes.historical_id(1, start, end)

        start = datetime.strptime("2018-12-20", "%Y-%m-%d").timestamp()
        end = datetime.strptime("2018-12-21", "%Y-%m-%d").timestamp()
        data_2 = self.sandbox.quotes.historical_id("1", start, end)

        self.assertIsInstance(data_1, dict)
        self.assertIsInstance(data_2, dict)
        self.assertEqual(data_1["data"], data_2["data"])

    def test_quotes_historical_symbol(self):
        start = datetime.strptime("2018-12-20", "%Y-%m-%d")
        end = datetime.strptime("2018-12-21", "%Y-%m-%d")
        data = self.sandbox.quotes.historical_symbol("BTC", start, end)
        self.assertIsInstance(data["data"], dict)

        start = datetime.strptime("2018-12-20", "%Y-%m-%d").timestamp()
        end = datetime.strptime("2018-12-21", "%Y-%m-%d").timestamp()
        data = self.sandbox.quotes.historical_symbol("BTC", start, end)
        self.assertIsInstance(data["data"], dict)

    def test_quotes_latest_id(self):
        data_1 = self.sandbox.quotes.latest_id(1)
        data_2 = self.sandbox.quotes.latest_id([1, 2])
        data_3 = self.sandbox.quotes.latest_id([1, 2], convert=["USD", "EUR"])

        self.assertIsInstance(data_1["data"], dict)
        self.assertIsInstance(data_2["data"], dict)
        self.assertIsInstance(data_3["data"], dict)

        self.assertEqual(len(data_1["data"]), 1)
        self.assertEqual(len(data_2["data"]), 2)
        self.assertEqual(len(data_3["data"]["1"]["quote"]), 2)

    def test_quotes_latest_symbol(self):
        data_1 = self.sandbox.quotes.latest_symbol("BTC")
        data_2 = self.sandbox.quotes.latest_symbol(["BTC", "ETH"])
        data_3 = self.sandbox.quotes.latest_symbol(
            ["BTC", "ETH"], convert=["USD", "EUR"]
        )

        self.assertIsInstance(data_1["data"], dict)
        self.assertIsInstance(data_2["data"], dict)
        self.assertIsInstance(data_3["data"], dict)

        self.assertEqual(len(data_1["data"]), 1)
        self.assertEqual(len(data_2["data"]), 2)
        self.assertEqual(len(data_3["data"]["BTC"]["quote"]), 2)


class TestExchange(unittest.TestCase):
    def setUp(self):
        self.sandbox = coinmarketcap.Client(sandbox=True).exchange

    def test_info_id(self):
        data_1 = self.sandbox.info.id(1)
        data_2 = self.sandbox.info.id("2")
        data_3 = self.sandbox.info.id([1, 2])

        self.assertIsInstance(data_1["data"], dict)
        self.assertIsInstance(data_2["data"], dict)
        self.assertIsInstance(data_3["data"], dict)

    def test_info_slug(self):
        data_1 = self.sandbox.info.slug("binance")
        data_2 = self.sandbox.info.slug("bittrex")
        data_3 = self.sandbox.info.slug(["binance", "bittrex"])

        self.assertIsInstance(data_1["data"], dict)
        self.assertIsInstance(data_2["data"], dict)
        self.assertIsInstance(data_3["data"], dict)

    def test_map_active_start(self):
        data_1 = self.sandbox.map.active_start()
        data_2 = self.sandbox.map.active_start(start=100, limit=200)

        self.assertIsInstance(data_1["data"], list)
        self.assertIsInstance(data_2["data"], list)
        self.assertGreater(len(data_2["data"]), len(data_1["data"]))

    def test_map_active_symbol(self):
        data_1 = self.sandbox.map.active_slug("binance")
        data_2 = self.sandbox.map.active_slug(["binance", "bittrex"])

        self.assertIsInstance(data_1["data"], list)
        self.assertIsInstance(data_2["data"], list)
        self.assertGreater(len(data_2["data"]), len(data_1["data"]))

    def test_map_inactive(self):
        data = self.sandbox.map.inactive()
        self.assertIsInstance(data["data"], list)

    def test_listings_historical_start(self):
        with self.assertRaises(NotImplementedError):
            self.sandbox.listings.historical_start()

    def test_listings_latest_start(self):
        data_1 = self.sandbox.listings.latest_start()
        data_2 = self.sandbox.listings.latest_start(limit=200, market_type="fees")

        self.assertIsInstance(data_1["data"], list)
        self.assertIsInstance(data_2["data"], list)
        self.assertGreater(len(data_2["data"]), len(data_1["data"]))

    def test_pairs_id(self):
        data = self.sandbox.pairs.id(1)
        self.assertIsInstance(data["data"]["market_pairs"], list)

    def test_pairs_slug(self):
        data = self.sandbox.pairs.slug("binance", limit=200)
        self.assertIsInstance(data["data"]["market_pairs"], list)

    def test_quotes_historical_id(self):
        start = datetime.strptime("2018-12-20", "%Y-%m-%d")
        end = datetime.strptime("2018-12-21", "%Y-%m-%d")
        data_1 = self.sandbox.quotes.historical_id(270, start, end)

        start = datetime.strptime("2018-12-20", "%Y-%m-%d").timestamp()
        end = datetime.strptime("2018-12-21", "%Y-%m-%d").timestamp()
        data_2 = self.sandbox.quotes.historical_id("270", start, end)

        self.assertIsInstance(data_1["data"], dict)
        self.assertIsInstance(data_2["data"], dict)
        self.assertEqual(data_1["data"], data_2["data"])

    def test_quotes_historical_slug(self):
        start = datetime.strptime("2018-12-20", "%Y-%m-%d")
        end = datetime.strptime("2018-12-21", "%Y-%m-%d")
        data_1 = self.sandbox.quotes.historical_slug("binance", start, end)

        start = datetime.strptime("2018-12-20", "%Y-%m-%d").timestamp()
        end = datetime.strptime("2018-12-21", "%Y-%m-%d").timestamp()
        data_2 = self.sandbox.quotes.historical_slug("binance", start, end)

        self.assertIsInstance(data_1["data"], dict)
        self.assertIsInstance(data_2["data"], dict)
        self.assertEqual(data_1["data"], data_2["data"])

    def test_quotes_latest_id(self):
        data_1 = self.sandbox.quotes.latest_id(270)
        data_2 = self.sandbox.quotes.latest_id([270, 22])
        data_3 = self.sandbox.quotes.latest_id([270, 22], convert=["USD", "EUR"])

        self.assertIsInstance(data_1["data"], dict)
        self.assertIsInstance(data_2["data"], dict)
        self.assertIsInstance(data_3["data"], dict)

        self.assertEqual(len(data_1["data"]), 1)
        self.assertEqual(len(data_2["data"]), 2)
        self.assertEqual(len(data_3["data"]["22"]["quote"]), 2)

    def test_quotes_latest_symbol(self):
        data_1 = self.sandbox.quotes.latest_slug("binance")
        data_2 = self.sandbox.quotes.latest_slug(["binance", "bittrex"])
        data_3 = self.sandbox.quotes.latest_slug(
            ["binance", "bittrex"], convert=["USD", "EUR"]
        )

        self.assertIsInstance(data_1["data"], dict)
        self.assertIsInstance(data_2["data"], dict)
        self.assertIsInstance(data_3["data"], dict)

        self.assertEqual(len(data_1["data"]), 1)
        self.assertEqual(len(data_2["data"]), 2)
        self.assertEqual(len(data_3["data"]["binance"]["quote"]), 2)
        self.assertEqual(len(data_3["data"]["bittrex"]["quote"]), 2)


class TestGlobalsMetrics(unittest.TestCase):
    def setUp(self):
        self.sandbox = coinmarketcap.Client(sandbox=True).global_metrics

    def test_quotes_historical(self):
        start = datetime.strptime("2018-12-20", "%Y-%m-%d").timestamp()
        end = datetime.strptime("2018-12-21", "%Y-%m-%d").timestamp()
        data = self.sandbox.quotes.historical(start, end)
        self.assertIsInstance(data["data"], dict)
        data = self.sandbox.quotes.historical()

    def latest(self):
        data = self.sandbox.quotes.latest(convert="EUR")
        self.assertIsInstance(data["data"], dict)


class TestTools(unittest.TestCase):
    def setUp(self):
        self.sandbox = coinmarketcap.Client(sandbox=True).tools

    def test_price_convert_id(self):
        time = datetime.strptime("2018-12-21", "%Y-%m-%d").timestamp()
        data = self.sandbox.price.convert_id(100, 1, time, convert="USD")
        self.assertIsInstance(data["data"], dict)

    def test_price_convert_symbol(self):
        time = datetime.strptime("2018-12-21", "%Y-%m-%d").timestamp()
        data = self.sandbox.price.convert_symbol(100, "BTC", time, convert="USD")
        self.assertIsInstance(data["data"], dict)


if __name__ == "__main__":
    unittest.main()
