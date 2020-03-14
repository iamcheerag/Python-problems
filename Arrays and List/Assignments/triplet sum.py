# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 10:45:33 2020

@author: cheerag.verma
"""

def doubletSum(n,a,num):
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                
                if i!=j!=k and a[i]+a[j]+a[k] == num :
                    
                    
                    if a[i] > a[j] and a[i] > a[k] and a[j]>a[k]:
                        print(a[k],a[j],a[i])
                    
                    elif a[i] > a[j] and a[i] > a[k] and a[j]<a[k]:
                        print(a[j],a[k],a[i])
                    
                    elif a[j]>a[i] and a[j]>a[k] and a[k]>a[i] :
                        print(a[i],a[k],a[j])
                        
                    elif a[j]>a[i] and a[j]>a[k] and a[k]<a[i] :
                        print(a[k],a[i],a[j])
                    
                    elif a[k]>a[i] and a[k]>a[j] and a[i]>a[j]:
                        print(a[j],a[i],a[k])
                    
                    elif a[k]>a[i] and a[k]>a[j] and a[i]<a[j]:
                        print(a[i],a[j],a[k])

                  
n = int(input())
arr = [int(x) for x in input().split()]
num = int(input())
doubletSum(n,arr,num)

#70
#9 5 7 27 22 21 2 7 10 12 3 26 10 19 18 24 9 30 12 18 12 13 11 18 3 3 12 22 29 19 11 21 29 3 1 9 5 26 29 23 30 27 8 11 12 20 5 28 5 3 11 22 18 24 12 29 25 17 29 18 20 18 25 27 10 5 30 29 5 14 
#66