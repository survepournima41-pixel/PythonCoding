# Write a program to create three lists of numbers, their squares
# and cubes

numbers = [1, 2, 3, 4, 5]

squares = []
cubes = []

for i in range(len(numbers)):
    sq = numbers[i] * numbers[i]
    cu = numbers[i] * numbers[i] * numbers[i]
    squares.append(sq)
    cubes.append(cu)
    
print('Numbers list:', numbers)
print('Squares list:', squares)
print('Cubes list:', cubes)