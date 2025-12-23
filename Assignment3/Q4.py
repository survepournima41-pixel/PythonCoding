# Write a program to input all sides of a triangle and check whether triangle is valid or
# not.
a1 = int(input('Enter the first angle:'))
a2 = int(input('Enter the second angle:'))
a3 = int(input('Enter the third angle:'))

if a1 > 0 and a2 > 0 and a3> 0 and (a1 + a2 > a3 )and (a1 + a3 > a2) and (a2 + a3 > a1):
    print('Triangle is a valid.')
else:
    print('Triangle is not valid.')
    