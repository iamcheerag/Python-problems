# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 22:53:25 2020

@author: cheerag.verma
"""

"""
Problem : 
Two random integer arrays are given A1 and A2, in which numbers from 0 to 9 are present at every index 
(i.e. single digit integer is present at every index of both given arrays).
You need to find sum of both the input arrays (like we add two integers) and put the result in another array 
i.e. output array (output arrays should also contain only single digits at every index).
The size A1 & A2 can be different.
Note : Output array size should be 1 more than the size of bigger array and place 0 at the 0th index if there 
is no carry. No need to print the elements of output array.

Input : 
        3
        6 2 4
        3
        7 5 6

Output: 1 3 8 0
"""

def sumof2Arrays(arr1,arr2,n1,n2):
    i = 1
    j = 1
    carry = 0 
    sumList = []
    
    while i <= n1 and j <= n2:
        num = carry + arr1[-i] + arr2[-j]
        #max_n = max(n1,n2)

        if num >= 10 :
            carry = num//10
            num = num % 10 
    
        else:
            carry = 0 
    
        i+=1
        j+=1
        sumList.append(num)
        
        
    while i <= n1:
        sumList.append(arr1[-i]+carry)
        i+=1
        carry = 0
        
        
    while j <= n2:
        sumList.append(arr2[-j]+carry)
        j+=1
        carry = 0
   
    sumList.append(carry)
    
    return sumList
        
#n1 = int(input())
#arr1 = [int(x) for x in input().split()]
#n2 = int(input())
#arr2 = [int(x) for x in input().split()]

n1 = 4
n2 = 3
arr1 = [3,4,5,7]
arr2 = [9,3,3]
result = sumof2Arrays(arr1,arr2,n1,n2)

print(*result[::-1])
    
    
    