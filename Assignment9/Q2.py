#Write a program to check if given number is Armstrong or not using recursive
#function.

def count_digits(n):
    if n == 0:
        return 0
    return 1 + count_digits(n // 10)

def sum_of_powers(n, digits):
    if n == 0:
        return 0
    else:
        return (n % 10) ** digits + sum_of_powers(n // 10, digits)
    
def is_armstrong(n):
    digits = count_digits(n)
    return n == sum_of_powers(n, digits)

num = int(input('Enter a number:'))
if is_armstrong(num):
    print(f'{num} is an Armstrong number.')
else:
    print(f'{num} is not an Armstrongnumber.')