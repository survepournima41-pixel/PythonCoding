#Write a program to find print the following Fibonacci series using
#functions:
#1 1 2 3 5 8 n terms

def fibonacci(n):
    a,b = 1,1
    for i in range(n):
        print(a, end = ' ')
        a,b = b, a + b
        
n = int(input('Enter number of terms:'))
fibonacci(n)