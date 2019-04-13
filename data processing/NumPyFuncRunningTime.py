# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 15:14:48 2018

@author: bxu601
"""

import time
import math
import numpy as py

x = py.arange(0, 1000, 0.01)
t_m1 = time.clock()
for i, j in enumerate(x):
    x[i] = math.sqrt(j)
t_m2 = time.clock()

y = py.arange(0, 1000, 0.01)
t_n1 = time.clock()
y = py.sqrt(y)
t_n2 = time.clock()

print('Running time of math:', t_m2 -t_m1)
print('Running time of numpy:', t_n2 -t_n1)