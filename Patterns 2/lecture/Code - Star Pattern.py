# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 00:59:48 2020

@author: cheerag.verma
"""

n = int(input())

row = 1
while row<=n:
    spaces = 1
    while spaces <= n-row:
        print(" ",end = "")
        spaces+=1
    
    symbol = 1
    while symbol<= row :
        print("*",end = "")
        symbol+=1
    
    
    symbol = row-1
    while symbol>=1:
        print("*",end= "")
        symbol-=1
    print()
    row+=1