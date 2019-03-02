# -*- coding: utf-8 -*-

from typing import Union
from datetime import datetime


class Parse:
    def args(self, **kwarg) -> dict:
        params = {}
        for method_name, arg in kwarg.items():
            try:
                params[method_name] = getattr(self, method_name)(arg)
            except AttributeError:
                continue
        return params

    def id(self, arg: Union[int, str, list]) -> int:
        if isinstance(arg, int) or isinstance(arg, str):
            return arg
        elif isinstance(arg, list):
            if all(isinstance(id, int) for id in arg):
                return ",".join(map(str, arg))
            if all(isinstance(id, str) for id in arg):
                return ",".join(arg)
            else:
                raise ValueError
        else:
            raise ValueError

    def symbol(self, arg: Union[str, list]) -> str:
        if isinstance(arg, str):
            return arg
        elif isinstance(arg, list):
            if all(isinstance(symbol, str) for symbol in arg):
                return ",".join(arg)
            else:
                raise ValueError
        else:
            raise ValueError

    def convert(self, arg: Union[str, list]) -> str:
        if isinstance(arg, str):
            return arg
        if isinstance(arg, list):
            if all(isinstance(slug, str) for slug in arg):
                return ",".join(arg)
            else:
                raise ValueError
        else:
            raise ValueError

    def start(self, arg: int) -> str:
        if isinstance(arg, int):
            return arg
        else:
            raise ValueError

    def limit(self, arg: int) -> str:
        if isinstance(arg, int):
            return arg
        else:
            raise ValueError

    def sort(self, arg: str) -> str:
        if isinstance(arg, str):
            return arg
        else:
            raise ValueError

    def sort_dir(self, arg: str) -> str:
        if isinstance(arg, str):
            return arg
        else:
            raise ValueError

    def cryptocurrency_type(self, arg: str) -> str:
        if isinstance(arg, str):
            return arg
        else:
            raise ValueError

    def time(self, arg: Union[datetime.datetime, float]) -> str:
        if isinstance(arg, datetime):
            return datetime.strftime("%Y-%m-%d")
        if isinstance(arg, float):
            return datetime.fromtimestamp(arg).strftime("%Y-%m-%d")
        else:
            raise ValueError

    def time_start(self, arg: Union[datetime.datetime, float]) -> str:
        return self.time(arg)

    def time_end(self, arg: Union[datetime, float]) -> str:
        return self.time(arg)

    def time_period(self, arg: str) -> str:
        if isinstance(arg, str):
            return arg
        else:
            raise ValueError

    def count(self, arg: int) -> int:
        if isinstance(arg, int):
            return arg
        else:
            raise ValueError

    def interval(self, arg: str) -> str:
        if isinstance(arg, str):
            return arg
        else:
            raise ValueError

    def slug(self, arg: Union[str, list]) -> str:
        if isinstance(arg, str):
            return arg
        elif isinstance(arg, list):
            if all(isinstance(slug, str) for slug in arg):
                return ",".join(arg)
            else:
                raise ValueError
        else:
            raise ValueError

    def market_type(self, arg: str) -> str:
        if isinstance(arg, str):
            return arg
        else:
            raise ValueError
