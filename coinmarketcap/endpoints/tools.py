# -*- coding: utf-8 -*-

from .parser import args
from typing import Union
from os.path import join as urljoin
import datetime


class Price:
    """ Convert an amount of one currency into multiple cryptocurrencies
    or fiat currencies at the same time using the latest market averages.
    Optionally pass a historical timestamp to convert values based on
    historic averages.
    """

    def __init__(self, request, endpoint):
        self.request = lambda x: request(
            urljoin(endpoint, "price-conversion"), args(**x)
        )

    def convert_id(
        self, amount: [int, float, str], id: Union[str, int], time=None, convert="USD"
    ):
        """
        Parameters
        ----------
        amount : `int`, `float` or `str`
            An amount of currency to convert. Example: 10.43
        id : `int` or `str`
            The CoinMarketCap currency ID of the base cryptocurrency or fiat
            to convert from. Example: "1"
        time : `int`, optional
            The number of interval periods to return results for. Optional,
            required if both "time_start" and "time_end" aren't supplied.
            The default is 10 items. The current query limit is 10000.
        time : `datetime.datetime` or `float`
            Timestamp (datetime obj or Unix) to reference historical pricing
            during conversion. If not passed, the current time will be used.
            If passed, we'll reference the closest historic values available
            for this conversion.
        convert : `str`, optional
            Calculate market quotes in up to 40 currencies at once. Each
            additional convert option beyond the first requires an additional
            call credit. Each conversion is returned in its own "quote"
            object. A list of supported fiat options can be found here.
            https://coinmarketcap.com/api/documentation/v1/#section/Standards-and-Conventions

        Returns
        -------
        `json obj`
            Schema - https://coinmarketcap.com/api/documentation/v1/#operation/getV1ToolsPriceconversion

        Raises
        ------
        ValueError
            If arguments is not parseable.

        requests.exceptions.HTTPError
            If status code is not 200
        """
        params = locals()
        if time is None:
            del params["time"]
        return self.request(params)

    def convert_symbol(
        self, amount: [int, float], symbol: str, time=None, convert="USD"
    ):
        """
        Parameters
        ----------
        amount : `int`, `float` or `str`
            An amount of currency to convert. Example: 10.43
        symbol : `str`
            Currency symbol of the base cryptocurrency or fiat to convert
            from. Example: "BTC".
        time : `int`, optional
            The number of interval periods to return results for. Optional,
            required if both "time_start" and "time_end" aren't supplied.
            The default is 10 items. The current query limit is 10000.
        time : `datetime.datetime` or `float`
            Timestamp (datetime obj or Unix) to reference historical pricing
            during conversion. If not passed, the current time will be used.
            If passed, we'll reference the closest historic values available
            for this conversion.
        convert : `str`, optional
            Calculate market quotes in up to 40 currencies at once. Each
            additional convert option beyond the first requires an additional
            call credit. Each conversion is returned in its own "quote"
            object. A list of supported fiat options can be found here.
            https://coinmarketcap.com/api/documentation/v1/#section/Standards-and-Conventions

        Returns
        -------
        `json obj`
            Schema - https://coinmarketcap.com/api/documentation/v1/#operation/getV1ToolsPriceconversion

        Raises
        ------
        ValueError
            If arguments is not parseable.

        requests.exceptions.HTTPError
            If status code is not 200
        """
        params = locals()
        if time is None:
            del params["time"]
        return self.request(params)


class Tools:
    """ API for convenience utilities. """

    def __init__(self, request):
        args = (request, "tools")
        self.price = Price(*args)
