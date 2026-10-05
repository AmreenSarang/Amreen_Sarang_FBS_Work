correct_userid = 101
correct_password = 1771

user_id = int(input('Enter UserID:'))
password = int(input('Enter Password:'))

if(user_id == correct_userid and password == correct_password):
    print('Login Successful!')
    
    Captcha = 1234
    print('Captcha = 1234')
    captcha = int(input('Enter the captcha:'))
    
    if(Captcha == captcha):
        print('Success!')
    else:
        print('Failed!')
    
else:
    print('Invalid UserID or Password.')

