# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 00:03:47 2020

@author: cheerag.verma
"""
"""
          * 
        * * 
      * * * 
    * * * * 
  * * * * * 
* * * * * * 

"""

n = int(input())

row = 1
while row <= n:
    spaces = 1
    while spaces<=n-row:
        print(" ",end =" ")
        spaces+=1
    
    symbol = 1 
    while symbol<=row:
        print("*",end=" ")
        symbol+=1
    
    print()
    row+=1