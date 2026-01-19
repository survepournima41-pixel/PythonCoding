# Python Program to Calculate the Number of Words and the Number of
# Characters Present in a String

text = 'Python is very easy.'

words = text.split()
num_Words = len(words)

num_chars = 0
for char in text:
    if char != ' ':
        num_chars = num_chars + 1
        
print('Number of words:', num_Words)
print('Number of characters(excluding spaces):', num_chars)

