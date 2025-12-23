# Write a program to check if user has entered correct userid and password.

correct_username = "Pournima"
correct_password = "pournima@123"

username = input('Enter the user id:')
password = input('Enter the password:')

if username == correct_username and password == correct_password:
    print('Correct user name and password =', correct_username)
    print('Correct password =', correct_password)
else:
    print('Invalid username and password.')