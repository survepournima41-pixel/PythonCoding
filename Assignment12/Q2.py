# Python Program to Remove the nth Index Character from a Non-Empty
# String

text = 'Python'
n =2

result = text[: n] + text[n + 1 :]

print('Original String', text)
print('String after removing character at index', n , ':', result)