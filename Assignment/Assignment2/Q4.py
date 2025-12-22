#WAP to calculate area of triangle and rectangle
# formula area of rectangle = lenght * breadth
# formula area of triangle = base * height / 2

# Take input
lenght = int(input('Enter the lenght:'))
breadth = int(input('Enter the bradth:'))
base = int(input('Enter the base:'))
height = int(input('Enter the height:'))

# Calculate the area of rectangle

total_area_of_rec = lenght * breadth

# Calculate the area of triangle

total_area_of_triangle = (base * height) / 2

print('Total area of rectangle = ', total_area_of_rec)

print('Total area of triangle = ', total_area_of_triangle)

