#Write a program to enter P, T, R and calculate simple Interest.
# Simple Intrest = P*R*T/100

# Take input
p=int(input('Enter the principle value:'))
r=int(input('Enter the rate of intrest:'))
t=int(input('Enter the no of year:'))

# Calculate
si = p*r*t / 100
 
# Print
print('Simple Intrest=', si)