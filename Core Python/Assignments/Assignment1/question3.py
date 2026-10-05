#Take input
divident = int(input('Enter value for divident:'))
divisor = int(input('Enter value for divisor:'))

#Calculate Quotient
Q = divident // divisor
print('Quotient:',Q)

#Calculate Remainder
R = divident % divisor 
print('Remainder:',R)
#Display Result
print(f'Quotient and Remainder of {divident} and {divisor} is: {Q} and {R}')