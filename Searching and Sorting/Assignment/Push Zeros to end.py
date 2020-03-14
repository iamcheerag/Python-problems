# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 12:27:35 2020

@author: cheerag.verma
"""

"""
input: Given a random integer array, push all the zeros that are present to end of the array. 
       The respective order of other elements should remain same.
       
        7
        2 0 4 1 3 0 28
       
output: 2 4 1 3 28 0 0

logic : 2 pointer i and j and swap i,j everytime j is 0 and i is non-zero else increment both
"""

def pushZeroToEnd(arr,n):
    i = 0 
    j = 0
    while i<n:
        if arr[i]!=0 and arr[j]!=0:
            i+=1
            j+=1
        
        elif arr[i] == 0:
            i+=1
        
        elif arr[i]!=0 and arr[j] == 0:
            temp = arr[j]
            arr[j] = arr[i]
            arr[i] = temp
        
            j+=1
            i+=1
    
    return arr

n = int(input())
arr = [int(x) for x in input().split()]
result = pushZeroToEnd(arr,n)

for data in result:
    print(data,end= " ")