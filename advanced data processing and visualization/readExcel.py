# -*- coding: utf-8 -*-
"""
Created on Thu Mar  1 16:15:37 2018

@author: bxu601
"""

import pandas as pd

df= pd.read_excel('grades.xlsx')
df['sum'] = df['Python'] + df['Math']
df.to_excel('students.xlsx',sheet_name='scores')