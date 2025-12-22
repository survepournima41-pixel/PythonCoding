#Write a program to enter P, T, R and calculate Compound Interest.
#Formula = (p*(1+r/100)**t) its formula find out the amount =a
#compound intrest = c-p

# Take input
p =int(input('Enter the princple amount:'))
r =int(input('Enter the rate of interest:'))
t =int(input('Enter the no of yea:'))

# Calculate
amount = (p*(1+r/100)**t)

print('Display the amount =', amount)

comp = amount - p
print('Compound Intrest =', comp) 
