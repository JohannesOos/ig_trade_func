# -*- coding: utf-8 -*-
"""
Created on Sat Aug 06 13:18:21 2016

@author: Oos
"""

#########################
"""
contains the main epics which are traded
Their name is taking from teh rest api of IG trade
the main ones have hihg frequency and volume
"""

epics_main = [
"CS.D.EURUSD.MINI.IP", #FOREX: EURO USD
'CS.D.GBPUSD.MINI.IP', #FOREX: GBP USD
'CS.D.GBPEUR.MINI.IP', #FOREC: GBP EURO

]

epics_secondary = [
'CS.D.EURJPY.MINI.IP', # FOREX EUR JPY

'CS.D.COPPER.MINI.IP', # METALLS: COPPER 5 USD
'CS.D.ALUMINIUM.MINI.IP', #METALLS: ALUMINIUM 5 USD
'CS.D.CFEGOLD.CFE.IP' #METALLS: GOLD KASSA 1 USD
]

epics_tertiery = [

'CS.D.GBPZAR.MINI.IP', #FOREX: GBP ZAR
'CS.D.GBPAUD.MINI.IP', #FOREX GBP AUD
'CS.D.AUDUSD.MINI.IP', # FOREX AUD USD
'CS.D.USDJPY.MINI.IP', # FOREX USD JPY

'CS.D.NICKEL.MINI.IP', # METALLS: NICKEL 1 USD
'CS.D.LEAD.MINI.IP', #METALLS: LEAD 5 USD
'CC.D.IRON.UME.IP', #Metalls: Iron Ore
]

all_epics = epics_main + epics_secondary + epics_tertiery