# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 12:43:45 2020

@author: cheerag.verma
"""

"""
problem : Given a random integer array of size n, write a function that rotates the given array by d elements
         (towards left)
         
         7
         1 2 3 4 5 6 7
         2
         
output: 3 4 5 6 7 1 2 """



def rotateArray(n,input_arr,d):
    arr = []
    for data in range(d,n):
        arr.append(input_arr[data])
        
    for data in range(d):
        arr.append(input_arr[data])
        
    return arr

n = int(input())
input_arr = [int(x)for x in input().split()]
d = int(input())
if d < len(input_arr):
    result = rotateArray(n,input_arr,d)
    print(*result)