# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 00:52:15 2020

@author: cheerag.verma
"""
"""
          1 
        1 2 1 
      1 2 3 2 1 
    1 2 3 4 3 2 1 
  1 2 3 4 5 4 3 2 1 
1 2 3 4 5 6 5 4 3 2 1 

"""

n = int(input())

row = 1
while row <= n:
    
    #spaces
    spaces = 1
    while spaces<=n-row:
        print(" ",end =" ")
        spaces+=1
    
    #increment sequence
    symbol = 1 
    while symbol<=row:
        print(symbol,end=" ")
        symbol+=1
    
    #decrement sequence
    symbol = row-1
    while symbol >= 1:
        print(symbol,end=" ")
        symbol-=1
    
    print()
    row+=1