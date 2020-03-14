# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 13:01:46 2020

@author: cheerag.verma
"""

n = int(input())
a = [int(x) for x in input().split()]

for i in range(n):
    for j in range(n):
        if i!=j and a[i]==a[j]:
            break
    else:
        print(a[i])
            