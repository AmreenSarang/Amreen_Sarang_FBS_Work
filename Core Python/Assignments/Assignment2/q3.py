#Take input

F = float(input("Enter Distance in Feet: "))
I = float(input("Enter Distance in Inches: "))

# Convert feet into inches

Total_inches = (F * 12) + I

#Convert inches into centimeters
C = Total_inches * 2.54

#Calculate Meters
M = C // 100

# Display Result

print('Distance in Meter:',M)
print('Distance in Centimeter:',C)