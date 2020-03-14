# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 00:34:34 2020

@author: cheerag.verma
"""
n = int(input())
f1 = 1
f2 = 1
i = 0
 
while i < n-2:
    f = f1+f2
    f2=f1
    f1=f
    i+=1

print(f)