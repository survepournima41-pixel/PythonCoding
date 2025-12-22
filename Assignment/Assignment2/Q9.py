#Write a program to swap two numbers without using third variable.

x = int(input('Enter the number:'))
y = int(input('Enter the number:'))
 
print(f'Befor the swapping x is{x}, y is{y}.')

y = x + y
x = y - x
y = y - x

print(f'After swapping x is {x}, y is {y}.')