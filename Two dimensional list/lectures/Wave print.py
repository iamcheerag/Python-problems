# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 21:37:16 2020

@author: cheerag.verma
"""

def wavePrint(arr):
    for j in range(m):
        
        if j%2 == 0 or j == 0:
            for i in range(n):
                print(arr[i][j],end=" ")
                
        
        else:
            for i in range(n-1,-1,-1):
                print(arr[i][j],end=" ")
            
          
inputString = input().split()
n,m = int(inputString[0]),int(inputString[1])
inputList = inputString[2:]
input2DList = [[int(inputList[m*i+j])for j in range(m)]for i in range(n)]
wavePrint(input2DList)
    
    
    
    
    
    
