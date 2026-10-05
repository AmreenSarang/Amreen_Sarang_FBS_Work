num = int(input('Enter Number:'))
sum = 0

for i in range(1 , num):
    if(num % i == 0):
        print(i)
        sum += i

if(sum == num):
    print(f'{num} is Perfect Number.')
else:
    print(f'{num} is not a Perfect Number.')
        
    