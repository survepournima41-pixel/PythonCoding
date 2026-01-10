#4. Sum of all odd numbers between 1 to n

def sum_of_odd_numbers(n):
    total = 0
    for i in range(1, n+1,2):
        total += i
    return total

n = int(input('Enter a number:'))
print('Sum of odd numbers:', sum_of_odd_numbers(n))