# Python Program to find larger string without using built-in functions.

str1 = input('Enter the first string:')
str2 = input('Enter the second string:')

len1 = 0
for _ in str1:
    len1 = len1 + 1
    
len2 = 0
for _ in str2:
    len2 = len2 + 1
    
if len1 > len2:
    print('Larger string is:', str1)
elif len2 > len1:
    print('Larger string is:', str2)
else:
    print('Both string are of equal length.')