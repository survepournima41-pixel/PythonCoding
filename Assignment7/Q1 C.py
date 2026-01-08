# 1
# 1  2
# 1    3
# 1      4
# 1 2  3 4 5

n = 5

print(1)

for i in range(2, n):
    print('1' + ' '*(2 * i -3)+ str(i))
    
for i in range(1, n + 1):
    print(i, end = ' ')