# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 15:16:01 2020

@author: cheerag.verma
"""
#
#n1 = int(input())
#ele1 = [int(x) for x in input().split()]
#n2 = int(input())
#ele2 = [int(x) for x in input().split()]




def arrayIntersection(a1,a2,n1,n2):
    a1.sort()
    a2.sort()
    i =0
    j = 0
    while i<n1 and j<n2:
        if a1[i] == a2[j]:
            #print("earth")
            print(a1[i])
            i+=1
            j+=1
        elif a1[i]<a2[j]:
            i+=1
            #print("mars")
        else:
            #print("saturn")
            j+=1
#        elif a2[j]>a1[i]:
#            j+=1



n1 = 5
ele1 = [2,6,2,3,2]
n2 = 3
ele2 = [3,2,2]

arrayIntersection(ele1,ele2,n1,n2)