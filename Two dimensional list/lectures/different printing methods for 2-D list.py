# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 16:56:47 2020

@author: cheerag.verma
"""

# can used to print normal list as well as jagged list.

li = [[1,2,3],[4,4,],[8,65,5,43,3]]

n = 3
for i in li:
    for j in i:
        print(j,end=" ")
    print()

    

# we can use this method we want to print int as a string and donot want space at the end of the string.
    
    #concept of join 
    "ac".join(['1','2','3','4'])
    #output: '1ac2ac3ac4'
  
       
for row in li:
    out = " ".join([str(j) for j in row])
    print(out)
    