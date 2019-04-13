# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 15:34:49 2018

@author: bxu601
"""

import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0, 1)
y = np.sin(4 * np.pi * x) * np.exp(-5 * x)
plt.plot(x, y, 'o')