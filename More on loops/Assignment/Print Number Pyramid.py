n = int(input())

row = 1
while row<=n:
    
    spaces = 1
    while spaces <= row-1:
        print(" ",end = "")
        spaces+=1
    
    symbol = row
    while symbol <= n:
        print(symbol,end="")
        symbol+=1
    
    print()
    row+=1

row2 = n-1
while row2 >=1:
    
    spaces = 1
    while spaces <= row2-1:
        print(" ",end = "")
        spaces+=1
    
    symbol = row2
    while symbol <= n:
        print(symbol,end="")
        symbol+=1
    
    print()
    row2-=1
    