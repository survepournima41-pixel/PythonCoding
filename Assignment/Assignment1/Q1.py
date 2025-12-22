# Write a program to calculate the percentage of student based on marks of any 5 subjects
#****formula of calculate the percentage= total=s1+s2+s3+s4+s5
# percentage=(total/500)*100

# Take input
s1=int(input('Enter the first subject marks:'))
s2=int(input('Enter the second subject marks:'))
s3=int(input('Enter the third subject marks:'))
s4=int(input('Enter the fourth subject marks:'))
s5=int(input('Enter the fivfth subject marks:'))

#Calculate
total_no_of_subject = s1+s2+s3+s4+s5
per_of_subject = (total_no_of_subject / 500)*100

# Print 
print('Enter the five subject marks:', total_no_of_subject) 
print('Percentage of five suject=', per_of_subject)