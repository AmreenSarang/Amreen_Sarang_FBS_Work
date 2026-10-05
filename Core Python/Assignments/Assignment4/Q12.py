num = int(input('Enter Number: '))

temp = num
count = 0

# Count number of digits
while temp > 0:
    count += 1
    temp //= 10

temp = num
sum = 0

# Calculate Armstrong sum
while temp > 0:
    digit = temp % 10
    sum += digit ** count
    temp //= 10

if sum == num:
    print(f'{num} is Armstrong Number.')
else:
    print(f'{num} is not Armstrong Number.')