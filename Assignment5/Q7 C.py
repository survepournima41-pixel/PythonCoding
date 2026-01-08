# c. Find the sum of a geomateric series from 1 to n where the common ratio is 2.

n = int(input('Enter the value of n:'))

sum = 0
term = 1

for i in range(n):
    sum = sum + term
    term = term * 2
    
print('Sum of the geomateric series=', sum)

