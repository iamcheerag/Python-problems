# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 19:46:20 2020

@author: cheerag.verma
"""

flag = True
while flag:
    choice = int(input())
    if choice < 6:
        n1 = int(input())
        n2 = int(input())
    
        if choice == 1:
            print(n1+n2)
        elif choice == 2:
             print(n1-n2)
        elif choice == 3:
             print(n1*n2)
        elif choice == 4:
            print(n1//n2)
        elif choice == 5:
             print(n1%n2)
        elif choice == 6:
            flag = False
    elif choice == 6:
        flag = False
    
    else:
        print("Invalid Operation")
    

    
    