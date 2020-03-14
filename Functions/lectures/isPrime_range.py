# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 22:32:12 2020

@author: cheerag.verma
"""

def isPrime(n):
    
    for i in range(2,n):
        if n % i == 0:
            #print("Not Prime")
            break
    else:
        #print("Prime")
        return True
    
    return False


def primeRangeFrom2toN(n):
    
    for data in range(2,n):
        prime_range = isPrime(data)
        if prime_range:
            print(data)
            

primeRangeFrom2toN(20)
    
    