#Write a Program to input two angles from user and find third angle of the
#triangle.
#x+y+z=180 find the third angle triangle
a1= 75
a2= 35
a1=int(input('Enter the first angle of triangle:'))
a2=int(input('Enter the second angle of triangle:'))

# let third angle is x
x = a1 + a2 == 180
x = 180 - (a1 + a2)
print(x)


print(f'Angle of triangle a1 is {a1}, a2 is a {a2} x is {x}.')


