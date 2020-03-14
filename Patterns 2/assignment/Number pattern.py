# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 08:42:35 2020

@author: cheerag.verma
"""

n = int(input())

row = 1
while row <= n:
    
    col =1
    while col <= row:
        print(col,end = "")
        col+=1

    
    spaces = 1
    while spaces<=2*(n-row):
        print(" ",end = "")
        spaces+=1
    
    
    col2 = row
    while col2>=1:
        print(col2,end="")
        col2-=1
    
#    col2 = 1
#    while col2<=row:
#        print(col2,end = "")
#        col2+=1
    
    print()
    row+=1