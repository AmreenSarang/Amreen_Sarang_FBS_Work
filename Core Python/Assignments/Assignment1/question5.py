#Take input
P = int(input('Enter Value for Principle Amount:'))
T = float(input('Enter Value for Time:'))
R = float(input('Enter Value for Rate:'))

#Calculate Amount
A = P * (1 + R / 100) ** T
print('Amount is:',A)

#Calculate Compound Interest
CI = A - P

#Display Result
print('Compound Interest is:',CI)