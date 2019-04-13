# -*- coding: utf-8 -*-
"""
Created on Sun Mar  4 21:50:14 2018

@author: bxu601
"""

import nltk
from nltk.corpus import brown

cfd = nltk.ConditionalFreqDist((genre, word)
           for genre in brown.categories()
           for word in brown.words(categories = genre))
genres = ['news', 'romance']
modals = ['can', 'could', 'may', 'might', 'must', 'will', 'would']
cfd.tabulate(conditions = genres, samples = modals)
cfd.plot(conditions = genres, samples = modals)