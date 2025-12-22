#WAP to calculate selling price of book based on cost price and discount.
# formula:-
# discount = (discount / 100)* cost price
# Selling price = cost price - discount

cp = int(input('Enter the celling price:'))
discount = int(input('Enter the discount:'))

# Calculate the discount

discount_amount = (discount / 100)* cp

# Calculate the selling price

sp = cp - discount_amount

print('Discount =', discount_amount)

print('Selling price =', sp)