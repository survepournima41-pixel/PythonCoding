# Python Program to count number of lowercase characters in a string.

string = input('Enter the string:')

count = 0

for ch in string:
    if ch.islower():
        count = count + 1
        
print('Number of lower characters:', count)

