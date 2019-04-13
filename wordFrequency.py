# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 15:26:07 2018

@author: bxu601
"""

# Method 1: 用collections模块中的Counter()函数
import collections
import copy
s = "我 是 一个 测试 句子 ， 大家 赶快 来 统计 我 吧 ， 大家 赶快 来 统计 我 吧，大家 赶快 来 统计 我 吧 ， 重要 事情 说 三遍 ！"
s_list = s.split()
s_list_backup = copy.deepcopy(s_list)
[s_list.remove(item) for item in s_list_backup if item in '，。！”“']
#print(s_list_backup)
#print(s_list)
print(collections.Counter(s_list))

# Method2: Use Dict
s = "我 是 一个 测试 句子 ， 大家 赶快 来 统计 我 吧 ， 大家 赶快 来 统计 我 吧，大家 赶快 来 统计 我 吧 ， 重要 事情 说 三遍 ！"
s_list = s.split()
#print(s_list)
dict = {}
for i in s_list:
    if i.strip() not in "，。！“”":
        if i not in dict:
            dict[i] = 1
        else:
            dict[i] += 1
print(dict)
