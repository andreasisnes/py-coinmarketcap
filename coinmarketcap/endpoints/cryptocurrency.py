# -*- coding: utf-8 -*-

from os.path import join as urljoin
from typing import Union
import datetime

# local
from .parser import args


class Info:
    """ Get metadata by CoinMarketCap ID

    Returns all static metadata for one or more cryptocurrencies including
    name, symbol, logo, and its various registered URLs.

    Cache / Update frequency: Static data is updated only as needed, every 30
    seconds. Plan credit use: 1 call credit per 100 cryptocurrencies returned
    (rounded up).
    """

    def __init__(self, request, endpoint):
        self.request = lambda x: request(urljoin(endpoint, "info"), args(**x))

    def id(self, id: Union[list, str, int]):
        """
        Parameters
        ----------
        id : [list, str, int]
            One or a list of CoinMarketCap cryptocurrency IDs. Example: "1,2"

        Returns
        -------
        json object
            Respone schema - https://coinmarketcap.com/api/documentation/v1/#operation/getV1CryptocurrencyInfo
        """
        return self.request(locals())

    def symbol(self, symbol: Union[list, str]):
        """
        Parameters
        ----------
        symbol : [list, str]
            One or a list of cryptocurrency symbols. Example: "BTC,ETH".

        Returns
        -------
        json object
            Respone schema - https://coinmarketcap.com/api/documentation/v1/#operation/getV1CryptocurrencyInfo
        """
        return self.request(locals())


class Map:
    """
    Returns a paginated list of all cryptocurrencies by CoinMarketCap ID. We
    recommend using this convenience endpoint to lookup and utilize our unique
    cryptocurrency id across all endpoints as typical identifiers like ticker
    symbols can match multiple cryptocurrencies and change over time. As a
    convenience you may pass a comma-separated list of cryptocurrency symbols
    as symbol to filter this list to only those you require.

    Cache / Update frequency: Mapping data is updated only as needed, every 30
    seconds. Plan credit use: 1 call credit per call. CMC equivalent pages: No
    equivalent, this data is only available via API.
    """

    def __init__(self, request, endpoint):
        self.request = lambda x: request(urljoin(endpoint, "map"), x)

    def active_start(self, start=1, limit=100):
        """
        Parameters
        ----------
        start : int >= 1
            Optionally offset the start (1-based index) of the paginated list
            of items to return.
        limit : int [ 1 .. 5000 ]
            Optionally specify the number of results to return. Use this
            parameter and the "start" parameter to determine your own
            pagination size.

        Returns
        -------
        json object
            Respone schema - https://coinmarketcap.com/api/documentation/v1/#operation/getV1CryptocurrencyMap
        """
        return self.request(args(**locals()))

    def active_symbol(self, symbol: Union[list, str]):
        """
        Parameters
        ----------
        symbol : [list, str]
            One or a list of cryptocurrency symbols. Example: "BTC,ETH".

        Returns
        -------
        json object
            Respone schema - https://coinmarketcap.com/api/documentation/v1/#operation/getV1CryptocurrencyMap
        """
        return self.request(args(**locals()))

    def inactive(self):
        """
        Returns
        -------
        json object
            Respone schema - https://coinmarketcap.com/api/documentation/v1/#operation/getV1CryptocurrencyMap
        """
        return self.request({"listing_status": "inactive"})


class Listings:
    """ List all cryptocurrencies

    Get a paginated list of all cryptocurrencies with latest market data.
    You can configure this call to sort by market cap or another market
    ranking field. Use the "convert" option to return market values in
    multiple fiat and cryptocurrency conversions in the same call.

    Cache / Update frequency: Every ~1 minute.
    Plan credit use: 1 call credit per 200 cryptocurrencies returned
    (rounded up) and 1 call credit per convert option beyond the first.
    """

    def __init__(self, request, endpoint):
        self.request = lambda x, y: request(urljoin(endpoint, "listings", x), args(**y))

    def historical_start(self):
        raise NotImplementedError

    def latest_start(
        self,
        start=1,
        limit=100,
        convert="USD",
        sort="market_cap",
        sort_dir="desc",
        cryptocurrency_type="all",
    ):
        """
        Parameters
        ----------
        start : int, 1 (default), >= 1
            Optionally offset the start (1-based index) of the paginated list
            of items to return.
        limit : int, 100 (default), [ 1 .. 5000 ]
            Optionally specify the number of results to return. Use this
            parameter and the "start" parameter to determine your own
            pagination size.
         convert : [str, list], "USD" (default)
            Optionally calculate market quotes in up to 40 currencies at once
            by passing a list of cryptocurrency or fiat currency symbols.
            Each additional convert option beyond the first requires an
            additional call credit. Each conversion is returned in its own
            "quote" object. A list of supported fiat options can be
            found here https://coinmarketcap.com/api/documentation/v1/#section/Standards-and-Conventions.
        sort : str, "market_cap" (default)
            What field to sort the list of cryptocurrencies by. Valid values:
            "name", "symbol", "date_added", "market_cap", "price",
            "circulating_supply", "total_supply", "max_supply",
            "num_market_pairs", "volume_24h", "percent_change_1h",
            "percent_change_24h", "percent_change_7d"
        sort_dir : str, "desc" (default)
            The direction in which to order cryptocurrencies against the
            specified sort. Valid values "asc" and "desc".
        cryptocurrency_type : str, "all" (default)
            The type of cryptocurrency to include. Valid values are "all",
            "coins", and "tokens"

        Returns
        -------
        json object
            Respone schema - https://coinmarketcap.com/api/documentation/v1/#operation/getV1CryptocurrencyListingsLatest
        """
        return self.request("latest", locals())


class Pairs:
    """ Get market pairs (latest)

    Lists all market pairs across all exchanges for the specified
    cryptocurrency with associated stats. Use the "convert" option
    to return market values in multiple fiat and cryptocurrency
    conversions in the same call.

    Cache / Update frequency: Every 1 minute.
    Plan credit use: 1 call credit per 100 market pairs returned (rounded up)
    and 1 call credit per convert option beyond the first. CMC equivalent
    pages: Our active cryptocurrency markets pages like
    """

    def __init__(self, request, endpoint):
        self.request = lambda x: request(
            urljoin(endpoint, "market-pairs/latest"), args(**x)
        )

    def id(self, id: Union[str, int], start=1, limit=100, convert="USD"):
        """
        Parameters
        ----------
        id : [str, int]
            One CoinMarketCap cryptocurrency IDs. Example: "1"
        convert : [str, list], "USD" (default)
           Optionally calculate market quotes in up to 40 currencies at once
           by passing a list of cryptocurrency or fiat currency symbols.
           Each additional convert option beyond the first requires an
           additional call credit. Each conversion is returned in its own
           "quote" object. A list of supported fiat options can be
           found here https://coinmarketcap.com/api/documentation/v1/#section/Standards-and-Conventions.

        Returns
        -------
        json object
            Respone schema - https://coinmarketcap.com/api/documentation/v1/#operation/getV1CryptocurrencyMarketpairsLatest
        """
        return self.request(locals())

    def symbol(self, symbol: str, start=1, limit=100, convert="USD"):
        """
        Parameters
        ----------
        symbol : str
            One or cryptocurrency symbols. Example: "BTC".
        convert : [str, list], "USD" (default)
           Optionally calculate market quotes in up to 40 currencies at once
           by passing a list of cryptocurrency or fiat currency symbols.
           Each additional convert option beyond the first requires an
           additional call credit. Each conversion is returned in its own
           "quote" object. A list of supported fiat options can be
           found here https://coinmarketcap.com/api/documentation/v1/#section/Standards-and-Conventions.

        Returns
        -------
        json object
            Respone schema - https://coinmarketcap.com/api/documentation/v1/#operation/getV1CryptocurrencyMarketpairsLatest
        """
        return self.request(locals())


class Ohlcv:
    """
    Return historical and latest OHLCV (Open, High, Low, Close, Volume) data
    along with market cap for any cryptocurrency using time interval
    parameters. Currently daily and hourly OHLCV periods are supported.
    Volume is only supported with daily periods at this time.

    Cache / Update frequency: Every 5 minutes. Additional OHLCV intervals and 1 minute updates will be available in the near-term.
    Plan credit use: 1 call credit per 100 OHLCV values returned (rounded up) and 1 call credit per convert option beyond the first.
    CMC equivalent pages: No equivalent, this data is only available via API.
    """

    def __init__(self, request, endpoint):
        self.request = lambda x, y: request(urljoin(endpoint, "ohlcv", x), args(**y))

    def historical_id(
        self,
        id: Union[str, int],
        time_start: Union[datetime.datetime, float],
        time_end: Union[datetime.datetime, float],
        time_period="daily",
        count=10,
        interval="daily",
        convert="USD",
    ):
        """
        Parameters
        ----------
        id : [int, str]
            A CoinMarketCap cryptocurrency ID. Example: "1"
        time_start : [datetime, float]
            Timestamp (Unix or datetime) to start returning OHLCV time periods
            for. Only the date portion of the timestamp is used for daily OHLCV.
        time_end : [datetime, float]
            Timestamp (Unix or datetime) to stop returning OHLCV time periods for
            (inclusive). Optional, if not passed we'll default to the current
            time. Only the date portion of the timestamp is used for daily OHLCV.
        time_period : str, "daily" (default)
            valid values : "daily" "hourly"
            Time period to return OHLCV data for. The default is "daily".
            See the main endpoint description for details.
        count : int, 10 (default)
            Optionally limit the number of time periods to return results for.
            The default is 10 items. The current query limit is 10000 items.
        interval : str, "daily" (default)
            valid values: "hourly", "daily", "weekly", "monthly", "yearly",
            "1h", "2h", "3h", "4h", "6h", "12h", "1d", "2d", "3d", "7d", "14d",
            "15d", "30d", "60d", "90d", "365d"
            Optionally adjust the interval that "time_period" is sampled.
            See main endpoint description for available options.
        convert : str, "USD" (default)
            By default market quotes are returned in USD. Optionally calculate
            market quotes in another fiat currency or cryptocurrency.

        Returns
        -------
        json object
            Respone schema - https://coinmarketcap.com/api/documentation/v1/#operation/getV1CryptocurrencyOhlcvHistorical
        """
        return self.request("historical", locals())

    def historical_symbol(
        self,
        symbol: str,
        time_start: Union[datetime.datetime, float],
        time_end: Union[datetime.datetime, float],
        time_period="daily",
        count=10,
        interval="daily",
        convert="USD",
    ):
        """
        Parameters
        ----------
        symbol : str
            A cryptocurrency symbol. Example: "BTC".
        time_start : [datetime, float]
            Timestamp (Unix or datetime) to start returning OHLCV time periods
            for. Only the date portion of the timestamp is used for daily OHLCV.
        time_end : [datetime, float]
            Timestamp (Unix or datetime) to stop returning OHLCV time periods for
            (inclusive). Optional, if not passed we'll default to the current
            time. Only the date portion of the timestamp is used for daily OHLCV.
        time_period : str, "daily" (default)
            valid values : "daily" "hourly"
            Time period to return OHLCV data for. The default is "daily".
            See the main endpoint description for details.
        count : int, 10 (default)
            Optionally limit the number of time periods to return results for.
            The default is 10 items. The current query limit is 10000 items.
        interval : str, "daily" (default)
            valid values: "hourly", "daily", "weekly", "monthly", "yearly",
            "1h", "2h", "3h", "4h", "6h", "12h", "1d", "2d", "3d", "7d", "14d",
            "15d", "30d", "60d", "90d", "365d"
            Optionally adjust the interval that "time_period" is sampled.
            See main endpoint description for available options.
        convert : str, "USD" (default)
            By default market quotes are returned in USD. Optionally calculate
            market quotes in another fiat currency or cryptocurrency.

        Returns
        -------
        json object
            Respone schema - https://coinmarketcap.com/api/documentation/v1/#operation/getV1CryptocurrencyOhlcvHistorical
        """
        return self.request("historical", locals())

    def latest_id(self, id: Union[list, str, int], convert="USD"):
        """
        Parameters
        ----------
        id : [int, str]
            A CoinMarketCap cryptocurrency ID. Example: "1"
        convert : str, "USD" (default)
            Optionally calculate market quotes in up to 40 currencies at once by
            passing a list of cryptocurrency or fiat currency symbols. Each
            additional convert option beyond the first requires an additional call
            credit. A list of supported fiat options can be found here. Each
            conversion is returned in its own "quote" object.

        Returns
        -------
        json object
            Respone schema - https://coinmarketcap.com/api/documentation/v1/#operation/getV1CryptocurrencyOhlcvLatest
        """
        return self.request("latest", locals())

    def latest_symbol(self, symbol: Union[list, str], convert="USD"):
        """
        Parameters
        ----------
        symbol : [list, str]
            One or a list of cryptocurrency symbols. Example: "BTC,ETH".
        convert : str, "USD" (default)
            Optionally calculate market quotes in up to 40 currencies at once by
            passing a list of cryptocurrency or fiat currency symbols. Each
            additional convert option beyond the first requires an additional call
            credit. A list of supported fiat options can be found here. Each
            conversion is returned in its own "quote" object.

        Returns
        -------
        json object
            Respone schema - https://coinmarketcap.com/api/documentation/v1/#operation/getV1CryptocurrencyOhlcvLatest
        """
        return self.request("latest", locals())


class Quotes:
    """ Get market quotes

    Returns an interval of historic market quotes for any cryptocurrency based
    on time and interval parameters.
    """

    def __init__(self, request, endpoint):
        self.request = lambda x, y: request(urljoin(endpoint, "quotes", x), args(**y))

    def historical_id(
        self,
        id: Union[str, int],
        time_start: Union[datetime.datetime, float],
        time_end: Union[datetime.datetime, float],
        count=10,
        interval="5m",
        convert="USD",
    ):
        """
        Parameters
        ----------
        id : [int, str]
            A CoinMarketCap cryptocurrency or fiat ID. Example: "1"
        time_start : [datetime, float]
            Timestamp (Unix or datetime) to start returning OHLCV time periods
            for. Only the date portion of the timestamp is used for daily OHLCV.
        count : int, 10 (default), [1 .. 10000]
            The number of interval periods to return results for. Optional, required
            if both "time_start" and "time_end" aren't supplied. The default is 10 items.
            The current query limit is 10000.
        interval : str, "5m" (default)
            Valid values: "yearly", "monthly", "weekly", "daily", "hourly",
            "5m", "10m", "15m", "30m", "45m", "1h", "2h", "3h", "6h", "12h",
            "24h", "1d", "2d", "3d", "7d", "14d", "15d", "30d", "60d", "90d",
            "365d".
            Interval of time to return data points for.
        convert : str, "USD" (default)
            By default market quotes are returned in USD. Optionally calculate
            market quotes in another fiat currency or cryptocurrency.

        Returns
        -------
        json object
            Respone schema - https://coinmarketcap.com/api/documentation/v1/#operation/getV1CryptocurrencyQuotesHistorical
        """
        return self.request("historical", locals())

    def historical_symbol(
        self,
        symbol: str,
        time_start: Union[datetime.datetime, float],
        time_end: Union[datetime.datetime, float],
        count=10,
        interval="daily",
        convert="USD",
    ):
        """
        Parameters
        ----------
        symbol : str
            pass a cryptocurrency symbol. Fiat symbols are not supported here.
            Example: "BTC".
        time_start : [datetime, float]
            Timestamp (Unix or datetime) to start returning OHLCV time periods
            for. Only the date portion of the timestamp is used for daily OHLCV.
        count : int, 10 (default), [1 .. 10000]
            The number of interval periods to return results for. Optional, required
            if both "time_start" and "time_end" aren't supplied. The default is 10 items.
            The current query limit is 10000.
        interval : str, "5m" (default)
            Valid values: "yearly", "monthly", "weekly", "daily", "hourly",
            "5m", "10m", "15m", "30m", "45m", "1h", "2h", "3h", "6h", "12h",
            "24h", "1d", "2d", "3d", "7d", "14d", "15d", "30d", "60d", "90d",
            "365d".
            Interval of time to return data points for.
        convert : str, "USD" (default)
            By default market quotes are returned in USD. Optionally calculate
            market quotes in another fiat currency or cryptocurrency.

        Returns
        -------
        json object
            Respone schema - https://coinmarketcap.com/api/documentation/v1/#operation/getV1CryptocurrencyQuotesHistorical
        """
        return self.request("historical", locals())

    def latest_id(self, id: Union[list, str, int], convert="USD"):
        """
        Parameters
        ----------
        id : [list, str, int]
            One or a list of CoinMarketCap cryptocurrency IDs. Example: "1,2"
        convert : str, "USD" (default)
            Optionally calculate market quotes in up to 40 currencies at once by
            passing a list of cryptocurrency or fiat currency symbols. Each
            additional convert option beyond the first requires an additional call
            credit. A list of supported fiat options can be found here. Each
            conversion is returned in its own "quote" object.

        Returns
        -------
        json object
            Respone schema - https://coinmarketcap.com/api/documentation/v1/#operation/getV1CryptocurrencyQuotesLatest
        """
        return self.request("latest", locals())

    def latest_symbol(self, symbol: Union[list, str], convert="USD"):
        """
        Parameters
        ----------
        symbol : [list, str]
            One or a list of cryptocurrency symbols. Example: "BTC,ETH".
        convert : str, "USD" (default)
            Optionally calculate market quotes in up to 40 currencies at once by
            passing a list of cryptocurrency or fiat currency symbols. Each
            additional convert option beyond the first requires an additional call
            credit. A list of supported fiat options can be found here. Each
            conversion is returned in its own "quote" object.

        Returns
        -------
        json object
            Respone schema - https://coinmarketcap.com/api/documentation/v1/#operation/getV1CryptocurrencyQuotesLatest
        """
        return self.request("latest", locals())


class Cryptocurrency:
    def __init__(self, request):
        args = (request, "cryptocurrency")
        self.info = Info(*args)
        self.map = Map(*args)
        self.pairs = Pairs(*args)
        self.listings = Listings(*args)
        self.ohlcv = Ohlcv(*args)
        self.quotes = Quotes(*args)
