# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 12:50:33 2020

@author: cheerag.verma
"""

def spiralPrinting(arr):
    
    rowStart = 0
    rowEnd   = n
    colStart = 0
    colEnd   = m
    while rowStart<rowEnd and colStart<colEnd:
      
        for j in range(colStart,colEnd):
          print(arr[rowStart][j],end = " ")
        
        rowStart+=1
        
        for i in range(rowStart,rowEnd):
            print(arr[i][colEnd-1],end=" ")
        colEnd-=1
        
        
        for j in range(colEnd-1,colStart-1,-1):
            print(arr[rowEnd-1][j],end=" ")
        rowEnd-=1
        
        
        for i in range(rowEnd-1,rowStart-1,-1):
            print(arr[i][colStart],end=" ")
        colStart+=1
        
        
    return arr    




inputString = input().split(" ")
n,m = int(inputString[0]),int(inputString[1])
inputList = inputString[2:]
input2DList = [[int(inputList[m*i+j]) for j in range(m)]for i in range(n)]
spiralPrinting(input2DList)
