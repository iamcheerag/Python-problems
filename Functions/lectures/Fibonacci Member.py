# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 09:26:30 2020

@author: cheerag.verma
"""

def checkMember(n):
    num = n
    f1 = 0
    f2 = 1
    if n == 0:
        return True
    for i in range(1,n+1):
        f = f1+f2  
        f1 = f2
        f2 = f

        if num == f1 or num == f2 or num == f:
            return True

n=int(input())

if(checkMember(n)):
    print("true")
else:
    print("false")