# -*- coding: utf-8 -*-

import json

from .parser import Parse
from typing import Union
from os.path import join as urljoin


class Exchange:
    def __init__(self, request):
        self.request = request
        parse = Parse()
