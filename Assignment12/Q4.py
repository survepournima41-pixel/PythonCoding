# Python Program to Form a New String where the First Character and
# the Last Character have been Exchanged

text = 'python'
if len(text) > 1:
    new_string = text[-1] + text[1: -1] + text[0]
else:
    new_string = text
    
print('ORiginal Strings', text)
print('New String:', new_string)
