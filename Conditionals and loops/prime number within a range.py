# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 19:34:51 2020

@author: cheerag.verma
"""

n = int(input())
k=2
while k<n:
    i=2
    count = True
    while i<k:
        if k%i==0:
            count = False
        i+=1
        
    if count:
        print(i)
            
    k+=1
    