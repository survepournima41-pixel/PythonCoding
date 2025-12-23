#Accept age of five people and also per person ticket amount and then calculate total
#amount to ticket to travel for all of them based on following condition :
#a. Children below 12 = 30% discount
#b. Senior citizen (above 59) = 50% discount
#c. Others need to pay full.

total_amount = 0

ticket_price = float(input('Enter the ticket price as per person:'))

for i in range(1 , 6):
    
    age = int(input(f'enter age in {i}:'))
    
    if age < 12:
        # 30% discount
        amount = ticket_price * 0.70
    
    elif age > 59:
        # 50% discount
        amount = ticket_price * 0.50
    else:
         amount = ticket_price
         
    total_amount += amount

print('Total ticket amount of all pepole:', total_amount)