#Take input
HH = int(input('Enter value hours :'))
MM = int(input('Enter value Minutes :'))
SS = int(input('Enter value SS :'))

#Calculate seconds

sec =(HH * 3600) + (MM * 60) + SS

# Display Result
print('Time into Seconds:',sec)