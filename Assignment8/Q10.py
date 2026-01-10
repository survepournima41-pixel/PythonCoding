#10. Write a program to check if entered year is a leap year or not.

def is_divisible(year, divisor):
    return year % divisor == 0

def is_leap_year(year):
    if is_divisible(year, 400):
        return True
    if is_divisible(year, 100):
        return False
    if is_divisible(year, 4):
        return True
    else: 
        return False
    
def get_year():
    return int (input('Enter a year:'))

def display_result(year, leap):
    if leap:
        print(f'{year} is a leap year.')
    else:
        print(f'{year} is not a leap year.')
        
def main():
    year = get_year()
    leap = is_leap_year(year)
    display_result(year, leap) 
    
main()
    
