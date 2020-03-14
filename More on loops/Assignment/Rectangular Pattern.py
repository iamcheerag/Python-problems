#steps
#1. create a 2d array nxn
#2. at row==first and row==last and col==first and col==last put n
#3....similar steps
n=int(input())
num=n
n=2*n-1
arr=[[0 for i in range(n)] for j in range (n)]
start=0
end=n-1
while (num!=0):
    for i in range(start,end+1):
        for j in range(start,end+1):
            if(i==start or i==end or j==start or j==end):
                arr[i][j]=num
    start+=1
    end-=1
    num-=1



#print array
for i in range(n):
    for j in range(n):
        print(arr[i][j],end='')
    print()
    