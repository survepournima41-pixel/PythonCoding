# Python Program to Sort the List According to the Second Element in Sublist

list_of_lists = [[1, 3], [4, 1], [2, 2], [5, 0]]

sorted_list = sorted(list_of_lists, key = lambda x : x[1])

print('Sorted list:', sorted_list)