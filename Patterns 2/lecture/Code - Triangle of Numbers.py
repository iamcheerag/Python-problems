# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 01:05:54 2020

@author: cheerag.verma
"""
"""


"""

# =============================================================================
# n = int(input())
# 
# row = 1
# while row<=n:
#     spaces = 1
#     while spaces <= n-row:
#         print(" ",end = "")
#         spaces+=1
#     
#     symbol = 1
#     count=row
#     while symbol<= row :
#         print(count,end = "")
#         count+=1
#         symbol+=1
#     
# 
#     symbol = 2*(row-1)
#     while symbol>=row:
#         print(symbol,end= "")
#         symbol-=1
#     
#     print()
#     row+=1
# =============================================================================

# =============================  Method 2 ================================================

n = int(input())

row = 1
while row <= n:
    spaces = 1
    while spaces <= n-row:
        print(" ",end = "")
        spaces+=1
    
    star = 1
    while star <= 2*row-1:
        print("*",end = "")
        star+=1
    
    print()
    row+=1
    
    
# =============================================================================