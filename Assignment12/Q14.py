# Python Program to count the occurrences of ach word in a string.

string = input('Enter a string:')

words = string.split()

words_count = {}

for word in words:
    if word in words_count:
        words_count[word] += 1
    else:
        words_count[word] = 1
        
print('Word Occuernces.')
for word, count in words_count.items():
    print(word, ':', count)