num = int(input('Enter number:'))

if(num > 1):
    for i in range(1 , num + 1):
        if(i % 7 == 0 and  i % 5 == 0):
            print(i)
    