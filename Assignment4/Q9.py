#9. WAP to print all numbers in a range divisible by a given number.
lower = int(input('Enter the lower limit:'))
upper = int(input('Enter the upper limit:'))
n = int(input('Enter the number to be divided by:'))

for i in range(lower,upper + 1):
    if(i % n == 0):
        print(i)
