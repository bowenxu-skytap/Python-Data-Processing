# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 15:23:41 2018

@author: bxu601
"""

import numpy as np
import pandas as pd

dates = pd.date_range('20171001', periods=10)
listA = ['value']

result = pd.DataFrame(np.array(range(1, 11)), index=dates, columns = listA)
print(result)