# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 13:25:18 2018

@author: bxu601
"""

import requests
import re
import json
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans

def retrieve_quotes_historical(stock_code):
    quotes = []
    url = 'https://finance.yahoo.com/quote/%s/history?p=%s' % (stock_code, stock_code)
    r = requests.get(url)
    m = re.findall('"HistoricalPriceStore":{"prices":(.*?),"isPending"', r.text)
    if m:
        quotes = json.loads(m[0])
        quotes = quotes[::-1]
    return  [item for item in quotes if not 'type' in item]

def create_df(stock_code):
    quotes = retrieve_quotes_historical(stock_code)
    cols = ['adjclose', 'close', '3', '4', '5', '6', '7']
    return pd.DataFrame(quotes, columns = cols)

listDji = ['MMM', 'AXP', 'AAPL', 'BA', 'CAT', 'CVX', 'CSCO', 'KO', 'DIS', 'DD']
listTemp = [0] * len(listDji)
for i in range(len(listDji)):
    listTemp[i] = create_df(listDji[i]).close
status = [0] * len(listDji)
for i in range(len(status)):
    status[i] = np.sign(np.diff(listTemp[i]))
    
# 简单处理某一只或几只股票数据没有获得（值为[])的问题，删掉此数据
for i in range(len(status)):
    if len(status[i]) == 0:
		     status.pop(i)
         
kmeans = KMeans(n_clusters = 3).fit(status)
pred = kmeans.predict(status)
print(pred)
    