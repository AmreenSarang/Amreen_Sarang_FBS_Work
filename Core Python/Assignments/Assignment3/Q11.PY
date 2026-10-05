age = (
    int(input('Enter age of Member 1: ')),
    int(input('Enter age of Member 2: ')),
    int(input('Enter age of Member 3: ')),
    int(input('Enter age of Member 4: ')),
    int(input('Enter age of Member 5: '))
)

ticket_amount = int(input('Enter Ticket Amount per Person: '))

# Member 1
if age[0] < 12:
    amount1 = ticket_amount * 70 / 100
elif age[0] > 59:
    amount1 = ticket_amount * 50 / 100
else:
    amount1 = ticket_amount

# Member 2
if age[1] < 12:
    amount2 = ticket_amount * 70 / 100
elif age[1] > 59:
    amount2 = ticket_amount * 50 / 100
else:
    amount2 = ticket_amount

# Member 3
if age[2] < 12:
    amount3 = ticket_amount * 70 / 100
elif age[2] > 59:
    amount3 = ticket_amount * 50 / 100
else:
    amount3 = ticket_amount

# Member 4
if age[3] < 12:
    amount4 = ticket_amount * 70 / 100
elif age[3] > 59:
    amount4 = ticket_amount * 50 / 100
else:
    amount4 = ticket_amount

# Member 5
if age[4] < 12:
    amount5 = ticket_amount * 70 / 100
elif age[4] > 59:
    amount5 = ticket_amount * 50 / 100
else:
    amount5 = ticket_amount

total_amount = amount1 + amount2 + amount3 + amount4 + amount5

print('Total Ticket Amount:', total_amount)