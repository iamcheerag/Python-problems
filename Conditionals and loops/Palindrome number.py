# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 00:16:16 2020

@author: cheerag.verma
"""

def checkPalindrome(num):
    copyNum = num
    reverse = 0 
    while num > 0:
        lastdigit = num %10
        reverse = reverse *10 + lastdigit
        num = num //10
    
    if reverse == copyNum:
        return True
    else:
        return False


num = int(input())
isPalindrome = checkPalindrome(num)
if(isPalindrome):
	print('true')
else:
	print('false')