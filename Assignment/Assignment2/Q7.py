# Find the sum of three-digit number.

num = int(input('Enter the number:'))

a = num // 100
b = (num //10) % 10
c = num % 10

# Calculate the sum of digit

sum_of_digit = a + b + c

print('Sum of digit =' , sum_of_digit)