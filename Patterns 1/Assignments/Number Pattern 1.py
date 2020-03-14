"""
1
11
111
1111

"""

n = int(input())

row = 1
while row<=n:
    col = 1
    while col<=row:
        print("1",end= "")
        col+=1
    print()
    row+=1