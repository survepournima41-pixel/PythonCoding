# Python Program to Detect if Two Strings are Anagrams

str1 = 'listen'
str2 = 'silent'

str1 = str1.replace(' ', ' ').lower()
str2 = str2.replace(' ', ' ').lower()

if sorted(str1) == sorted(str2):
    print('The strings are anagrams')
else:
    print('The string are not anagrams')