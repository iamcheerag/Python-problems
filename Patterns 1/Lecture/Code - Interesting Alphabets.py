"""
E
DE
CDE
BCDE
ABCDE
"""

n = int(input())
row = 1
i=1
while row <=n:
    col = 1
    start_char = chr(ord("A")+n-i)
    while col<=row:
        print(chr(ord(start_char)+col-1),end = "")
        col+=1
    print()
    row+=1
    i+=1
    