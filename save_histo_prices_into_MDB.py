# -*- coding: utf-8 -*-
"""
Created on Sat Aug 06 17:33:38 2016

@author: Oos
"""
"""
this script can be used to save data into mongodb from IG trading
the limit of the api is 10,000 values per week though...
so limit use only
as is now it copy the mintue data of 5 days for eurusd exchange

"""


from trading_ig import IGService
#then my password
from trading_ig_config import config

import pymongo

# establish a connection to the database
connection = pymongo.MongoClient("mongodb://localhost")
# define database
db=connection.ig_trade
#define one colelction per epic
eurusd = db.eurusd



#create the conention
ig_service = IGService(config.username, config.password, config.api_key, config.acc_type)
ig_service.create_session()

#get all data historical

#define resolution - see IG service and rst api reference for correct names
reso = '1Min'

#how far back
num_points = 7200

#which epic
epic = "CS.D.EURUSD.MINI.IP"

#ask the server for json response
response = ig_service.fetch_historical_prices_by_epic_and_num_points(epic, reso, num_points)

#name the json positions so its easier to undersand
df_ask_close = response['prices']['ask']["Close"]
df_ask_high = response['prices']['ask']["High"]
df_ask_low = response['prices']['ask']["Low"]
df_bid_close = response['prices']['bid']["Close"]
df_bid_high = response['prices']['bid']["High"]
df_bid_low = response['prices']['bid']["Low"]
dates = df_bid_low.index.values

#create the monog db entries, one for each time point
for entry in range(num_points):
    eurusd.insert_one({"_id": dates[entry], 
                       "ask": {"close":df_ask_close[entry], "high":df_ask_high[entry], "low":df_ask_low[entry]},
                       "bid": {"close":df_bid_close[entry], "high":df_bid_high[entry], "low":df_bid_low[entry]}
                       })


