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
        plan="free",
        expire=3600,
        sandbox=False,
        throttle=None,
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
        self._throttler = Throttler(plan, throttle, block)

    def request(self, urn, params):
        url = Request("GET", urljoin(self._url, urn), params=params).prepare().url
        # NOTE: race condition, but it should be harmless
        if self._session.cache.has_url(url):
            response = self._request_cache(url)
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
                raise response.raise_for_status()

    def _request_cache(self, url):
        return self._session.get(url)

    def _request_throttle(self, url):
        self._throttler.throttle()
        return self._session.get(url)

    @property
    def plan(self):
        return self._throttler.plan

    @plan.setter
    def plan(self, minute=0, daily=0, monthly=0):
        self._throttler.plan(minute, daily, monthly)
