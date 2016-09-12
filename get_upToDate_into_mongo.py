# -*- coding: utf-8 -*-
"""
Created on Sat Aug 06 17:33:38 2016

@author: Oos
"""

"""
the script test the storing of itmes of the rest APi into MOngoDB databases
the actual getting of data is better daone using the stream api
but this serves a trial start to get a feeling and understanding for some items
"""

# building on top of IGSERVICE
from trading_ig import IGService

#get teh pasword
from trading_ig_config import config

#get the epics we want to copy
import epic_List as eL

#get the other needed python libs
import time
import pymongo

# establish a connection to the mongo server
connection = pymongo.MongoClient("mongodb://localhost")
# define database
db=connection.ig_trade

#define one colelction per epic
#here hard coded in - needs to be adjusted and be done more flexible
eurusd = db.eurusd
gbpusd = db.gbpusd
gbpeur = db.gbpeur

colList = [eurusd, gbpusd, gbpeur]


#create the conention
ig_service = IGService(config.username, config.password, config.api_key, config.acc_type)
ig_service.create_session()


timelist = []
#start timer and counter

counter = 0
t0 = time.time()
freq = 10 # frequency of call is every 10 seconds

while counter < 80:
    #create list for all information
    bunch_list =[]
    epicList = eL.epics_main
    
    #get the market prices by their epic number
    for epic in epicList:
        bunch_list.append(ig_service.fetch_market_by_epic(epic))
    
    
    #create list of main information as dictionary
    snaplist = []
    for bunch in range(len(bunch_list)):
        snaplist.append(dict(bunch_list[bunch]["snapshot"]))
        
    
    #insert into the mongo collection
    for data in range(len(snaplist)):
        coll = colList[data]
        coll.insert_one(snaplist[data])
    
    #get timing right for repetition
    timelist.append(time.time()-t0)
    time_so_far = time.time()-t0-counter*freq
    time.sleep(freq-time_so_far)
    counter +=1
    print counter
    print time_so_far