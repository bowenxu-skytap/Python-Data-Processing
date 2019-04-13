# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 14:30:55 2018

@author: bxu601
"""


def newusers():
    name = input("Please enter a name: ")
    if name in system:
        newusers()
    else:
        passwd = input("Please enter a password: ")
        system[name] = passwd


def oldusers():
    name = input("Please enter a name: ")
    passwd = input("Please enter a password: ")
    if passwd == system.get(name):  
        print(name, 'welcome back ')  
    else:  
        print('login incorrect') 

def login():
    option = '''
             (N)ew User Login 
             (O)ld User Login
             (E)xit
             '''
    choice = ''
    while True: 
        print(option)
        choice = input("Enter the option: ")
        if choice.lower() == 'n':
            newusers()
            print(system)
            break
        elif choice.lower() == 'o':
            oldusers()
            print(system)
            break
        elif choice.lower() == 'e':
            break
        else:
            print('Please try again.\n')

if __name__ == '__main__':  
    system = {'Dipen': 'fadfa', 'Bowen': 'dffa', 'Babu': 'dafafaa'}
    login() 