# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 21:49:31 2018

@author: USER
"""

def insert_line(lines):
    lines.insert(0, "Blowin’ in the wind\n")
    lines.insert(1, "Bob Dylan\n")
    lines.append("\n1962 by Warner Bros. Inc.")
    return ''.join(lines)

with open("Blowing in the wind.txt", "r+") as f:
    lines = f.readlines()
    string = insert_line(lines)
    print(string)