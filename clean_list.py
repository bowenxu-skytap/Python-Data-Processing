# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 21:26:50 2018

@author: USER
"""

def clean_list(lst):
    new_list = []
    for item in lst:
        for c in item:
            if c.isalpha() != True:
                item = item.replace(c, '')
        new_list.append(item)
    return new_list

coffee_list = ['32Latte', '_Americano30', '/34Cappuccino', 'Mocha35']
clean_list = clean_list(coffee_list)
for (j,k) in zip(range(1, len(coffee_list)+1), clean_list):
    print(j, k)

                