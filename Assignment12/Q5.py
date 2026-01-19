# Python Program to Count the Number of Vowels in a String

text = 'Python Program'

vowels ='aeiouAEIOU'

count = 0

for char in text:
    if char in vowels:
        count = count + 1

print('Number of vowels:', count)