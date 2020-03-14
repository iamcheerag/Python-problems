# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 11:56:01 2020

@author: cheerag.verma
"""

def checkPalindrome(inputString):
    
    reverseString = inputString[::-1]
    
    if inputString == reverseString:
        return True
    else:
        return False
    
inputString = input()
result = checkPalindrome(inputString)
print(result)