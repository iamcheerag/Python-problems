# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 09:06:13 2020

@author: cheerag.verma
"""




def printTable(start,end,step):
#Implement Your Code Here
    for i in range(start,end,step):
        celsius  = (i-32) * 5/9
        celsius = int(celsius)
        print(str(i)+"\t"+str(celsius))
        
	   
s = int(input())
e = int(input())
step = int(input())
printTable(s,e,step)





