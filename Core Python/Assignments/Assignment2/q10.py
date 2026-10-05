#Take input
num = int(input('Enter 3 digit number:'))

#Separate First didit
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

#merging three digits
reverse = d1 * 100 + d2 * 10 + d3

#Display result

print("Reverse number =", reverse)