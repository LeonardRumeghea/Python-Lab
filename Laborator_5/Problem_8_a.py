def multiply_by_two(x):
    return x * 2


def add_numbers(a, b, c=1):
    return a + b

def print_arguments(function):
    def wrapper(*args, **kwargs):
        print (f'Arguments are: {args}, {kwargs}')
        return function(*args, **kwargs)

    return wrapper

augmented_multiply_by_two = print_arguments(multiply_by_two)
print(augmented_multiply_by_two(10))

augmented_add_numbers = print_arguments(add_numbers)
print(augmented_add_numbers(3, 4, c=10))
