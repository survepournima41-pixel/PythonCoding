# 1^1 + 2^2 + 3^3 +..........+ n^n

def power_term(num):
    return num ** num
    
def sum_of_power_series(n):
    total = 0
    for i in range(1, n + 1):
        total += power_term(i)
    return total

n = int(input("Enter the value of n:"))
result = sum_of_power_series(n)

print("Sum of the series is :", result)