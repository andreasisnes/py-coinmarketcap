# -*- coding: utf-8 -*-

from requests import Request
from json import loads
from os.path import join as urljoin
from requests.exceptions import HTTPError

# local
from .endpoints import Cryptocurrency, Exchange, GlobalMetrics, Tools
from .environment import Sandbox, Production, Throttler


class Client(Sandbox, Production):
    def __init__(
        self,
        apikey=None,
        plan="hobbyist",
        expire=3600,
        sandbox=False,
        throttle="monthly",
        block=True,
    ):
        if sandbox:
            Sandbox.__init__(self, apikey, expire)
        else:
            Production.__init__(self, apikey, expire)

        self.cryptocurrency = Cryptocurrency(self.request)
        self.global_metrics = GlobalMetrics(self.request)
        self.exchange = Exchange(self.request)
        self.tools = Tools(self.request)
        self.throttler = Throttler(plan, throttle, block)

    def request(self, urn, params):
        url = Request("GET", urljoin(self.url, urn), params=params).prepare().url
        # NOTE: race condition, but it should be harmless
        if self.session.cache.has_url(url):
            response = self._request(url)
        else:
            response = self._request_throttle(url)

        res = loads(response.text)
        if response.status_code == 200:
            res["cached"] = response.from_cache
            return res
        else:
            try:
                raise HTTPError(
                    "%d - %s" % (response.status_code, res["status"]["error_message"])
                )
            except KeyError:
                raise HTTPError(response.status_code)

    def _request(self, url):
        return self.session.get(url)

    def _request_throttle(self, url):
        self.throttler.throttle()
        return self.session.get(url)

    @property
    def plan(self):
        return self.throttler.plan

    @plan.setter
    def plan(self, minute=0, daily=0, monthly=0):
        self.throttler.plan(minute, daily, monthly)
