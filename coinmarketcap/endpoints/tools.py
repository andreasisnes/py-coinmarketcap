# -*- coding: utf-8 -*-

from .parser import args
from typing import Union
from os.path import join as urljoin
import datetime


class Price:
    def __init__(self, request, endpoint):
        self.request = lambda x: request(urljoin(endpoint, "price-conversion"), args(**x))

    def convert_id(
        self,
        amount: [int, float],
        id: Union[str, int],
        time: Union[datetime.datetime, float],
        convert="USD",
    ):
        return self.request(locals())

    def convert_symbol(
        self,
        amount: [int, float],
        symbol: str,
        time: Union[datetime.datetime, float],
        convert="USD",
    ):
        return self.request(locals())


class Tools:
    def __init__(self, request):
        args = (request, "tools")
        self.price = Price(*args)
