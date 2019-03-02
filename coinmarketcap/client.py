# -*- coding: utf-8 -*-

from requests import Request
from json import loads
from os.path import join as urljoin

# local
from .endpoints import Cryptocurrency, Exchange, GlobalMetrics, Tools
from .environment import Sandbox, Production


class Client(Sandbox, Production):
    def __init__(self, apikey=None, expire=3600, sandbox=False):
        if sandbox:
            Sandbox.__init__(self, apikey, expire)
        else:
            Production.__init__(self, apikey, expire)

        self.cryptocurrency = Cryptocurrency(self.request)
        self.global_metrics = GlobalMetrics(self.request)
        self.exchange = Exchange(self.request)
        self.tools = Tools(self.request)

    def request(self, urn, params):
        url = Request("GET", urljoin(self.url, urn), params).prepare().url

        # NOTE: race condition, but it should be harmless
        if self.session.cache.has_url(url):
            response = self._request(url)
        else:
            response = self._request_throttle(url)

        if response.status_code == 200:
            res = loads(response.text)
            res["cached"] = response.from_cache
            return res
        else:
            response.raise_for_status

    def _request(self, url):
        return self.session.get(url)

    def _request_throttle(self, url):
        return self.session.get(url)
