# 11. Write a program to print all numbers which are divisible by m and n in the
# list.

list = [10, 15, 20, 30, 40, 60, 90]

m = int(input('Enter value of m:'))
n = int(input('Enter value of n:'))

print('Number divisible by', m ,'add', n, 'are:')

for i in range(len(list)):
    if list[i] % m == 0 and list[i] % n == 0:
        print(list[i])