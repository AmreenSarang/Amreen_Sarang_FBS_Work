#Take input
salary = int(input('Enter basic salary of Employee:'))

#calculate da
da = (10 / 100) * salary
print('da',da)

#calculate ta
ta = (12 / 100) * salary
print('ta',ta)

#calculate hra
hra = (15 / 100) * salary
print('hra',hra)

#Calculate total salary
total_sal = salary + ta + da + hra

#Display result
print('Total salary of Employee:',total_sal)