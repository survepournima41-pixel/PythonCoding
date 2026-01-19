# 10. Write a program to print list after removing even numbers.

num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = []

for n in num:
    if n % 2 != 0:
        result.append(n)

print('List after removing even numbers',result )