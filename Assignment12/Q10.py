# 10.Python Program to Take in Two Strings and Display the Larger String
# without Using Built-in Functions

str1 = input('Enter first string:')
str2 = input('Enter second string:')

count1 = 0
for _ in str1:
    count1 = count1 + 1
    
count2 = 0
for _ in str2:
    count2 = count2 + 1

if count1 > count2:
    print('Large String is:', str1)
elif count2 > count1:
    print('Large string is:', str2)
else:
    print('Both string are of equal length.')