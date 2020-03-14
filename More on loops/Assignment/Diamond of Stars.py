# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 18:05:12 2020

@author: cheerag.verma
"""

n = int(input())

n1 = (n+1)/2
n2 =n-n1


row = 1
while row<=n1:
    spaces = 1
    while spaces <= n1-row:
        print(" ",end = "")
        spaces+=1
    
    star = 1
    while star <= (2*row)-1:
        print("*",end = "")
        star+=1
    
    print()
    row+=1
    
row = n2
while row>=1:
    
    spaces =1 
    while spaces <= n2-row+1:
        print(" ",end = "")
        spaces+=1
        
    star =1
    while star <= (2*row)-1:
        print("*",end = "")
        star+=1  
    
    print()
    row-=1