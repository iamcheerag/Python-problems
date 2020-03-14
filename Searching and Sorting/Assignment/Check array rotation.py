# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 15:30:26 2020

@author: cheerag.verma
"""

"""
Problem : Given an integer array, which is sorted (in increasing order)
          has been rotated by some number k in clockwise direction. Find and return the k.
          
Input:    6
          5 6 1 2 3 4
          
Output:         2
          

"""

def checkRotation(arr,n):
    i = 0
    while i < n :
        if arr[i] > arr[i+1]:
            return i+1
        else:
            i+=1
    else:
        return 0
    
n = int(input())
arr = [int(x)for x in input().split()]
result = checkRotation(arr,n)
print(result)