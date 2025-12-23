# Write a program to input any alphabet and check whether it is vowel or consonant.
alpha = input('Enter the alphabates:')

if(alpha in 'aeiouAEIOU'):
    print(f'{alpha} is a vowel')
else:
    print(f'{alpha} is a consonant')    