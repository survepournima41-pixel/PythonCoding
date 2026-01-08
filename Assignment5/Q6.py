n = int(input('Enter the value of n:'))
count = 0
num = 2

print('First', n, 'Prime numbers are:')

while count < n:
    is_prime = True
    
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
        
    if is_prime:
        print(num, end = ' ')
        count = count + 1
        
    num = num + 1
    