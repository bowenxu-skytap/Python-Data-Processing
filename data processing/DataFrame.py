# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 15:28:36 2018

@author: bxu601
"""

import pandas as pd

music_data = [("the rolling stones","Satisfaction"),
              ("Beatles","Let It Be"),("Guns N' Roses","Don't Cry"),
              ("Metallica","Nothing Else Matters")]

frame = pd.DataFrame(music_data, index = range(1, 5), columns = ['singer', 'song_name'])

print(frame)