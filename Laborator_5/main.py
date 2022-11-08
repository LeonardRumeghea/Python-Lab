# 2.
# def my_function(*args, **kwargs):
#     try:
#         return sum(kwargs.values())
#     except Exception as e:
#         print('Please enter only numbers!')


# my_anonymous_funtions = lambda *args, **kwargs: sum(kwargs.values())


# print(my_function(1, 2, c=3, d='a'))
# print(my_anonymous_funtions(1, 2, c=3, d=4))

# 3.
# def vowels(string):
#     vowels = ['a', 'e', 'i', 'o', 'u']
#     return [letter for letter in string if letter in vowels]


# def vowels(string):
    # return list(filter(lambda x: x in 'aeiou', string))


# vowels = lambda string: [letter for letter in string if letter in ['a', 'e', 'i', 'o', 'u']]
# vowels = lambda string: list(filter(lambda x: x in 'aeiou', string))


# print(vowels('Programming in Python is fun'))

# 4.
# def is_valid(object):
#     answer = True
#     answer = answer and type(object) == dict
#     answer = answer and len(object) >= 2
#     answer = answer and any([type(key) == str and len(key) >= 3 for key in object.keys()])
    
#     return answer


# def my_function(*args, **kwargs):
#     return [object for object in args if is_valid(object)] + [object for object in kwargs.values() if is_valid(object)]

# print(my_function(
#     {1: 2, 3: 4, 5: 6},
#     {'a': 5, 'b': 7, 'c': 'e'},
#     {2: 3},
#     [1, 2, 3],
#     {'abc': 4, 'def': 5},
#     3764,
#     dictionar={'ab': 4, 'ac': 'abcde', 'fg': 'abc'},
#     test={1: 1, 'test': True}
# ))

# 5.
# def my_function(list):
#     return [item for item in list if type(item) == int or type(item) == float]


# print(my_function([1, "2", {"3": "a"}, {4, 5}, 5, 6, 3.0]))


# 6.
# def my_function(list):

#     even = [number for number in list if number % 2 == 0]
#     odd = [number for number in list if number % 2 != 0]
    
#     return [item for item in zip(even, odd)]


# print(my_function([1, 3, 5, 2, 8, 7, 4, 10, 9, 2, 2]))

# 7.
# def process(filters=None, limit=1000, offset=0):
    
#     def fibbonaci(filters, max_count):
#         result = []

#         for i in [0, 1]:
#             is_valid = False not in [filter(i) for filter in filters] if filters else True
#             if is_valid:
#                 result.append(i)
#                 max_count -= 1

#         a, b = 0, 1
#         while max_count > 0:
#             number = a + b
#             is_valid = False not in [filter(number) for filter in filters] if filters else True

#             if is_valid:
#                 result.append(number)
#                 max_count -= 1
                
#             a, b = b, a + b

#         return result

#     if limit < 0:
#         assert limit > 0, 'Limit must be greater or equal than 0!'
    
#     if offset < 0:
#         assert offset >= 0, 'Offset must be greater or equal to 0!'

#     return fibbonaci(filters=filters, max_count=(limit + offset))[offset:] if limit > 0 else []

# def sum_digits(x):
#     return sum(map(int, str(x)))

# try:
#     print(process(
#         filters=[lambda item: item % 2 == 0, lambda item: item == 2 or 4 <= sum_digits(item) <= 20],
#         limit=2,
#         offset=2
#     ))
# except Exception as e:
#     print(e)

# 8. 
# a)
# def multiply_by_two(x):
#     return x * 2


# def add_numbers(a, b):
#     return a + b

# def print_arguments(function):
#     def wrapper(*args, **kwargs):
#         return f'Arguments are: {args}, {kwargs} and will return {function(*args, **kwargs)}'

#     return wrapper

# augmented_multiply_by_two = print_arguments(multiply_by_two)
# x = augmented_multiply_by_two(10)
# print(x)

# augmented_add_numbers = print_arguments(add_numbers)
# x = augmented_add_numbers(3, 4)
# print(x)

# b)

# def multiply_by_three(x):
#     return x * 3


# def multiply_output(function):
#     def wrapper(*args, **kwargs):
#         return function(*args, **kwargs) * 2

#     return wrapper


# augmented_multiply_by_three = multiply_output(multiply_by_three)
# x = augmented_multiply_by_three(10) 
# print(x)

# c)

# Write a function called augment_function with two parameters named function and decorators. decorators will be a list of 
# functions which will have the same signature as the previous functions (print_arguments, multiply_output). augment_function 
# will create a new function which is augmented using all the functions in the decorators list.

# Example:
# def add_numbers(a, b):
    # return a + b

# decorated_function = augment_function(add_numbers, [print_arguments, multiply_output]) 
# x = decorated_function(3, 4)  # this will print: Arguments are: (3, 4), {} and will return (2 * (3 + 4))


# def add_numbers(a, b):
#     return a + b


# def multiply_output(function):
#     def wrapper(*args, **kwargs):
#         return function(*args, **kwargs) * 2

#     return wrapper


# def print_arguments(function):
#     def wrapper(*args, **kwargs):
#         print (f'Arguments are: {args}, {kwargs} and will return {function(*args, **kwargs)}')

#     return wrapper


# def augment_function(function, decorators):
#     def wrapper(*args, **kwargs):
#         for decorator in decorators:
#             fct = decorator(function)
#             print(fct(*args, **kwargs))

#         return fct(*args, **kwargs)

#     return wrapper


# decorated_function = augment_function(add_numbers, [print_arguments, multiply_output]) 
# x = decorated_function(3, 4)  # this will print: Arguments are: (3, 4), {} and will return (2 * (3 + 4))
# print(x)


# 9.
# def pair_calulator(list):
#     operations = {
#         'sum': lambda a, b: a + b,
#         'prod': lambda a, b: a * b,
#         'pow': lambda a, b: a ** b,
#     }

#     return [{operation: function(a, b) for operation, function in operations.items()} for a, b in list]


# for elem in pair_calulator([(5, 2), (19, 1), (30, 6), (2, 2)] ):
#     print(elem)