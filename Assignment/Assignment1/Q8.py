#Write a program to convert days into years, weeks and days.
# 1year = 365
# 1 Week = 7
# days=1935

dividend = int(input('Enter the dividend:'))

# Calculate Year & days

year = dividend // 365
days = dividend % 365
print(f'Days convert into year is {year}, days is {days}')
print('Days is =', days)

# Weeks & Days

week = days // 7
days = days % 7
print(f'Days convert into week is {week}, days is {days}')


