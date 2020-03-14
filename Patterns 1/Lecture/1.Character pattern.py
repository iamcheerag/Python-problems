"""
ABCD
ABCD
ABCD
ABCD
"""


n = int(input())
row = 1
while row <= n:
    col=1
    i = 65
    while col<=n:
        print(chr(ord('A')+col-1), end= "")
        col+=1
    print()
    row+=1
    
    
"""
ABCD
BCDE
CDEF
DEFG

"""

n = int(input())
row = 1
while row <= n:
    start_char = chr(ord('A')+row-1)
    col=1
    i = 65
    while col<=n:
        print(chr(ord(start_char)+col-1), end= "")
        col+=1
    print()
    row+=1



