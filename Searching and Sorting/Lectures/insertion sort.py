# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 00:28:19 2020

@author: cheerag.verma
"""

def insertionSort(a,n):
    for i in range(n):
        key = a[i]
        j=i-1
        while j>=0 and a[j] > key:
            a[j+1]=a[j]
            j=j-1
        a[j+1] = key
    return a
        
n = 6
a =[44,3,4,1,9,66]
result = insertionSort(a,n)
for data in result:
    print(data,end=' ')


