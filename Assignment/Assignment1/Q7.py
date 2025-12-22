#Program to Find the Roots of a Quadratic Equation
#Equation = 2x**2-7x+3=0
# Comparing equation with ax**2 + bx + c = 0
#***why= we use import math because python dose not have a built-in square root function by default.

a = 2
b = 7
c = 3


a =int(input('Enter the a:'))
b =int(input('Enter the b:'))
c =int(input('Enter the c:'))

# Calculate

root1 = (-b + (0.5*b**2)-4*a*c) / (2*a)
root2 =(-b - (0.5*b**2)-4*a*c) / (2*a)
print('Root1 is = ', root1)
print('Root2 is = ', root2)









