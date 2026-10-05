num = int(input('Enter number:'))
a = num 
sum = 0
while(num > 0):
    d = num % 10
    print('d:',d)
    num = num // 10
    fact = 1
    for i in range(1 , d + 1):
        fact *= i
    print('fact:',fact)
    sum += fact
    print('sum:',sum)
if(sum == a):
    print('Number is strong number.') 
else:
    print('Given number is not a strong number.') 