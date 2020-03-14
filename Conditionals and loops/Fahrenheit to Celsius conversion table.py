# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 19:36:17 2020

@author: cheerag.verma
"""

S = int(input())
E = int(input())
W = int(input())

while S<=E:
    c = (S-32)*5/9
    print(S,"\t",int(c))
    S = S+W