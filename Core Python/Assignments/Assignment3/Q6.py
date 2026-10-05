cost_price = int(input('Enter Cost Price:'))
selling_price = int(input('Enter Selling Price:'))

if(cost_price < selling_price):
    Profit = selling_price - cost_price
    print('Profit:',Profit)

else:
    loss = cost_price - selling_price
    print('Loss:',loss)