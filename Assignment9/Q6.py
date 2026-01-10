# Write a program to print Fibonacci series using recursion.

def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    
n_terms = int(input('Enter number of terms:'))
print('Fibonacci series:')
for i in range(1, n_terms + 1):
    print(fibonacci(i), end = ' ')