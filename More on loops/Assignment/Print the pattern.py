# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 18:55:57 2020

@author: cheerag.verma
"""

n = int(input())

if n % 2 == 0:
    n1 = n/2
else:
    n1 = (n+1)/2

n2 = n-n1
row = 1
count = 1
while row<=n1:
    col = 1
    while col<=n:
        print(count,end = " ")
        col+=1
        count+=1
    
    count+=n
    print()    
    row+=1
        

row = 1
if n % 2 !=0:
    count = count -(3*n) # in case of it always decreasing by 3n times 
else:
    count = count - n   
    
while row <= n2:
    col=1
    while col <= n:
        print(count,end = " ")
        col+=1
        count+=1
        
    count = count -(3*n) #odd
    
    print()
    row+=1
    
        
        

 