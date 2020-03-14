# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 11:36:12 2020

@author: cheerag.verma
"""
def sort0and1(n,a):
    i = 0 
    j = n-1
    while(i<j):
        if a[i] == 0:
            i+=1
            
        elif a[j] == 1:
            j-=1
        
        elif a[i]!=0 and a[j]!=1:
            a[i],a[j] = a[j],a[i]
            i+=1
            j-=1
    
    return a

n = int(input())
a = [int(x) for x in input().split()]
resultArray = sort0and1(n,a)

for data in resultArray:
    print(data,end = " ")