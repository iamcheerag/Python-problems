# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 12:13:08 2020

@author: cheerag.verma
"""

#n = int(input("Rows"))
#m = int(input("Columns"))

n = 2
m = 3

newlist = [[input().split() for j in range(m)]for i in range(n)]  # this restict to m,n


new_list = [[int(j) for j in input().split()]for i in range(n)]  # this method is useful in case of jagged list



# now if you want to take input for n = 2 , m = 3
# 1,2,3,4,5,6 - > [[1,2,3],[4,5,6]]

b = input().split()
new_list = [[int(b[m*i+j])for j in range(m)]for i in range(n)]


#input : 3 3 1 2 3 45 6 7 89 9 99

#now n ,m and list are given in the same line
inputString = input().split()
n,m = int(inputString[0]), int(inputString[1])

b = inputString[2:]
newList = [[int(b[m*i+j])for j in range(m)]for i in range(n)]


