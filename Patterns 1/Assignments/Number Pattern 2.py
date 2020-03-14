"""
1
11
202
3003
"""

n = int(input())
print("1")

row = 2
while row<=n:
    col = 1
    while col<=row:
        if col == 1  or col == row:
            print(row-1,end = "")
        else:
            print("0",end = "")

        col+=1
    print()
    row+=1