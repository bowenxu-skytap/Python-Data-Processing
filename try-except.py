# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 09:40:00 2018

@author: bxu601
"""

while True:
    try:
        count = int(input("Enter count: "))
        price = int(input("Enter price for each one: "))
        pay = count * price
        print("The price is:", pay)
        break
    except ValueError:
        print('Error, please enter numeric one. ')