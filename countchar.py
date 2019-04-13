# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 21:13:02 2018

@author: USER
"""

def countchar(s):
    list = [0] * 26
    s = s.lower()
    for c in s:
        if c >= 'a' and c <= 'z':
            i = ord(c) - ord('a')
            list[i] += 1
    print(list)
    
s = "Hope is a good thing."
countchar(s)