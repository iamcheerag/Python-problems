# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 12:36:33 2020

@author: cheerag.verma
"""
def swapAlternate(elem,n):
    i=0
    while i < n-1:
        elem[i],elem[i+1] = elem[i+1],elem[i]
        i+=2
    return elem
    
n = int(input())
elem =[int(x) for x in input().split()]
result = swapAlternate(elem,n)
for i in result:
    print(i,end= " ")