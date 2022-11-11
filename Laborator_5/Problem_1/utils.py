from math import sqrt


def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(sqrt(x) + 1)):
        if x % i == 0:
            return False
    return True


def process_item(x):
    x += 1
    while not is_prime(x):
        x += 1
    return x

# try:
#     x = input('Enter a number: ')
        
#     prime_number = process_item(int(x))
#     print( f'\tFirst prime number greater than {x} is {prime_number}\n')

# except ValueError:
#     print('\tPlease enter a valid number!\n')