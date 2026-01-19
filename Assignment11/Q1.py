# Python Program to Put Even and Odd elements of a List into two Different
# Lists

numbers = [10, 21, 4, 45, 66, 93, 1]

even_list = []
odd_list = []

for num in numbers:
    if num % 2 == 0:
        even_list.append(num)
    else:
        odd_list.append(num)
        
print('Even numbers lists:', even_list)
print('Odd numbers lists:', odd_list)