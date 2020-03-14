"""
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5
"""


n = int(input())
row = 1

while row <= n:
    col = 1
    while col<=row:
        print(col,end = " ")
        col+=1
    print()
    row+=1
    
    

"""
1 
2 3 
3 4 5 
4 5 6 7 
5 6 7 8 9 
"""


n = int(input())
row = 1
while row <= n:
    col = 1
    count = row
    while col<=row:
        print(count,end = " ")
        count+=1
        col+=1
    print()
    row+=1
    
    
    
"""
1 
2 3 
4 5 6 
7 8 9 10 
11 12 13 14 15
"""

n = int(input())
row = 1
count = row
while row<= n :
    col = 1
    while col<= row:
        print(count,end = " ")        
        count+=1
        col+=1
    print()
    row+=1







