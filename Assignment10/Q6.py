# Write a program to remove duplicates from the list.

list = [2, 5, 3, 5, 7, 5, 9, 2]

new_list = []

for i in range(len(list)):
    found = False
    for j in range(len(new_list)):
        if list[i] == new_list[j]:  
            found = True
            break
    if not found:
        new_list.append(list[i])
        
print('List after removing duplicates.')
print(new_list)