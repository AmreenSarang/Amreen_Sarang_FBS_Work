a= int(input('Enter value of a: '))
sum = 0

for i in range(1, 11):
    term = (a ** i) / i
    sum += term
    print('Term:', term)
print('Sum:', sum)