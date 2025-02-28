n=123
reverse=0
while n>0:
    digit=n%10
    reverse=reverse*10+digit
    n=n//10
print("reverse numbered:" +str(reverse))

n=int(input())
print(str(abs(n))[::-1])

#OUTPUT
reverse numbered:321
