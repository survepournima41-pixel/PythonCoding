#Write a program to find sum of n numbers using recursion.

def sum_n_numbers(n):
    if n == 0:
        return 0
    else:
        return n + sum_n_numbers(n - 1)
    
num = int(input('Enter a number:'))
total = sum_n_numbers(num)
print(f'Sum of first {num} numbers is : {total}')