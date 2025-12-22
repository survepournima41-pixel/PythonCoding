#Write a program to swap two numbers using third variable.
x = int(input('Enter the number:'))
y = int(input('Enter the number:'))

print(f'Before swapping x is {x}, y is {y}')

z = y
y = x
x = z

print(f'After swapping x is {x}, y is {y}')