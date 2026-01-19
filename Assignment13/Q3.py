# Python Program to Check if a Given Key Exists in a Dictionary or Not

my_dict = {
    "name" : "pournima",
    "age" : 23, 
    "City" : "Pune"
}

key = input('Enter key to check:')

if key in my_dict:
    print('Key exists in the dictionary.')
else:
    print('Key dose not exists in the dictionary.')
    