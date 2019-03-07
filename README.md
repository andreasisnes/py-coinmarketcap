![Coverage](https://img.shields.io/badge/coverage-87%25-yellowgreen.svg)
![Python](https://img.shields.io/badge/Python-3.7-brightgreen.svg)
![Version](https://img.shields.io/badge/Version-0.5-brightgreen.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

# CoinMarketCap
A Python implementation of CoinMarketCap's V1 API.


You need an API key from CoinMarketCap to utilize this module, and you can get a key from [here](https://coinmarketcap.com/api/). Due to the low request rate, I recommend you to test your application in their sandbox environment. You need a different API key when using their sandbox environment that you can get from [here](https://sandbox.coinmarketcap.com/).

## Installing
```terminal
python3 -m pip install CoinMarketCapAPI
```

## Authentication
If no keys are provided during init, the module will look for a JSON file in `$HOME/.coinmarketcap.json`, with the following syntax.
```json
{
  "sandbox": "API_KEY",
  "production": "API_KEY"
}
```

Alternatively, you can set your keys as OS environment variables. With .bashrc, add the following two lines.
```terminal
export COINMARKETCAP_SANDBOX="API_KEY"
export COINMARKETCAP_PRODUCTION="API_KEY"
```

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

Due to CoinMarketCap's credit and rate limit system, implementing a proper request throttler is complex. Anyway, I tried to apply three different levels of throttling. "minute", "daily", "monthly". Each level make sure you don't exceed the request limit of the given plan. The different levels have no perception of CoinMarketCap's credit system...

```python  

from coinmarketcap import Client
# By default throttling of requests are off.
# Ignore the Client's keyword arguments "throttle", "plan", and "block" if
# you don't want the client to throttle requests.  

# client_1 will not exceed the number of request each minute with the basic plan.
client_1 = Client(throttle="minute", plan="basic")

# client_2 will not exceed the daily request limit.
client_2 = Client(throttle="daily", block=True, plan="hobbyist")

# client_3 will never exceeded CoinMarketCap monthly request rate.
client_3 = Client(throttle="monthly", block=False, plan="professional")

```

Each request is cached, the expiration time of data can be adjusted with the keyword argument `expire`. Set `expire=0` if don't want any cached data.
```python
from coinmarketcap import Client
# cached request will be removed after a second.
client = Client(expire=1)

# cached request will be removed after an hour
client = Client(expire=3600)

# To remove all data from the cache, use the method clear_cache
client.clear_cache()
```

## TODO
* Enable Proper throttling of requests.
* Testing in different python versions.

This is my first python module. So, I appreciate any feedback :)
