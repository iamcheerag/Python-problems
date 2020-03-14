# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 15:56:40 2020

@author: cheerag.verma
"""


"""
Problem :   Given two strings, check if they are permutations of each other. Return true or false.
            Permutation means - length of both the strings should same and should contain same set of characters. 
            Order of characters doesn't matter.

input : abcde
        baedc
        
output: true


"""


str1 = "abcf"
str2 = "cbad"
if len(str1)!= len(str2):
    print("false")

else:  
    for i in str2:
        if i not in str1:
            print("false")
            break
    else:
        print("true")