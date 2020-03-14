# =============================================================================
# """
# 
# 
# """
# n = int(input())
# row = 1
# while row <= n :
#     
#     #upper half
#     spaces = 1
#     while spaces <= n-row:
#         print(" ",end = "")
#         spaces+=1
#     
#     symbol = 1
#     while symbol <= row:
#         print("*" ,end = "")
#         symbol+=1
#     
#     
#     symbol = 2*(row-1)
#     while symbol>=row:
#         print("*",end= "")
#         symbol-=1
#     
#     #lower half
#     
# #    spaces = 1
# #    while spaces <= row:
# #        print(" ",end = "")
# #        spaces+=1
# #        
# #    symbol = 1
# #    while symbol <= n-row:
# #        print("*" ,end = "")
# #        symbol+=1
# #    
# #    
# #    
#     
#     print()
#     row+=1
# =============================================================================



n = int(input())
row =1 
n1=(n+1)/2
n2=n-n1
while row <= n1 :

    #Upper half of the diamond
    spaces = 1
    while spaces <=n1-row:
        print(" ",end = "")
        spaces+=1
        
    star = 1
    while star <= 2*row-1:
        print("*",end = "")
        star +=1

    print()
    row+=1

row=n2
while row>=1:
    #lower half of the diamond
    spaces = 1
    while spaces <= n2-row+1:
        print(" ",end = "")
        spaces+=1
        
    star = 1
    while star <= 2*row-1:
        print("*",end = "")
        star +=1
    
    print()
    row-=1
    





















