# Python Program to Find the Second Largest Number in a List Using Bubble
# Sort

numbers = [10, 45, 23, 89, 12]

n = len(numbers)

for i in range(n):
    for j in range(0, n - i - 1):
        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1],numbers[j]
            
print('Second largest number:',numbers[-2])