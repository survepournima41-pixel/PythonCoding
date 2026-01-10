#5. Sum of all prime numbers between 1 to n

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def sum_of_prime(n):
    total = 0
    for i in range(2, n + 1):
        if is_prime(i):
            total = total + i
    return total

n = int(input('Enter a number:'))
print('Sum of all prime numbers:', sum_of_prime(n))