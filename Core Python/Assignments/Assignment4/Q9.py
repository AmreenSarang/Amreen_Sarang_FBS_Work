Range = int(input('Enter Range:'))
n = int(input('Enter Number:'))

for i in range(1 , Range):
    if(i % n == 0):
        print(i)