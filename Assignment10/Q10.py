# 10. Write a program to remove all occurrences of a given element in the list.

list = [2, 5, 3, 5, 7, 5, 9]

ele = int(input('Enter the element to remove:'))

new_list = []

for i in range(len(list)):
    if list[i] != ele:
        new_list.append(list[i])
        
print('Original list:', list)
print('List after removing all occuerences:', new_list)