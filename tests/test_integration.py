# -*- coding: utf-8 -*-

import unittest

from context import coinmarketcap


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

    @unittest.skip("map")
    def test_map_active_symbol(self):
        pass

    @unittest.skip("map")
    def test_map_inactive(self):
        pass

    @unittest.skip("listings")
    def test_listings_historical_start(self):
        pass

    @unittest.skip("listings")
    def test_listings_latest_start(self):
        pass

    @unittest.skip("pairs")
    def test_pairs_id(self):
        pass

    @unittest.skip("pairs")
    def test_pairs_symbol(self):
        pass

    @unittest.skip("pairs")
    def test_pairs_start(self):
        pass

    @unittest.skip("ohlcv")
    def test_ohlcv_historical_id(self):
        pass

    @unittest.skip("ohlcv")
    def test_ohlcv_historical_symbol(self):
        pass

    @unittest.skip("ohlcv")
    def test_ohlcv_latest_id(self):
        pass

    @unittest.skip("ohlcv")
    def test_ohlcv_latest_symbol(self):
        pass

    @unittest.skip("quotes")
    def test_quotes_historical_id(self):
        pass

    @unittest.skip("quotes")
    def test_quotes_historical_symbol(self):
        pass

    @unittest.skip("quotes")
    def test_quotes_latest_id(self):
        pass

    @unittest.skip("quotes")
    def test_quotes_latest_symbol(self):
        pass


class TestExchange(unittest.TestCase):
    def setUp(self):
        self.sandbox = coinmarketcap.Client(sandbox=True).exchange


class TestGlobalsMetrics(unittest.TestCase):
    def setUp(self):
        self.sandbox = coinmarketcap.Client(sandbox=True).global_metrics


class TestTools(unittest.TestCase):
    def setUp(self):
        self.sandbox = coinmarketcap.Client(sandbox=True).tools


if __name__ == "__main__":
    unittest.main()
