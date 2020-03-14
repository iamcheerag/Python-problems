# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 23:27:01 2020

@author: cheerag.verma
"""
"""
*
 * *
   * * *
     * * * *
   * * *
 * *
*
"""

n = int(input())
n1 = (n+1)/2
n2= n-n1

row=1
while row <= n1:
    
    spaces = 1
    while spaces <= row-1:
        print(" ",end = "")
        spaces+=1
    
    star_symbol = 1
    while star_symbol<=row:
        print("* ",end = "")
        star_symbol+=1
    
    print()
    row+=1

row = n2
while row >=1:
    
    spaces = 1
    while spaces <= row-1:
        print(" ",end = "")
        spaces+=1
    
    star_symbol = row
    while star_symbol>=1 :
        print("* ",end="")
        star_symbol-=1
    
    print()
    row-=1
    

i=1
while i<5:
    if i==3:
        continue
    print(i,end=" ")
    i = i + 1
    
    