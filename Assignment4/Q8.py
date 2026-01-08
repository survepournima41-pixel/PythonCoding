# WAP to find which numbers are divisible by 7 and multiple of 5 in a given range.
lower = int(input('Enter the lower number:'))
upper = int(input('Enter the upper number:'))

for i in range(lower,upper + 1):
    if(i%7==0 and i%5==0):
        print(i)