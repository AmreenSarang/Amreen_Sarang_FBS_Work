#Take input

cost_price= int(input('Enter cost price of book :'))
discount = int(input('Enter discount on book :'))

#Calculate discount amount

Disc_amount = (cost_price * discount) / 100

#Calculate selling price

Selling_price = cost_price - Disc_amount

#Display Result
print('selling price of book is:',Selling_price)