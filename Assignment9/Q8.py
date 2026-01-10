# 8. Write a program to check whether a number is prime or not using recursion.

def is_prime_recursive(n, i = 2):
    if n <= 1:
        return False
    if i * i > n:
        return True
    if n % i == 0:
        return False
    return is_prime_recursive(n, i + 1)

num = int(input('Enter a number:'))
if is_prime_recursive(num):
    print(f'{num} is a prime number.')
else:
    print(f'{num} is not a prime number.')