# Write a program to print list after removing even numbers.

list = [10, 15, 22, 7, 8, 3, 40]

new_list = []

for i in range(len(list)):
    if list[i] % 2 != 0:
        new_list.append(list[i])
        
print('Original list:', list)
print('List after removing even numbers:', new_list)