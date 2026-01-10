# Write a program to calculate the m to the power n using recursion.

def power(m, n):
    if n == 0:
        return 1
    elif n > 0:
        return m * power(m, n - 1)
    else:
        return 1 / power(m, -n)
    
m = float(input('Enter the base (m):'))
n = int(input('Enter the exponent(n):'))
result = power(m, n)
print(f'{m}^{n} = {result}')