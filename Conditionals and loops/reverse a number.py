n = int(input())
reverse = 0
while n > 0:
    lastdigit = n%10
    reverse = (reverse*10)+ lastdigit
    n = n/10

print(reverse)



