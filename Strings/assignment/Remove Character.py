# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 14:10:31 2020

@author: cheerag.verma
"""
"""
Problem : Given a string and a character x. Write a function to remove all occurrences of x character from the 
            given string.Leave the string as it is, if the given character is not present in the string.

Input format :

Line 1 : Input string

Line 2 : Character x

Input : welcome to coding ninjas
        o
Output: welcme t cding ninjas
    
"""


def removeCharacter(s,x):
    print(s.replace(x,""))


inputString = input()
x = input()
removeCharacter(inputString,x)