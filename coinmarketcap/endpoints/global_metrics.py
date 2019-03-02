# -*- coding: utf-8 -*-

from .parser import Parse
from typing import Union
from os.path import join as urljoin
import datetime


class Quotes:
    def __init__(self, request, parse, endpoint):
        self.request = lambda x, y: request(urljoin("quotes", x), parse(y))

    def historical(
        self,
        time_start: Union[datetime.datetime, float],
        time_end: Union[datetime.datetime, float],
        count=10,
        interval="1d",
        convert="USD",
    ):
        return self.request("historical", locals())

    def latest(self, convert="USD"):
        return self.request("latest", locals())


class GlobalMetrics:
    def __init__(self, request):
        args = (request, Parse().args, "global-metrics")
        self.quotes = Quotes(*args)
