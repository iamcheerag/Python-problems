def listSum(n,elements):
    sum_ = 0 
    for data in elements:
        sum_ = sum_ + data
        
    return sum_
    
lenghtOfList = int(input())
#elements = list(map(int,input().split(" ")))
elements = [int(x) for x in input().split()]
result = listSum(lenghtOfList,elements)
print(result)

#data = []
#for i in input().split():
#    data.append(int(i))