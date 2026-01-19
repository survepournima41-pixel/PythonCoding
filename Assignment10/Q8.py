# Write a program to create a duplicate of an existing list it should not point to same list.

list = [10, 20, 30, 40, 50]

duplicate_list = []

for i in range(len(list)):
    duplicate_list.append(list[i])
    
print('Original List:', list)
print('Duplicate List:', duplicate_list)