# WAP to check if given number Strong Number.
sum = 0
num = int(input('Enter the number:'))
n = num
while(n):
    i = 1 
    f = 1
    r = n % 10
    while(i<=r):
        f = f*i
        i = i+1
    sum = sum + f
    n //= 10

if(sum == num):
    print("The number is a strong number:")
else:
    print("The number is not a strong number:")
    