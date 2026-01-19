# Python Program to count number of digits and letters in a string.

string = input('Enter a string: ')

letters = 0
digits = 0

for ch in string:
    if ch.isalpha():
        letters = letters + 1
    elif ch.isdigit():
        digits = digits + 1

print('Number of letters:', letters)
print('Number of digits:', digits)