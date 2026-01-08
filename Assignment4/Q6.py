# WAP to check if a given number is prime number or not.
n = int(input('Enter the number:'))

i = 2

while n % i == 0:
    print(f'{n} is Prime Number.')
    break
    
else:
    print(f'{n} is Not prime number.')