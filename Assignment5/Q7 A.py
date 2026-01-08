# a. 1!+2!+3!+4!+.....n!

n = int(input('Enter the number of n:'))

fact = 1
sum_fact = 0

for i in range(1, n + 1):
    fact = fact * i
    sum_fact = sum_fact + fact
    
print('Sum of factorials=', sum_fact)
