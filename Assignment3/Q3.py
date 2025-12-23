# Write a program to input angles of a triangle and check whether triangle is valid or not.
a1 = int(input('Enter the first angle:'))
a2 = int(input('Enter the second angle:'))
a3 = int(input('Enter the third angle:'))
angle = a1, a2, a3


if(a1 > 0, a2 > 0, a3 > 0):
    angle = (a1 + a2 + a3 == 180)
    print('Angle of triangle is valid', angle)
else:
    print('Angle of triangle is not valid', angle)
    