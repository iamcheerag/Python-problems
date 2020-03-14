# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 23:55:17 2020

@author: cheerag.verma
"""
"""
55555
4444
333
22
1

"""

n = int(input())
row = 1
while row<=n:
    col=1
    while col<= n-row+1:
        print(n-row+1,end = "")
        col+=1
    print()
    row+=1