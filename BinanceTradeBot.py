from binance.client import Client
from binance.enums import *
import threading


api_key = 'Insert Key Here'
api_secret = 'Insert Secret Here'

client = Client(api_key, api_secret)

tickersymbol = 'LTCBTC'

price = client.get_recent_trades(symbol=tickersymbol);

lastprice = price[len(price)-1]['price']

print(lastprice);

price = round((float(lastprice)*.95), 4)

print(price)

def looporder():

	#Most Recent Client Trade
	MRCT = client.get_recent_trades(symbol=tickersymbol);

	lasttrade = len(MRCT)-1

	currentprice = float(MRCT[lasttrade]['price'])

	if currentprice > price:
		try:
			sellorder = client.order_limit_sell(
				symbol=ticker,
			    quantity=10000,
			    price=price)
		except:
			print("Sale order did not go through.")
	else:
		buyorder = client.order_limit_buy(
			  symbol=ticker,
		      quantity=10000,
		      price=price)
	threading.Timer(60, looporder).start();

looporder();