# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 15:42:58 2018

@author: bxu601
"""

sStr = "acdhdca"
if sStr == ''.join(reversed(sStr)):
    # sStr == sStr[::-1]
    print('Yes')
else:
    print('No')