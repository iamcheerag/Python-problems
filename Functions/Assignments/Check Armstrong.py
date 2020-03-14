# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 22:34:06 2020

@author: cheerag.verma
"""

def isArmstrong(n):
    power = len(str(n))
    sum = 0
    rem = 0
    while n>=1:
        rem = n % 10
        sum = sum + rem**power
        n=n//10
    return sum
    
n = int(input())
result = isArmstrong(n)
if result == n:
    print("true")
else:
    print("false")
