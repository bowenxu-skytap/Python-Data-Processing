# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 15:56:46 2018

@author: bxu601
"""

aStr= 'What do you think of this saying "No pain, No gain"?'
tempStr = aStr.split('\"')[1]
if tempStr.istitle():
    print('It is title format.')
else:
    print('It is not title format.')
print(tempStr.title())