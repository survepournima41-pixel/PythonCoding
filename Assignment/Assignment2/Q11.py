# Write a program to accept an integer amount from user and tell minimum
# number of notes needed for representing that amount.

amount = 2893

print('Minimum number of notes:')

notes = [2000, 500, 100, 50, 20, 10, 5, 2, 1]

for note in notes:
    if amount >= note:
        count = amount // note
        amount = amount % note
        
        print(f'amount in a {count}.')
    