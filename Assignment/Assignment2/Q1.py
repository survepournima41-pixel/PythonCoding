#1. Convert the time entered in hh,min and sec into seconds.
# 1h = 3600hr
# 1min = 60sec
# 1sec = 45

h = int(input('Enter the hour:'))
m = int(input('Enter the minute:'))
s = int(input('Enter the sec:'))

total_seconds = h*3600 + m*60 + s

print('Total seconds =', total_seconds) 
