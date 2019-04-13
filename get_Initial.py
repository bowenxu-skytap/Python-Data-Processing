#!/usr/bin/env python

def get_initial(string):
    for i in string.split():
        print(i[0].upper())

get_initial('federal bureau investigation')
