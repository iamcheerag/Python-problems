"""
A
BC
CDE
DEFG
"""


n = int(input())
row = 1

while row <=n:
    col = 1
    start_char = chr(ord("A")+row-1)
    while col<=row:
        print(chr(ord(start_char)+col-1),end = "")
        col+=1
    print()
    row+=1