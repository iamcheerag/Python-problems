"""

1
22
333
4444

"""

n = int(input())
row = 1

while row <= n:
    col=1
    while col<=row:
        print(row,end= "")
        col+=1
    print()
    row+=1