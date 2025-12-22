#Convert distant given in feet and inches into meter and centimeter.
# 1foot = 30.48
# 1inches = 2.54

# Take input
feet = int(input('Enter the feet:'))
inches = int(input('Enter the inches:'))

# calculate the centimeter
total_cm = feet * 30.48 + inches * 2.54


# convert the meter and centimeter

meter = (total_cm // 100)
centimeter = total_cm % 100

print(f'Distant is a {meter}, Meter is a {centimeter}')