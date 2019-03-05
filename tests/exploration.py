from context import coinmarketcap
from datetime import datetime

client = coinmarketcap.Client(sandbox=True)

# fetch cryptocurrency info
client.cryptocurrency.listings.latest_start()
client.cryptocurrency.info.ids(1)
client.cryptocurrency.info.symbols(["BTC", "ETH"])

# fetch exchange info
client.exchange.info.slugs("binance")
client.exchange.info.ids([1, 4])

# fetch global market data
time = datetime.strptime("2018-12-21", "%Y-%m-%d")
client.global_metrics.quotes.latest()

amount_1 = 100.4
amount_2 = "901.23"
id = 4

# convert price historic price
client.tools.price.convert_id(amount_1, id, time=time)
client.tools.price.convert_symbol(amount_2, "BTC", convert=["USD", "ETH"])
