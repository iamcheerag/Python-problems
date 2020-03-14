# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 23:31:40 2020

@author: cheerag.verma
"""

def selectionSort(a,n):
    for i in range(n-1):
        min_index = i
        for j in range(i+1,n):
            if a[min_index] > a[j]:
                min_index = j
        
        a[i],a[min_index] = a[min_index],a[i]
    
    return a


#n = int(input())
n = 6
a = [13,24,39,0,1,2]
result = selectionSort(a,n)
for data in result:
    print(data,end = " ")