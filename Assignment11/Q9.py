# 9. Write a program to create three lists of numbers, their squares and cubes

num = []
squares = []
cubes = []

for i in range(1, 11):
    num.append(i)
    squares.append(i * i)
    cubes.append(i * i * i)
    
print('Number:', num)
print('Squares:', squares)
print('Cubes:', cubes)