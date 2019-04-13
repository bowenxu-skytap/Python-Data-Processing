# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 16:08:59 2018

@author: bxu601
"""

import requests as re
r = re.get('https://api.douban.com/v2/movie/subject/1291546') 
# 1292720, 1292052, 1295644
data = r.json()
print(data['title'], data['rating']['average'])