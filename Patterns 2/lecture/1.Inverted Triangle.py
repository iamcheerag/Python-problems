"""
* * * * * 
* * * * 
* * * 
* * 
* 
"""

n = int(input())
row = 1
while row<=n:
    col=1
    while col<=n-row+1:
        print("*",end = " ")
        col+=1
    print()
    row+=1