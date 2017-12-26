#!/usr/bin/env python

# import blockchain library

from blockchain import statistics

# get the statistics

stats = statistics.get()


# Get and print the trade volume

print("Bitcoin Trade volume: %s" % stats.trade_volume_btc)


# Get and print bitcoin mined

Print("Bitcoin mined: %s\n", stats.btc_mined )