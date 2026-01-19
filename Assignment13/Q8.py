# Python Program to Count the Frequency of Words Appearing in a String Using
# a Dictionary

text = input('Enter a string:')

words = text.lower().split()

word_freq = {}

for word in words:
    word_freq[word] = word_freq.get(word, 0) + 1
    
print('Word frequency:')
for word, count in word_freq.items():
    print(word, ':' , count)