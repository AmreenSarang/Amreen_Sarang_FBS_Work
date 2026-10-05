a = int(input('Enter 1st angle of triangle:'))
b = int(input('Enter 2nd angle of triangle:'))
c = int(input('Enter 3rd angle of triangle:'))

sum_of_angles = a + b + c

if(sum_of_angles == 180):
    print('Triangle is valid')
else:
    print('Triangle is not valid')