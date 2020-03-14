# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 23:06:29 2020

@author: cheerag.verma
"""

n = int(input())

row = 1
while row <=n:
    spaces = 1
    while spaces<= n-row:
        print(" ",end = "")
        spaces+=1
    

    symbol = row
    while symbol>=1:
        print(symbol,end = "")
        symbol-=1
    
    symbol = 2
    while symbol <=row:
        print(symbol,end = "")
        symbol+=1
        
    
    print()
    row+=1