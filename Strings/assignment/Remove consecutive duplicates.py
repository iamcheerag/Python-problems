# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 12:58:48 2020

@author: cheerag.verma
"""

"""
Problem : Given a string, remove all the consecutive duplicates that are present in the given string.
            That means, if 'aaa' is present in the string then it should become 'a' in the output string
            
Input : aabccbaa
Output: abcba

"""


def removeConsecutiveDuplicates(str_):
    arr=[]
    for i in str_:
        arr.append(i)
        
    if len(arr)>1:
        i = 0
        j = 1
        new_arr = []
        while i < len(arr) and j< len(arr):
            
            if arr[i] !=arr[j]:
                new_arr.append(arr[i])
                i = j
                j+=1
                #print(j)
                if j == len(arr):
                    #print("asdf")
                    new_arr.append(arr[i])
                    break
                    

            
            elif arr[i] == arr[j]:
                j+=1
                
                if j == len(arr):
                    new_arr.append(arr[i])
                    break
    
        
        return new_arr
    
    else:
        return str_
    
inputString = input()
result = removeConsecutiveDuplicates(inputString)
for data in result:
    print("".join(data),end = "")
    
