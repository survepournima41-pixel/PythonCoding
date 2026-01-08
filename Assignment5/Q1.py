#1. Write a program to prompt user to enter userid and password. If Id and
#password is incorrect give him chance to re-enter the credentials. Let him try 3
#times. After that program to terminate.

correct_userid = 'admin'
correct_password = '1234'

max_attempts = 3

for attempt in range(1, max_attempts + 1):
    userid = input('Enter user ID:')
    password = input('Enter password:')
    
    if userid == correct_userid and password == correct_password:
        print("Login Successful!")
        break
    else:
        print(f'Incorrect credentials, attempt {attempt} of {max_attempts}')
        
        if attempt == max_attempts:
            print('Maximum attempts reached program terminated.')