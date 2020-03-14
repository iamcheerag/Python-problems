# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 13:59:41 2020

@author: cheerag.verma
"""

"""
Problem :  Given a string S, reverse each word of a string individually. For eg. if a string is "abc def", 
           reversed string should be "cba fed".
           
input : Welcome to Coding Ninjas

Output: emocleW ot gnidoC sajniN


"""

def reverseEachWord(s):
    s = s.split()
    for i in s:
        print(i[::-1],end=" ")
    


s = input()
reverseEachWord(s)
