# Take input

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

#Perform Swapping
a = a + b
b = a - b
a = a - b

#Display Result
print('After swapping First number =', a)
print('After swapping Second number =', b)