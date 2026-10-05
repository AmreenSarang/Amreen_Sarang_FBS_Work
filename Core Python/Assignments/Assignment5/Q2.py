n = int(input('Enter number of students: '))
total_percentage = 0

for i in range(1, n + 1):
    print('Student:',i)

    total = 0
    for j in range(1, 6):
        marks = int(input(f'Enter marks of subject {j}: '))
        total += marks

        percentage = (total / 500) * 100
        print('Percentage:',percentage)

        total_percentage += percentage
print('Total Percentage:',total_percentage)

avg = total_percentage / n
print('Average percentage of students:',avg)


