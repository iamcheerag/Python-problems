# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 14:38:26 2020

@author: cheerag.verma
"""

def findDuplicate(a,n):
    for i in range(n):
        for j in range(n):
            if i!=j and a[i]==a[j]:
                return a[i]
                
    

n = int(input())
a = [int(x) for x in input().split()]
result = findDuplicate(a,n)
print(result)
    