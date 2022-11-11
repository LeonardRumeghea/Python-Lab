def multiply_by_three(x):
    return x * 3


def multiply_output(function):
    def wrapper(*args, **kwargs):
        return 2 * function(*args, **kwargs)
    return wrapper


augmented_multiply_by_three = multiply_output(multiply_by_three)
print(f'Result: {augmented_multiply_by_three(10)}')