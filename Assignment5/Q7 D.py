# S = a + a2 / 2 + a3 / 3 + ...... + a10 / 10.abs

a = float(input('Enter the value of a:'))

sum = 0

for i in range(1, 11):
    sum = sum + (a ** i) / i
    
print('Sum of the series =', sum)