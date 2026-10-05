#Take input Marks
sub1 = int(input('Enter Marks for subject 1:'))
sub2 = int(input('Enter Marks for subject 2:'))
sub3 = int(input('Enter Marks for subject 3:'))
sub4 = int(input('Enter Marks for subject 4:'))
sub5 = int(input('Enter Marks for subject 5:'))

#Calculate Obtained Marks
Obt_Marks = sub1 + sub2 + sub3 + sub4 + sub5

#Calculate Percentage
Percentage = (Obt_Marks / 500) * 100

#Display Result
print('Total Percentage:',Percentage)