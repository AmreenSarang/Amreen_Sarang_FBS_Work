#Take input
num = int(input('Enter 3 digit number:'))
temp = num

#Separate First didit
d1 = num % 10
num = num // 10

#Separate Middle didit
d2 = num % 10
num = num // 10

#Separate first didit
d3 = num % 10
num = num // 10

#merging three digits
reverse = d1 * 100 + d2 * 10 + d3

if(temp == reverse):
    print('Given number is Pallindrome')
else:
    print('Given number is not Pallindrome')
