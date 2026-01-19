# Accept a number from user and check if this element is present in the list.

list = [2, 5, 3, 5, 7, 5, 9]

num = int(input('Enter a number to search:'))

count = 0

for i in range(len(list)):
    if list[i] == num:
        count = count + 1
        
if count > 0:
    print(num,'is present in the list.')
    print('It appears', count ,'times.')
else:
    print(num,'is not present in the list.')    
