# Python Program to Find the Intersection of Two Lists

list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]

intersection_list = []

for element in list1:
    if element in list2 and element not in intersection_list:
        intersection_list.append(element)
        
print('Intersection of the two lists:', intersection_list)