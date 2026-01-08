#     1
#    1  2
#   1    3
#  1      4
# 1  2 3 4 5

n = 5

print(' '*(n - 1)+ '1')

for i in range(2, n):
    print(' '*(n - i) + '1' + ' '*(2*i-3) + str(i))
    
print(' '.join(str(i) for i in range(1, n + 1)))