# -*- coding: utf-8 -*-

from .parser import Parse
from typing import Union
from os.path import join as urljoin
import datetime


class Info:
    def __init__(self, request, parse, endpoint):
        self.request = lambda x: request(urljoin(endpoint, "info"), parse(x))

    def id(self, id: Union[list, str, int]):
        return self.request(locals())

    def slug(self, slug: Union[list, str]):
        return self.request(locals())


class Map:
    def __init__(self, request, parse, endpoint):
        self.parse = parse
        self.request = lambda x: request(urljoin(endpoint, "map"), x)

    def active_start(self, start=1, limit=100):
        return self.request(self.parse(locals()))

    def active_slug(self, slug: Union[list, str]):
        return self.request(self.parse(locals()))

    def inactive(self):
        return self.request({"listing_status": "inactive"})


class Listings:
    def __init__(self, request, parse, endpoint):
        self.request = lambda x, y: request(urljoin(endpoint, "listings", x), parse(y))

    def historical_start(self):
        raise NotImplementedError

    def latetest_start(
        self,
        start=1,
        limit=100,
        sort="volume_24h",
        sort_dir="desc",
        market_type="all",
        convert="USD",
    ):
        return self.request("latest", locals())


class Pairs:
    def __init__(self, request, parse, endpoint):
        self.request = lambda x: request(
            urljoin(endpoint, "market-pairs/latest"), parse(x)
        )

    def id(self, id: Union[list, str, int], convert="USD"):
        return self.request(locals())

    def slug(self, slug: Union[list, str], convert="USD"):
        return self.request(locals())

    def start(self, start=1, limit=100, convert="USD"):
        return self.request(locals())


class Quotes:
    def __init__(self, request, parse, endpoint):
        self.request = lambda x, y: request(urljoin(endpoint, "quotes", x), parse(y))

    def historical_id(
        self,
        id: Union[str, int],
        time_start: Union[datetime.datetime, float],
        time_end: Union[datetime.datetime, float],
        count=10,
        interval="5m",
        convert="USD",
    ):
        return self.request("historical", locals())

    def historical_slug(
        self,
        slug: str,
        time_start: Union[datetime.datetime, float],
        time_end: Union[datetime.datetime, float],
        count=10,
        interval="5m",
        convert="USD",
    ):
        return self.request("historical", locals())

    def latest_id(self, id: Union[list, str, int], convert="USD"):
        return self.request("latest", locals())

    def latest_slug(self, slug: Union[list, str], convert="USD"):
        return self.request("latest", locals())


class Exchange:
    def __init__(self, request):
        args = (request, Parse().args, "exchange")
        self.info = Info(*args)
        self.map = Map(*args)
        self.listings = Listings(*args)
        self.pairs = Pairs(*args)
        self.quotes = Quotes(*args)
