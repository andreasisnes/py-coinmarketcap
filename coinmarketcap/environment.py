# -*- coding: utf-8 -*-

from os.path import join
from pathlib import Path
from tempfile import gettempdir
from requests_cache.core import CachedSession as session
from json import load
from os import environ

FILE = ".coinmarketcap.json"


class Session:
    def __init__(self, apikey, expire, cf):
        self.session = session(cf, "sqlite", expire)
        self.session.headers.update({"X-CMC_PRO_API_KEY": apikey})
        self.session.headers.update({"Accept": "application/json"})
        self.session.headers.update({"Accept-Encoding": "deflate, gzip"})


class Sandbox(Session):
    url = "https://sandbox-api.coinmarketcap.com/v1/"

    def __init__(self, apikey, expire):
        cf = join(gettempdir(), "CoinMarketCap_sandbox")
        if apikey is None:
            try:
                with open(join(Path.home(), FILE), "r") as fp:
                    keys = load(fp)
                apikey = keys["sandbox"]

            except FileNotFoundError:
                try:
                    apikey = environ["COINMARKETCAP_SANDBOX"]
                except KeyError:
                    raise KeyError("Can not locate key.")

        Session.__init__(self, apikey, expire, cf)


class Production(Session):
    url = "https://pro-api.coinmarketcap.com/v1"

    def __init__(self, apikey, expire):
        cf = join(gettempdir(), "CoinMarketCap_production")
        if apikey is None:
            try:
                with open(join(Path.home(), FILE), "r") as fp:
                    keys = load(fp)
                apikey = keys["production"]

            except FileNotFoundError:
                try:
                    apikey = environ["COINMARKETCAP_PRODUCTION"]
                except KeyError:
                    raise KeyError("Can not locate key.")

        Session.__init__(self, apikey, expire, cf)
