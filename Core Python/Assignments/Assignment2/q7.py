num = int(input('Enter 3 digit number:'))

#Separate last didit
d1 = num % 10
print('d1:',d1)
num = num // 10
print('num:',num)

#Separate Middle didit
d2 = num % 10
print('d2:',d2)
num = num // 10
print('num:',num)

#Separate first didit
d3 = num % 10
print('d3:',d3)
num = num // 10
print('num:',num)

#Perform Addition of three digit
sum = d1 + d2 + d3

#Display Result
print('Addition of three digit number:',sum)