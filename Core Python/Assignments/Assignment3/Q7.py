correct_userid = 101
correct_password = 1771

user_id = int(input('Enter UserID:'))
password = int(input('Enter Password:'))

if(user_id == correct_password and correct_password == password):
    print('Login Successful!')

else:
    print('Invalid UserID or Password.')