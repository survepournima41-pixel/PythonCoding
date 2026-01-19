# Write a program to find maximum and minimum element in a list.

# Maximum Element
li = [40, 30, 60, 20, 80, 10, 70]

max = li[0]

for i in range(1, len(li)):
    if(li[i] > max):
        max = li[i]
print("Maximum Element is:", max)


# Minimum Element
li = [40, 30, 60, 20, 80, 10, 70]

min = li[0]

for i in range(1, len(li)):
    if(li[i] < min):
        min = li[i]
print("Minimum Element is:", min)
