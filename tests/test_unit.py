# -*- coding: utf-8 -*-

import unittest
import os
import requests

from context import coinmarketcap
from pathlib import Path


class TestClient(unittest.TestCase):
    def setUp(self):
        temp_file = os.path.join(Path.home(), ".temp_coinmarketcap.json")
        keys_file = os.path.join(Path.home(), ".coinmarketcap.json")
        sand_env = os.environ["COINMARKETCAP_SANDBOX"]
        prod_env = os.environ["COINMARKETCAP_PRODUCTION"]

        # Test no keys
        os.rename(keys_file, temp_file)
        del os.environ["COINMARKETCAP_SANDBOX"]
        del os.environ["COINMARKETCAP_PRODUCTION"]
        with self.assertRaises(KeyError):
            production = coinmarketcap.Client()
        with self.assertRaises(KeyError):
            sandbox = coinmarketcap.Client(sandbox=True)

        # Test os env
        os.environ["COINMARKETCAP_SANDBOX"] = sand_env
        os.environ["COINMARKETCAP_PRODUCTION"] = prod_env
        production = coinmarketcap.Client()
        sandbox = coinmarketcap.Client(sandbox=True)
        self.assertIsInstance(production, coinmarketcap.client.Production)
        self.assertIsInstance(sandbox, coinmarketcap.client.Sandbox)

        # Test file
        os.rename(temp_file, keys_file)
        production = coinmarketcap.Client()
        sandbox = coinmarketcap.Client(sandbox=True)
        self.assertIsInstance(production, coinmarketcap.client.Production)
        self.assertIsInstance(sandbox, coinmarketcap.client.Sandbox)

        # Test key
        self.production = coinmarketcap.Client(apikey=prod_env)
        self.sandbox = coinmarketcap.Client(apikey=sand_env)
        self.assertIsInstance(production, coinmarketcap.client.Production)
        self.assertIsInstance(sandbox, coinmarketcap.client.Sandbox)

    def test_request(self):
        self.sandbox._session.cache.clear()
        urn = "cryptocurrency/listings/latest"

        # check if data is fresh
        data = self.sandbox.request(urn, {})
        self.assertIsInstance(data, dict)
        self.assertFalse(data["cached"])

        # check if data is cached
        data = self.sandbox.request(urn, {})
        self.assertIsInstance(data, dict)
        self.assertTrue(data["cached"])

        # check if exception is raised when wrong urn is given
        with self.assertRaises(requests.exceptions.HTTPError):
            self.sandbox.request("error", {})


if __name__ == "__main__":
    unittest.main()
