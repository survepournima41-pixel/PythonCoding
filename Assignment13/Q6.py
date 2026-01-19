# Python Program to Multiply All the Items in a Dictionary

my_dict = {
    'a' : 2,
    'b' : 3,
    'c' : 4
}

result = 1
for value in my_dict.values():
    result = result * value
    
print('Product of all items:', result)