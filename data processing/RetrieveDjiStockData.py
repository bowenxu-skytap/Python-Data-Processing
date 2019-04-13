# -*- coding: utf-8 -*-
"""
Retrieve dji stock data

@author: USER
"""
import requests
import re
import pandas as pd

def retrieve_dji_list():
    r = requests.get("http://money.cnn.com/data/dow30/")
    pattern = re.compile('class="wsod_symbol">(.*?)<\/a>.*?<span.*?">(.*?)<\/span.*?\n.*?class="wsod_stream">(.*?)<\/span')
    list = re.findall(pattern, r.text)
    return list

list = retrieve_dji_list()
new_list = []
for item in list:
    new_list.append([item[0], item[1], float(item[2])]) 
print(new_list)

frame = pd.DataFrame(new_list)
cols = ['code', 'name', 'lasttrade']
frame.columns = cols
frame.index = range(1, len(frame) + 1)

print(frame)

