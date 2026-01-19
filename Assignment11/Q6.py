# Python Program to Find the Union of two Lists

list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]

union_list = list1.copy()

for element in list2:
    if element not in union_list:
        union_list.append(element)
        
print('Union of the two lists:', union_list)
    