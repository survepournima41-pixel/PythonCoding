#WAP to calculate total salary of employee based on basic, da=10% of basic,
#ta=12% of basic, hra=15% of basic.

b = int(input('Enter the basic salary:'))

# Calculate the basic salary of 20000

da = 0.10 * b
ta = 0.12 * b
hra = 0.15 * b

# Calculate the total salary
 
total_salary = b + da + ta + hra

print('DA =', da)
print('TA =', ta)
print('HRA =', hra)
print('Total salary =', total_salary)