# -*- coding: utf-8 -*-
"""
Created on Fri Feb  9 14:56:04 2018

@author: bxu601
"""

import requests
from bs4 import BeautifulSoup
import re

r = requests.get("https://book.douban.com/subject/1084336/comments/")

soup = BeautifulSoup(r.text, 'lxml')
#markup = '<p class="title"><b>The Little Prince</b></p>'
pattern = soup.find_all('p', 'comment-content')
for item in pattern:
    print(item.string)

pattern_s = re.compile('<span class="user-stars allstar(.*?) rating"')
p = re.findall(pattern_s, r.text)
sum = 0
for star in p:
    sum += int(star)
print(sum)

