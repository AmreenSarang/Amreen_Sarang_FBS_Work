correct_userid = 101
correct_password = 1771

for i in range(1, 4):
    user_id = int(input('Enter UserID: '))
    password = int(input('Enter Password: '))

    if(user_id == correct_userid and password == correct_password):
        print('Login Successful!')
        break
    else:
        print('Incorrect UserID or Password.')

else:
    print('You lost 3 chances.')