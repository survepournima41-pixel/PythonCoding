#Program to find quotient and remainder of two numbers.
#** Quotient=dividend // divisor
#** Remainder=dividend % divisor

#Take input
dividend=int(input('Enter the dividend:'))
divisor=int(input('Enter the divisor:'))

# calculate the Quotient
quotient = dividend // divisor
print('Quotient=', quotient)

# Calculate the Remainder
remainder = dividend % divisor
print('Remainder=', remainder)