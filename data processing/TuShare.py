# -*- coding: utf-8 -*-
"""
Created on Fri Feb  9 14:56:04 2018

@author: bxu601
"""

#获取股票代码是600848的股票在2017年3月1日至3月10日间的基本历史数据

import tushare as ts
data = ts.get_hist_data('600848', start='2017-03-01', end='2017-03-08')
print(data)