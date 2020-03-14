# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 15:24:02 2020

@author: cheerag.verma
"""

def binarySearch(start,end,arr,element):
    
    while start <= end :
        mid = (start + end) //2
        
        if arr[mid] > element: #right half
            end = mid - 1
            
            #return binarySearch(start,end,arr,element)
        
        elif arr[mid] < element: #left half
            start = mid +1
            #return binarySearch(start,end,arr,element)
        
        
        elif element == arr[mid]:
            print(mid)
            break
    else:   
        print("-1")


n = int(input())
arr = [int(x) for x in input().split()]
x = int(input())
start = 0
end = n -1

binarySearch(start,end,arr,x)