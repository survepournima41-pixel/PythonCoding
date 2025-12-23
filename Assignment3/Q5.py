# Write a program to check whether the triangle is equilateral, isosceles or scalene
# triangle.
#equilateral = all three sides are equal.
#isosceles = any two sides are equal.
#Scalene = all sides are different.

a1 = int(input('Enter the first angle:'))
a2 = int(input('Enter the second angle:'))
a3 = int(input('Enter the third angle:'))

if a1 == a2 == a3:
    print('Triangle is equilateral.')
    
if a1 == a2 or a2 == a3 or a3 == a1:
    print('Triangle is isosceles.')
        
else:
    print('Triangle is a Scalene.')
    