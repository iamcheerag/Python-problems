# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 20:23:38 2020

@author: cheerag.verma
"""


def checkPalindrome(num):
    digit = num
    rev = 0
    while num>=1:
        rem = num % 10
        rev = rev * 10 + rem
        num = num //10
    
    if digit == rev:
        return True
    else:
        return False
		
num = int(input())
isPalindrome = checkPalindrome(num)
if(isPalindrome):
	print('true')
else:
	print('false')
