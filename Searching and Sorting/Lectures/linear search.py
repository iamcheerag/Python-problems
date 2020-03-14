# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 15:16:09 2020

@author: cheerag.verma
"""


def linearSearch(n,arr,search):
    
    for i in range(n):
        if arr[i] == search:
            print("Element found at {}th position".format(i+1))
            break
    else:
        print("Element Not present in the List")


n = int(input())
listOfElement = [int(x) for x in input().split()]
search = int(input())
linearSearch(n,listOfElement,search)
