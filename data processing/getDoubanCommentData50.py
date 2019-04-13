# -*- coding: utf-8 -*-
"""
Created on Fri Feb  9 14:56:04 2018

@author: bxu601
"""

import requests
from bs4 import BeautifulSoup
import re

i = 1
count = 0
sum = 0
count_s = 0

while(count < 50):
    try:
        r = requests.get("https://book.douban.com/subject/1084336/comments/hot?p=" + str(i))
    except Exception as err:
        print(err)
        break
    soup = BeautifulSoup(r.text, 'lxml')
    pattern = soup.find_all('p', 'comment-content')
    for item in pattern:
        print(count+1, item.string)
        count += 1
        if count == 50:
            break
    pattern_s = re.compile('<span class="user-stars allstar(.*?) rating"')
    p = re.findall(pattern_s, r.text)
    for star in p:
        count_s += 1
        sum += int(star)
    i += 1

if count == 50:
    print("Average star:", sum/count_s/10)
