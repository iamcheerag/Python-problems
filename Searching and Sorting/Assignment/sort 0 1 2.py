# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 16:16:23 2020

@author: cheerag.verma
"""

"""
Problem :   You are given an integer array containing only 0s, 1s and 2s. 
            Write a solution to sort this array using one scan only.
            
input :  7
         0 1 2 0 2 0 1
        
output:  0 0 0 1 1 2 2 

1.logic : take temp array , from original if element is 0 copy it to the front ,if 2 copy to back rest in between.
2.logic : take i,nz(next zero),nT(next two) pointers,place i , nz from starting and nT from the back ,now:
    a.if a[i] is 0 --> swapo(nz,i),i++,nz++
    b if a[i] is 1 --> i++ only
    3. if a[i] is 2 --> swap(nT,i) nT-- , and check a[i] if it is 0 or 1 , if 0 repeat step (a) else step (b) 
"""
def sort012(arr,n):
    i=0
    nz=0
    nT=n-1
    while i < n and i <= nT:
        
        if arr[i] == 1:
            i+=1
        
        elif arr[i] == 0:
            arr[nz],arr[i] = arr[i],arr[nz]
            i+=1
            nz+=1
        
        elif arr[i] == 2:
            arr[i],arr[nT] = arr[nT],arr[i]
            
            
            if arr[i] == 0:
                arr[nz],arr[i] = arr[i],arr[nz]
                i+=1
                nz+=1
            elif arr[i] == 1:
                i+=1
                
            nT-=1
                
n = 7
arr = [2,1,0,0,1,2,2]
sort012(arr,n)

 