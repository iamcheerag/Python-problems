"""
1111
2222
3333
4444

"""



n = int(input())

row = 1
while row <= n:
    col=1
    while col<=n:
        print(row,end= "")
        col+=1
    print()
    row+=1
    
    
"""
123456
123456
123456
123456
123456
123456
"""
n = int(input())

row =1
while row <=n:
    col = 1
    while col<=n:
        print(col,end = "")
        col+=1
    print()
    row+=1
    
    
"""
4321
4321
4321
4321

"""
    
n = int(input())
row = 1
while row <=n:
    col = 1
    while col <=n:
        print(n-col+1,end = "")
        col+=1
    print()
    row+=1