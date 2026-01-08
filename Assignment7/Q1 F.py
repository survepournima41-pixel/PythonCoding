# 1 2 3 4 5
# 2     5
# 3   5
# 4 5
# 5

n = 5

for i in range(1, n + 1):
    print(i, end =' ')
print()

for i in range(2, n + 1):
    print(i, end =' ')
    if i < n:
        print(' ' *(n - i - 1) + str(n))
    else:
        print()