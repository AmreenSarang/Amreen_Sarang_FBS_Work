n = int(input('Enter number of employees: '))
total_salary = 0

for i in range(1, n + 1):
    basic = int(input(f'Enter basic salary of employee {i}: '))
    if basic < 20000:
        da = basic * 10 / 100
        ta = basic * 12 / 100
        hra = basic * 15 / 100
    else:
        da = basic * 15 / 100
        ta = basic * 18 / 100
        hra = basic * 20 / 100

    salary = basic + da + ta + hra
    total_salary += salary
    print(f"Total salary of employee {i}: {salary}")

print(f"Total salary of all employees: {total_salary}")