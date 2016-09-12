# -*- coding: utf-8 -*-
"""
Created on Mon Aug 01 18:51:04 2016

@author: Oos
"""
import json
            
"""own workaround"""
"""
the code in teh standard ig libary did not work for me...
so jsut added functions I needed
this version just uses the values specified in teh api handbook

see also https://labs.ig.com/rest-trading-api-reference
"""


############MARKET TRADE START #####################

def close_open_position_market(ig_service, direction, epic, expiry, 
                        size, session=None):
    """Closes one or more OTC positions"""
    params = {

        'direction': direction,
        'epic': epic,
        'expiry': expiry,
        'orderType': "MARKET",
        'size': size
    }
    endpoint = '/positions/otc'
    action = 'delete'
    response = ig_service._req(action, endpoint, params, session)

    if response.status_code == 200:
        deal_reference = json.loads(response.text)['dealReference']
        return ig_service.fetch_deal_by_deal_reference(deal_reference)
    else:
        return response.text



def create_open_position_market (ig_service, currency_code, direction, epic, expiry,
                         limit_distance, size,
                         stop_distance, session = None):
    """Creates an OTC position"""
    params = {
        'currencyCode': currency_code,
        'direction': direction,
        'epic': epic,
        'expiry': expiry,
        'forceOpen': True,
        'guaranteedStop': False,
        'limitDistance': limit_distance,
        'orderType': "MARKET",
        'size': size,
        'stopDistance': stop_distance
    }

    endpoint = '/positions/otc'
    action = 'create'
    response = ig_service._req(action, endpoint, params, session)

    if response.status_code == 200:
        deal_reference = json.loads(response.text)['dealReference']
        return ig_service.fetch_deal_by_deal_reference(deal_reference)
    else:
        return response.text  # parse_response ?



############MARKET TRADE END #####################

############START LIMIT TRADE ###################

def create_open_position_limit (ig_service, currency_code, direction, epic, expiry,
                         level, limit_distance, size,
                         stop_distance, session = None):
    """Creates an OTC position"""
    params = {
        'currencyCode': currency_code,
        'direction': direction,
        'epic': epic,
        'expiry': expiry,
        'forceOpen': True,
        'guaranteedStop': False,
        'level': level,
        'limitDistance': limit_distance,
        'orderType': "LIMIT",
        'size': size,
        'stopDistance': stop_distance
    }

    endpoint = '/positions/otc'
    action = 'create'
    response = ig_service._req(action, endpoint, params, session)

    if response.status_code == 200:
        deal_reference = json.loads(response.text)['dealReference']
        return ig_service.fetch_deal_by_deal_reference(deal_reference)
    else:
        return response.text  # parse_response ?




def close_open_position_limit(ig_service, direction, epic, expiry, level, 
                        size, session=None):
    """Closes one or more OTC positions"""
    params = {

        'direction': direction,
        'epic': epic,
        'expiry': expiry,
        'level' : level,
        'orderType': "LIMIT",
        'size': size
    }
    endpoint = '/positions/otc'
    action = 'delete'
    response = ig_service._req(action, endpoint, params, session)

    if response.status_code == 200:
        deal_reference = json.loads(response.text)['dealReference']
        return ig_service.fetch_deal_by_deal_reference(deal_reference)
    else:
        return response.text

############END LIMIT TRADE ###################