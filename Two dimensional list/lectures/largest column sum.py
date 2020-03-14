# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 19:43:53 2020

@author: cheerag.verma
"""

def largestColumnSum(arr):
    
    j=0
    newlist = []
    for row in arr:
        sum = 0
        i=0
        for col in row:
            sum = sum + arr[i][j]
            i+=1
        j+=1
        newlist.append(sum)
    return max(newlist)

n= 3
m = 3
l = [int(x) for x in input().split()]
arr = [[l[m*row+col] for col in range(m)]for row in range(n)]

result = largestColumnSum(arr)
print(result)


    

