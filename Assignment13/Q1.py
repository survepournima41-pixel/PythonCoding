# Python Program to Add a Key-Value Pair to the Dictionary

my_dict = {
    "name" :"Pournima",
    "age" : 23
}

key = input('Enter key:')
value = input('Enter value:')

my_dict.update({key: value})

print('Udated dictionary:', my_dict)