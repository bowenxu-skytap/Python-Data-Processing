# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 09:26:00 2018

@author: bxu601
"""

pList = [('MMM', '3M', '236.67'), ('AXP', 'American Express', '96.79'), 
         ('AAPL', 'Apple', '172.43'), ('BA', 'Boeing', '355.04'), 
         ('CAT', 'Caterpillar', '156.29')]
aList = []
bList = []
for i in range(5):
    aString = pList[i][0]
    bString = pList[i][2]
    aList.append(aString)
    bList.append(bString)
dict = dict(zip(aList, bList))
'''
dict = {}
for data in pList:
    dict[data[0]] = data[2]
'''
print(dict)