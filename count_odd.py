n=1234567890
def odd_digits(n):
    count=0
    while n>0:
        temp=n%10
        if temp%2!=0:
            count+=1
        n=n//10
    return count
a=odd_digits(n)
print(a)

#OUTPUT
#5
