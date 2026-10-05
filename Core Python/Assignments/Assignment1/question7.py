# Take input

a = float(input("Enter value of a: "))
b = float(input("Enter value of b: "))
c = float(input("Enter value of c: "))

# Calculate roots

x1 = -b + (b ** 2 - 4 * a * c)/ (2 * a)
x2 = -b - (b ** 2 - 4 * a * c)/ (2 * a)

#Display Result
print('Roots of Quadratic equation are:',x1 , x2)