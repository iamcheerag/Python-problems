"""
1
21
321
4321

"""

n = int(input())
row = 1

while row <= n:
    col=1
    count = row
    while col<=row:
        print(count,end= "")
        col+=1
        count-=1
    print()
    row+=1