"""
A
BB
CCC
DDDD
"""



n = int(input())
row = 1
while row <= n:
    col=1
    start_alpha = chr(ord("A")+row-1)
    while col<=row:
        print(chr(ord(start_alpha)),end = "")
        col+=1
    print()
    row+=1