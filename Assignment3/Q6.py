# Write a program to calculate profit or loss.
# selling_price > cost_price = profit.
# cost_price > selling_price = loss.

selling_price = int(input('Enter the selling price:'))
cost_price = int(input('Enter the cost price:'))

if(selling_price > cost_price):
    profit = selling_price - cost_price
    print('Profit', profit)
elif(cost_price > selling_price):
    loss = cost_price - selling_price
    print('loss', loss)
else:
    print('No profit, no loss.')