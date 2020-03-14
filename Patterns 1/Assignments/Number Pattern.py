# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 16:03:11 2020

@author: cheerag.verma
"""

"""
1234
123
12
1
"""

n = int(input())
row = 1
while row<=n:
    col = 1
    while col<=n-row+1:
        print(col,end= "")
        col+=1
    print()
    row+=1