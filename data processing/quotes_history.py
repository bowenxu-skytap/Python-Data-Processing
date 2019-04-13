# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 11:33:33 2018

@author: bxu601
"""

import requests
import re
import json
import pandas as pd
from datetime import date

def retrieve_quotes_historical(stock_code):
    quotes = []
    url = 'https://finance.yahoo.com/quote/%s/history?p=%s' % (stock_code, stock_code)
    r = requests.get(url)
    m = re.findall('"HistoricalPriceStore":{"prices":(.*?),"isPending"', r.text)
    if m:
        quotes = json.loads(m[0])
        quotes = quotes[::-1]
    return  [item for item in quotes if not 'type' in item]

quotes = retrieve_quotes_historical('IBM')
print(quotes)
dateList = []
for i in range(len(quotes)):
    x = date.fromtimestamp(quotes[i]['date'])
    y = date.strftime(x, '%Y-%m-%d')
    dateList.append(y)
quotesdf_ori = pd.DataFrame(quotes, index = dateList)
quotesdf = quotesdf_ori.drop(['date'], axis = 1)
print(quotesdf)