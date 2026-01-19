# Python Program to Sort a List According to the Length of the Elements
# within the list.

words = ['apple', 'banana', 'kiwi', 'cherry', 'fig']

sorted_words = sorted(words, key = len)

print('Sorted list:', sorted_words)