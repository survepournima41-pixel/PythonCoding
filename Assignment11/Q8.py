# Print 1 to 100 in snakes and ladder pattern.

num = 1

for row in range(10):
    row_numbers = []
    
    for col in range(10):
        row_numbers.append(num)
        num = num + 1
        
    if row % 2 != 0:
        row_numbers.reverse()
        
    for n in row_numbers:
        print(f'{n : 3}', end = ' ')
    print()