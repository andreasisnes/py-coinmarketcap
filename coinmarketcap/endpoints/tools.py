# -*- coding: utf-8 -*-

from .parser import Parse
from typing import Union
from os.path import join as urljoin

class Price:
    def __init__(self, request, parse, endpoint):
        self.request = lambda x: request(urljoin(endpoint, "price-conversion"), parse(x))

    def convert_id(self, amount: [int, float], id: Union[str, int], time: Union[datetime, float], convert="USD"):
        return self.request(locals())

    def convert_symbol(self, amount: [int, float], symbol: str, time: Union[datetime, float], convert="USD"):
        return self.request(locals())

class Tools:
    def __init__(self, request):
        args = (request, Parse().args, "tools")
