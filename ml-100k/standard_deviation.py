# -*- coding: utf-8 -*-
"""
Created on Tue Mar  6 21:21:28 2018

@author: bxu601
"""
# Cousera课程《用Python玩转数据 Data Processing Using Python》第4.2章编程作业《男女电影评分差异分析编程》
#
#分析数据集，找出男性女性用户评分的标准差，并输出两位小数部分
#提示：先分别计算每个人电影评分的平均分，再按性别求标准差

import pandas


table = pandas.read_table('u.data', sep='\t', names=('userid', 'rating'), usecols=[0,2])
#print(table)

table_user = pandas.read_table('u.user', sep='|', names=('userid', 'gender'), usecols=[0,2])
#print(table_user)

df = pandas.merge(table, table_user, how='inner')
#print(df)

std_male = df[df.gender=='M'].groupby('userid').mean().std()
std_female = df[df.gender=='F'].groupby('userid').mean().std()

print(std_male)
print(std_female)