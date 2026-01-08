# WAP to print Fibonacci series upto n.
n = int(input('Enter number of terms:'))

a, b = 0, 1
i = 0
print('Fibonacci Series:')

while i < n:
    print(a, end = ' ')
    a, b = b, a + b
    i += 1
    
    