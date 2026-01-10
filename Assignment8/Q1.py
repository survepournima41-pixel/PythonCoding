# Write a program to calculate area of rectangle

def area_of_rectangle(length, width):
    return length * width

l = int(input('Enter length:'))
w = int(input('Enter width:'))

area = area_of_rectangle(l, w)

print('Area of rectangle=', area)