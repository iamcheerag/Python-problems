# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 23:47:19 2020

@author: cheerag.verma
"""


def bubbleSort(a,n):
    for i in range(n-1):
        for j in range(n-i-1):
            if a[j] > a[j+1]:
                a[j],a[j+1] = a[j+1],a[j]
    
    return a


#n = int(input())
n = 6
a = [13,24,39,0,1,2]
result = bubbleSort(a,n)
for data in result:
    print(data,end = " ")