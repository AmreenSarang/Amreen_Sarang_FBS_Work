num = int(input('Enter Number:'))
temp = num

sum = 0
while(num > 0):
    d = num % 10
    print(d)
    num = num // 10
    fact = 1
    for i in range(1 , d + 1):
        fact *= i
    print(fact)
    sum += fact
print('Sum:',sum)

if(sum == temp):
    print(f'Given number is strong number.')
else:
    print(f'Given number is not a strong number.')
        
    

    