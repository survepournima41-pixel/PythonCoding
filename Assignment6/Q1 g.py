#        A
#      A B C  
#    A B C D E  
#  A B C D E F G  
#A B C D E F G H I  

n =5 
for i in range(1, n + 1):
    print(' '*(n - i), end = '')
    
    for j in range(2 * i - 1):
        print(chr(65 + j), end = ' ')
    print()