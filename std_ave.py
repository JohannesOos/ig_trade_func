# -*- coding: utf-8 -*-
"""
Created on Mon Aug 08 17:34:38 2016

@author: Oos
"""

"""

this file defines two functions:
the first is calculate a rolling average and an std
the second is to calculate the momentum
there is also a test list defined to check the correct inmplementation easily
"""

import math

value_list = [1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,1,2,3,4,5,6]  # list of bin size values for tests


#################################
#funciton for rolling average and std calculation

def give_roll_ave_and_std(value_list, bin_size =20):
	"""
	input 
	valuelist: list of length bin_size
	bin_size: int
	
	return:
	list of form average and std
	"""
	#check if bin size is ok
	
	if len(value_list) > bin_size:
		value_list = value_list[-bin_size:]
	elif len(value_list) < bin_size:
		return "list too small"

	#average
	sum_pre = sum(value_list)
	ave = sum_pre/float(bin_size)

	#standard deviation	
	tot_sum = 0 # helper variable for std calcualtion
	#calulcating the sum for the std caluclation
	for value in value_list:
		dif = (value - ave)**2
		tot_sum += dif

		std = math.sqrt(tot_sum / (bin_size-1))  #std formula

	return [ave, std]


#################################
#extend each Mongo DB entrie by value of
#1_std = 1 * std
#2_std = 2 * std
#std_upper = ave + std
#std_lower = ave - std
#2_std_upper = ave + 2*std
#2_std_lower = ave - 2*std



#################################
#momentum calc 
"""
momentum is the trend as is relative to the last datapoints
"""

def give_momentum(value_list ,bin_size, mom_short_size = 2,mom_long_size =10):
	"""
	input 
	value_lilst: list of length bin_size
	bin_size: int
	returns three values for momentums (-0.5 means 50% loss)
	"""
	
	mom_short_values = mom_short_size
	mom_long_values = mom_long_size
	mom_bin_size = bin_size
	
	#the diff is the absolute change
	dif_short = value_list[-1] - value_list[-mom_short_values]
	dif_long = value_list[-1] - value_list[-mom_long_values]
	dif_bin = value_list[-1] - value_list[-mom_bin_size]
	
	#the momentum is teh relative change
	mom_short = dif_short/float(value_list[-1])
	mom_long = dif_long/ float(value_list[-1])
	mom_bin = dif_bin / float(value_list[-1])

	return [mom_bin, mom_short, mom_long]


####################################
#extend each mongo DB entrie by value of
#mom_bin
#mom_short
#mom_long

#######################################
