n = int(input('Enter no. of fibonacci number:'))
a = -1
b = 1

for i in range(n):
    c = a + b
    print(c, end = ' ')
    a = b
    b = c
