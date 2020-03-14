n = int(input())

row = 1
while row <=n:
    col = 1
    while col<= n-row+1:
        if row%2!=0:
            print("1",end="")
        else:
            print("0",end = "")
        
        col+=1
    
    print()
    row+=1