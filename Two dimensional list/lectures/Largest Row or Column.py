# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 18:02:33 2020

@author: cheerag.verma
"""
"""
Problem: Given an NxM 2D array, you need to find out which row or column has largest sum (sum of its elements) 
         overall amongst all rows and columns.
         
Input : Line 1 : 2 integers N and M respectively, separated by space 
        Line 2: Single line having N*M elements entered in row wise manner, each separated by space.
        
Output: If row sum is maximum then - "row" row_num max_sum
        If column sum is maximum then - "column" col_num max_sum

"""




def largestRoworCol(arr):
    
    #Row wise Sum
    rowSumList=[]
    for i in range(n):
        sumRow = 0
        for j in range(m):
            sumRow+=arr[i][j]
        rowSumList.append(sumRow)
    print(rowSumList)
    
    
    #Column wise Sum
    colSumList = []
    i=0;j=0
    for j in range(m):
        sumCol = 0
        for i in range(n):
            sumCol+=arr[i][j]
        colSumList.append(sumCol)
    print(colSumList)
    
    maxElementOfRow = max(rowSumList)
    maxElementOfCol = max(colSumList)
    
    if maxElementOfRow >= maxElementOfCol :
        return "row"+" "+str(rowSumList.index(maxElementOfRow))+" "+str(maxElementOfRow)
    
    else:
        return "column"+" "+str(colSumList.index(maxElementOfCol))+" "+str(maxElementOfCol)
    
    

n,m = list(map(int,input().split()))
inputList = [int(x) for x in input().split()]

input2Darr = [[inputList[m*i+j] for j in range(m)]for i in range(n)]

result = largestRoworCol(input2Darr)
print(result)