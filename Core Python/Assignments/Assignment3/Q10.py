gender = input('Enter gender(F/M):')
age = int(input('Enter age:'))

if(gender == 'M'):
    if(age >= 21):
        print('Boy is Eligible for Marrige.')
    else:
        print('Boy is not Eligible for Marrige.')
else:
    if(age >= 18):
        print('Girl is Eligible for Marrige.')
    else:
        print('Girl is not Eligible for Marrige.')