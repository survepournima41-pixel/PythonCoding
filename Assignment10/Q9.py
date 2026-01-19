# Write a program of having n number of elements in the list and find out even
# and odd elements in that list and then create two separate lists which will have
# even elements and other will have odd elements.

n = int(input('Enter number of element in the list:'))

list = []

for i in range(n):
    num = int(input(f'Enter number {i + 1}:'))
    list.append(num)
    
even_list = []
odd_list = []

for i in range(len(list)):
    if list[i] % 2 == 0:
        even_list.append(list[i])
    else:
        odd_list.append(list[i])

print('Original list:', list)
print('Even element list:', even_list)
print('Odd element list:', odd_list)