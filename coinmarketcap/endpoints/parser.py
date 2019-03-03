# -*- coding: utf-8 -*-

from typing import Union
import datetime
import sys


def args(**kwarg) -> dict:
    params = {}
    for method_name, arg in kwarg.items():
        try:
            params[method_name] = getattr(sys.modules[__name__], method_name)(arg)
        except AttributeError:
            continue
    return params


def id(arg: Union[int, str, list]) -> int:
    if isinstance(arg, int) or isinstance(arg, str):
        return str(arg)
    elif isinstance(arg, list):
        if all(isinstance(id, int) for id in arg):
            return ",".join(map(str, arg))
        if all(isinstance(id, str) for id in arg):
            return ",".join(arg)
        else:
            raise ValueError
    else:
        raise ValueError


def symbol(arg: Union[str, list]) -> str:
    if isinstance(arg, str):
        return arg
    elif isinstance(arg, list):
        if all(isinstance(symbol, str) for symbol in arg):
            return ",".join(arg)
        else:
            raise ValueError
    else:
        raise ValueError


def convert(arg: Union[str, list]) -> str:
    if isinstance(arg, str):
        return arg
    if isinstance(arg, list):
        if all(isinstance(slug, str) for slug in arg):
            return ",".join(arg)
        else:
            raise ValueError
    else:
        raise ValueError


def start(arg: int) -> str:
    if isinstance(arg, int):
        return str(arg)
    else:
        raise ValueError


def limit(arg: int) -> str:
    if isinstance(arg, int):
        return str(arg)
    else:
        raise ValueError


def sort(arg: str) -> str:
    if isinstance(arg, str):
        return arg
    else:
        raise ValueError


def sort_dir(arg: str) -> str:
    if isinstance(arg, str):
        return arg
    else:
        raise ValueError


def cryptocurrency_type(arg: str) -> str:
    if isinstance(arg, str):
        return arg
    else:
        raise ValueError


def time(arg: Union[datetime.datetime, float]) -> str:
    if isinstance(arg, datetime.datetime):
        return datetime.datetime.strftime(arg, "%Y-%m-%d")
    if isinstance(arg, float):
        return datetime.datetime.strftime(datetime.datetime.fromtimestamp(arg),"%Y-%m-%d")
    else:
        raise ValueError


def time_start(arg: Union[datetime.datetime, float]) -> str:
    return time(arg)


def time_end(arg: Union[datetime.datetime, float]) -> str:
    return time(arg)


def time_period(arg: str) -> str:
    if isinstance(arg, str):
        return arg
    else:
        raise ValueError


def count(arg: int) -> int:
    if isinstance(arg, int):
        return str(arg)
    else:
        raise ValueError


def interval(arg: str) -> str:
    if isinstance(arg, str):
        return arg
    else:
        raise ValueError


def slug(arg: Union[str, list]) -> str:
    if isinstance(arg, str):
        return arg
    elif isinstance(arg, list):
        if all(isinstance(slug, str) for slug in arg):
            return ",".join(arg)
        else:
            raise ValueError
    else:
        raise ValueError


def market_type(arg: str) -> str:
    if isinstance(arg, str):
        return arg
    else:
        raise ValueError

def amount(arg: Union[float, int, str]) -> str:
    return str(arg)
