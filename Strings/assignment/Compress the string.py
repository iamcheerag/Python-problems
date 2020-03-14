# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 15:35:23 2020

@author: cheerag.verma
"""


"""
Program : Write a program to do basic string compression. For a character which is consecutively repeated more than once, replace consecutive duplicate occurrences with the count of repetitions.
            For e.g. if a String has 'x' repeated 5 times, replace this "xxxxx" with "x5"
            
Input : aaabbccdsa
output: a3b2c2dsa
"""

def compressString(str_):
    arr=[]
    
    for i in str_:
        arr.append(i)
        
    if len(arr)>1:
        i = 0
        j = 1
        new_arr = []
        count = 0
        while i < len(arr) and j< len(arr):

            if arr[i] !=arr[j]:
                count = j-i
                if count >1:
                    new_arr.append(arr[i]+str(count))
                
                else:
                    new_arr.append(arr[i])
                i = j
                j+=1
                if j == len(arr):
                    new_arr.append(arr[i])
                    break
                    

            
            elif arr[i] == arr[j]:
                j+=1
        
                if j == len(arr):
                    count=j-i
                    new_arr.append(arr[i]+str(count))
                    break
    
        
        return new_arr
    
    else:
        return str_
    
inputString = input()
result = compressString(inputString)
for data in result:
    print("".join(data),end = "")
    