def add_numbers(a, b):
    return a + b


def multiply_output(function):
    def wrapper(*args, **kwargs):
        return 2 * function(*args, **kwargs)

    return wrapper


def print_arguments(function):
    def wrapper(*args, **kwargs):
        print (f'Arguments are: {args}, {kwargs}')
        return function(*args, **kwargs)

    return wrapper


def augment_function(function, decorators):
    for decorator in decorators:	
        function = decorator(function)
    return function


decorated_function = augment_function(add_numbers, [print_arguments, multiply_output]) 
print(decorated_function(3, 4))  # this will print: Arguments are: (3, 4), {} and will return (2 * (3 + 4))