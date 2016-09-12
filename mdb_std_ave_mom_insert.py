# -*- coding: utf-8 -*-
"""
Created on Sun Aug 14 20:48:49 2016

@author: Oos
"""

import std_ave
import pymongo

"""
this script reads in a mongo db collection
the read in colelction shoudl hae the format of the ig_Trade answer
it create a new colelction that has onyl the timestamp as id and some values
those values are rolling average and bolligner bands accoridn gto the bin size selected
it only uses the ask close values

"""


###################connect to MONGO DB ############################
# establish a connection to the database mongodb
connection = pymongo.MongoClient("mongodb://localhost")

# define database
db=connection.ig_trade

#define the two colelctions
#can be any here 
eurusd = db.eurusd
eurusd_copy = db.eurusd_copy

#tp drop an old exisitng one
eurusd_copy.drop()

#################connection stands ###################################


####################create cursor to all elements in first collection###########
cursor = eurusd.find()
####################cursor done###################################

####################create helper variables
bin_size = 20
valueList = []
result_pair = [0,0]
mom_list = [0,0,0]


#####################run through all entries of colelction ###########################
for entry in cursor:    
    """
    now for each entriy in teh original collecion we calucalate values
    those values are only calculatable, if they have values prior to them
    """    
    
    #the needed value of the cursor id the ask - close value
    ask_close = entry["ask"]["close"]
    
    #nan handler, entries cant start with Nan
    if ask_close == "NaN":
        #if there is no value, the prior value is used
        ask_close = valueList[-1]
    # the new value gets attached to the value list
    valueList.append(ask_close)  
    
    #delete first element of value list
    if len(valueList) > bin_size:
        #if the list now got lnger then the bin we can pop the first element (the oldest)
        valueList = valueList[1:]
        #the std ave function calculates teh rllign average and the std
        result_pair = std_ave.give_roll_ave_and_std(valueList, bin_size)
        
    #the values before reaching a fill bin are useless so they 
    # get the dummy value 0
    average = result_pair[0]
    std = result_pair[1]
    
    #momentum list from std_ave only f value list long eneough
    if len(valueList) == bin_size:
        mom_list = std_ave.give_momentum(valueList, bin_size)
    
    #define the new insert into the database
    eurusd_copy.insert_one(
    {"_id":entry["_id"], 
    "ask_close": ask_close,
    "ave": average,
    "std": std,
    "neg_std": average - std ,
    "pos_std": average + std,
    "neg_2std": average - 2*std,
    "pos_2std": average + 2*std,
    "mom":{"short": mom_list[1], "long": mom_list[2], "bin": mom_list[0]}
    }
    )

