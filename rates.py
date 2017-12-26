#!/usr/bin/env python

# import blockchain library

from blockchain import exchangerates

# get the bitcoin rates in various currencies

ticker = exchangerates.get_ticker()


# print bitcoin price for every currency

print("Bitcoin Prices")

for k in ticker:
	print k, ticker[k].p15min

# getting bitcoin value for a particular amount and currency

btc = exchangerates.to_btc('EUR',100)
print("\n100 euros in Bitcoin: %s", %btc )