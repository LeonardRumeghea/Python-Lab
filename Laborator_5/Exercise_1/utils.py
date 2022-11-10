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
#     x = int(input('Enter a number: '))
#     print(process_item(x))
# except ValueError:
#     print('Please enter a valid number!')