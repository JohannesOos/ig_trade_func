# -*- coding: utf-8 -*-
"""
Created on Mon Aug 01 13:31:46 2016

@author: Oos
"""

"""
to have a sample script of buying and selling with no good strategy
but for understanding of the ecosystem
"""

#set up environment
#first the trading packackge
from trading_ig import IGService
#then the password
from trading_ig_config import config

#the trading functions
from own_work_around import close_open_position_market
from own_work_around import create_open_position_market
from own_work_around import create_open_position_limit
from own_work_around import close_open_position_limit

import time

#create the connection to ig
ig_service = IGService(config.username, config.password, config.api_key, config.acc_type)
ig_service.create_session()



heartbeat = 10  # wait in seconds


"""code to close a position"""
def sample_sell():

    direction ="SELL"
    epic = "CS.D.EURUSD.MINI.IP"
    expiry = "-"
    size = 1 #how many
    response = close_open_position_market(ig_service, direction, epic, expiry, size)    
    return response

"""code to open shit"""  
def sample_buy():
    currency_code = "USD"
    direction = "BUY" # change to sell if market is falling
    epic = "CS.D.EURUSD.MINI.IP" # change to stuff you wanna trade
    expiry = "-" # random date in the future
    limit_distance = 5 # by hand for testing 
    size = 1 # define how many will be traded
    stop_distance = 5 # by hand for testing 
    
    response = create_open_position_market (ig_service, currency_code, direction, epic, expiry, 
                         limit_distance, size, stop_distance)
    return response



#buy and sell same stuff every X sec
if False:
    i = 0
    answer_list_buy = []
    answer_list_sell =[]
    while i <=3:
        a = sample_buy()
        answer_list_buy.append(a)
        time.sleep(heartbeat)
        b = sample_sell()
        answer_list_sell.append(b)
        time.sleep(heartbeat)
        i+=1
    
    