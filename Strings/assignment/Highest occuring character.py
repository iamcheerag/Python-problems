# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 15:09:31 2020

@author: cheerag.verma
"""
d={}
str_ = "cheerrag"
count = 1

for i in str_:
    if i in d:
        d[i] = d[i]+1
    else:
        d[i] = count
        
list_ = sorted(d.items(),key=lambda x: x[1])
print(list_[-1][0])




s=input()
f=[0]*256
for i in s:
    f[ord(i)]+=1

ans=s[0]
count=f[ord(s[0])]

for i in range(1,len(s)):
    if f[ord(s[i])]>count:
        ans=s[i]
        count=f[ord(s[i])]
print(ans)
