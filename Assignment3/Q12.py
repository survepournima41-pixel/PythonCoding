# Write a program to check if given 3 digit number is a palindrome or not.

num = int(input("Enter a three digit number: "))

# convert to floor division / modulus
a = num // 100
b = (num // 10) % 10
c = num % 10

# Reverse the number
reverse = c * 100 + b * 10 + a

# Check palindrome
if num == reverse:
    print("The number is a palindrome.")
else:
    print("The number is not a palindrome.")