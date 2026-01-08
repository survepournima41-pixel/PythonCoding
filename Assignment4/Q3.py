# WAP to print sum of series upto n.

n = int(input("Enter n: "))
sum = 0
i = 1

while i <= n:
    sum += i
    i += 1

print('Sum of series:', sum)
