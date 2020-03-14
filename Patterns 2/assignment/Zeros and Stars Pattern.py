# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 22:49:07 2020

@author: cheerag.verma
"""

n = int(input())
row = 1
while row<=n:
    col=1
    while col<=n:
        if row == col:
            print("*",end = "")
        else:
            print("0",end = "")
        col+=1
    
    print("*",end = "")
    
    col2=1
    while col2<=n:
        if col2 == n-row+1:
            print("*",end = "")
        else:
            print("0",end = "")
        col2+=1
    
    print()
    row+=1