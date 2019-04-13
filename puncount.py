# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 10:49:06 2018

@author: bxu601
"""

aStr = "Hello, World!"
bStr = aStr[:7] + 'Python!'
count = 0
for ch in bStr:
    if ch in ',.!?':
        count += 1
print(count)