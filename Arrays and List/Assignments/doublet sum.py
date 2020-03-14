# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 10:12:08 2020

@author: cheerag.verma
"""



def doubletSum(n,a,num):
    for i in range(n):
        for j in range(i+1,n):
            if i!=j and a[i]+a[j] == num :
                if a[i] < a[j]:
                    print(a[i],a[j])
                else:
                    print(a[j],a[i])

                  
n = int(input())
arr = [int(x) for x in input().split()]
num = int(input())
doubletSum(n,arr,num)



