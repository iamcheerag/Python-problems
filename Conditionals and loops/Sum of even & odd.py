num = int(input())
sum_even =0 
sum_odd = 0
while num >0 :
    lastdigit = num%10
    
    if lastdigit % 2 == 0 :
        sum_even = sum_even+lastdigit
    else:
        sum_odd = sum_odd + lastdigit
        
    num = num//10

print(sum_even," ",sum_odd)