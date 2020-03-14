# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 17:26:08 2020

@author: cheerag.verma
"""

"""
Given a 2D integer array of size M*N, find and print the sum of ith row elements separated by space.
"""

def rowWiseSum(arr):
    newlist = []
    
    for i in arr:
        sum = 0 
        for j in i:
            sum = sum + j 
        newlist.append(sum)
            
    return newlist

#Main
n,m = list(map(int,input().split()))
l = [int(x) for x in input().split()]

arr = [[l[m*i+j] for j in range(m)] for i in range(n)]







