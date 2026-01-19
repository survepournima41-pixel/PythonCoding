# Python Program to Remove the Given Key from a Dictionary

my_dict = {
    'name' : 'Pournima',
    'age' : 23,
    'City' : 'Pune'
}

key = input('Enter key to remove:')

removed_value = my_dict.pop(key, 'key not found')

print('Updated Dictionary:', my_dict)