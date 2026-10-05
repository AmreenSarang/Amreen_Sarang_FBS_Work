#Take input for days

days = int(input("Enter number of days: "))

# Calculate years

years = days // 365

# Remaining days after years

remaining_days = days % 365

# Calculate weeks

weeks = remaining_days // 7

# Remaining days

remaining_days = remaining_days % 7

# Display result

print("Years:", years)
print("Weeks:", weeks)
print("Days:", remaining_days)