![Coverage](https://img.shields.io/badge/coverage-89%25-yellowgreen.svg)
![Python](https://img.shields.io/badge/Python-3.7-brightgreen.svg)
![Version](https://img.shields.io/badge/Version-0.4-brightgreen.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

# CoinMarketCap
A Python implementation of CoinMarketCap's V1 API.

## Installing
```terminal
python3 -m pip install CoinMarketCapAPI
```

## Authentication
Keys can be loaded given directly to the module or from a file in `$HOME/.coinmarketcap.json`, with the following syntax.
```json
{
  "sandbox": "API_KEY",
  "production": "API_KEY"
}
```

Or as OS environment variables.
```terminal
export COINMARKETCAP_SANDBOX="API_KEY"
export COINMARKETCAP_PRODUCTION="API_KEY"
```

It's highly recommended to test your application with the sandbox environment. You need a different API key when using the sandbox environment, you can get one from [here](https://sandbox.coinmarketcap.com/).


## Examples
Init client with an API Key.
```python
from coinmarketcap import Client

key = "API_KEY"
client = Client(apikey=key)
```

The following example shows how you can access and send a request to each of CoinMarketCap's endpoint (cryptocurrency, exchange, global_metrics, tools). Notice plural and singular method endings. Plurals allow a list of `id`, `symbol` or `slug`, singular allows only a single value.

```python
from coinmarketcap import Client
from datetime import datetime

# Init sandbox client.
client = Client(sandbox=True)

# fetch cryptocurrency info
client.cryptocurrency.info.symbols(["BTC", "ETH"])
client.cryptocurrency.info.ids(1)

# fetch exchange info
client.exchange.info.slugs("binance")
client.exchange.info.ids([1, 4])

# fetch global market data
time = datetime.strptime("2018-12-21", "%Y-%m-%d")
client.global_metrics.quotes.latest()
client.global_metrics.quotes.historical(time_start=time)

amount_1 = 100.4
amount_2 = "901.23"
id = 4
# convert price historic price
client.tools.price.convert_id(amount_1, id, time=time)
client.tools.price.convert_symbol(amount_2, "BTC", convert=["USD", "ETH"])
```

Due to CoinMarketCap's credit and rate limit system, implementing a proper request throttler is complex. Anyway, I tried to apply three different levels of throttling. WARNING, this module has no perception of credits, only requests.

```python  

from coinmarketcap import Client
# By default throttling of requests are off.
# Ignore the Client's keyword arguments "throttle", "plan", and "block" if
# you don't want the client to throttle requests.  

# client_1 will not exceed the number of request one can do each minute.
# Hopefully, an request limit exception will be raised if the limit each minute are exceeded.
# Hopefully, an HTTPError exception will be raised if the daily request limit is exceeded.
client_1 = Client(throttle="minute", plan="basic")

# client_2 will not exceed the daily request limit.
# Hopefully, the thread will be blocked if monthly request limit is exceeded.
# Hopefully, An HTTPError exception is raised if monthly request limit are exceeded.
client_2 = Client(throttle="daily", block=True, plan="hobbyist")

# client_3 will never exceeded CoinMarketCap request limit.
# Hopefully, will never exceed the monthly limit.
# Hopefully, an ratelimit exception is raised if the request limit is exceeded.
client_3 = Client(throttle="monthly", block=False, plan="professional")

```

Each request is cached, the expiration time of data can be adjusted with the keyword argument `expire`. Set `expire=0` if don't want any cached data.
```python
from coinmarketcap import Client
# cached request will be removed after 1 second
client = Client(expire=1)

# cacherd request will be removed after 1 h
client = Client(expire=3600)

# To remove all data from the cache, use the method clear_cache
client.clear_cache()

```

## TODO
This is my first python module. So, I appreciate any feedback :)
* Enable Proper throttling of requests.
* Testing of different python versions.
