# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 15:52:58 2020

@author: cheerag.verma
"""
"""
1
11
121
1221
"""

n = int(input())
if n>=1:
    print("1")
    row = 2
    while row<=n:
        col = 1
        while col<=row:
            if col == 1  or col == row:
                print("1",end = "")
            else:
                print("2",end = "")
    
            col+=1
        print()
        row+=1