#12. Write a program to check if given number is Armstrong number or not.
#(Hint : 153 = 1*1*1 + 5*5*5 + 3*3*3 , 1634 = 1*1*1*1 + 6*6*6*6 + 3*3*3*3 +
#4*4*4*4)

num = int(input('Enter a number:'))
n = num
digits = len(str(num))
sum_pow = 0

while n > 0:
    digit = n % 10
    sum_pow = sum_pow + digit ** digits
    n //= 10
    
if sum_pow == num:
    print("Armstrong number is an:", num)
else:
    print("Is not an Armstrong number:", num)