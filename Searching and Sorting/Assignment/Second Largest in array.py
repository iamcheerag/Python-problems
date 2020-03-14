# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 14:22:13 2020

@author: cheerag.verma
"""

"""
problem : Given a random integer array of size n, find and return the second largest element present in the array.
          If n <= 1 or all elements are same in the array, return -2147483648 i.e. -2^31.
          
          7
          2 13 4 1 3 6 28


Output:   13

          """
          
def secondHighestElement(arr,n):
    unique_elements = set(arr)
    
    if n <= 1:
        return -2147483648
    
    elif len(unique_elements) == 1:
        return -2147483648
    
    else:
        list_element = list(unique_elements)
        list_element.sort()
        return list_element[-2]
          
n = int(input())
arr = [int(x)for x in input().split()]
result = secondHighestElement(arr,n)
print(result)
