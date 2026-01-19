# Write a program to create a new list from existing list which contains cube of each number.

list = [1, 2, 3, 4, 5]

cube_list = []

for i in range(len(list)):
    cube = list[i] * list[i] * list[i]
    cube_list.append(cube)
    
print('Original List:', list)
print('New list with cube:', cube_list)