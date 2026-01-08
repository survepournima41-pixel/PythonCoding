#WAP to check if given number is Perfect Number.

num = int(input('Enter the number:'))
div = 0

for i in range(1, num):
    if num % i == 0:
        div = div + i
        
if div == num:
    print("Perfect number is a:", num)
else:
    print('Not perfect number is a:', num)
    
    