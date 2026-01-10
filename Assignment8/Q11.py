# WAP to check if a given number is Armstrong number or not. For
# each task create separate functions.

def count_digit(num):
    return len(str(num))

def sum_of_powers(num, power):
    total = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        total = total + digit ** power
        temp = temp // 10
    return total

def is_armstrong(num):
    digits = count_digit(num)
    return num == sum_of_powers(num, digits)

def get_number():
    return int(input('Enter a number:'))

def display_result(num, result):
    if result:
        print(f'{num} is an Armstrong number.')
    else:
        print(f'{num} is not an Armstrong number.')

def main():
    num = get_number()
    result = is_armstrong(num)
    display_result(num, result)

main()
    