# 2.
# def my_function(*args, **kwargs):
#     try:
#         return sum(kwargs.values())
#     except Exception:
#         print('Please enter only numbers!')
#         return None


# my_anonymous_funtions = lambda *args, **kwargs: sum(kwargs.values())


# print(my_function(1, 2, c=3, d='a'))
# print(my_anonymous_funtions(1, 2, c=3, d=4))

# 3.
# def vowels(string):
#     if type(string) != str:
#         raise TypeError('Please enter a string!')

#     vw = ['a', 'e', 'i', 'o', 'u']
#     return [letter for letter in string if letter in vw]


# def vowels(string):
#     if type(string) != str:
#         raise TypeError('Please enter a string!')
    
#     return list(filter(lambda x: x in 'aeiou', string))


# vowels = lambda string: [letter for letter in string if letter in ['a', 'e', 'i', 'o', 'u']] if type(string) == str \
#     else TypeError('Please enter a string!')

# vowels = lambda string: list(filter(lambda x: x in 'aeiou', string)) if type(string) == str \
#     else TypeError('Please enter a string!')


# try:
#     print(vowels('Programming in Python is fun'))
#     print(vowels(2))
# except TypeError as e:
#     print(e)

# 4.
# def is_valid(object):

#     return  type(object) == dict \
#                 and len(object) >= 2 \
#                 and any([type(key) == str and len(key) >= 3 for key in object.keys()])


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
# def my_function(lst):
    
#     if type(lst) != list:
#         raise TypeError('Please enter a list!')
    
#     return [item for item in lst if type(item) == int or type(item) == float]

# try:
#     print(my_function([1, "2", {"3": "a"}, {4, 5}, 5, 6, 3.0]))
# except TypeError as e:
#     print(e)

# 6.
# def my_function(list):
    
#     try:
#         even = []
#         odd = [] 
#         result = []

#         for item in list:
#             if type(item) == int:
#                 if item & 1:
#                     result.append((item, odd.pop(0))) if len(odd) > 0 else even.append(item)
#                 else:
#                     result.append((even.pop(0), item)) if len(even) > 0 else odd.append(item)
            
#             elif type(item) == float:
#                 if int(str(item).split('.')[1]) & 1:
#                     result.append((item, odd.pop(0))) if len(odd) > 0 else even.append(item)
#                 else:
#                     result.append((even.pop(0), item)) if len(even) > 0 else odd.append(item)

#             else:
#                 raise TypeError('Please enter only numbers!')

#         if len(odd) > 0:
#             raise ValueError('There are more odd numbers than even numbers!')

#         if len(even) > 0:
#             raise ValueError('There are more even numbers than odd numbers!')

#         return result

#     except TypeError as e:
#         return e

# try:
#     print(my_function([1, 3, 5, 2, 8, 7, 4, 10, 9, 2]))
# except ValueError as e:
#     print(e)

# 7.
# def process(filters=None, limit=1000, offset=0):
    
#     def fibbonaci(filters, max_count):
#         result = []

#         """
#             •[filter(number) for filter in filters] -> [b_1, b_2, b_3, ...] -> [True/False, True/False, True/False, ...]
#                 Where b_i is the result of i-th filter function applied to the number
#                 If all b_i is True, then the number is considered valid and will be added to the result list
#             •If we have no filters, then all numbers will be considered as valid
#         """

#         if (False in [filter(0) for filter in filters] if filters else True):
#             result.append(0)
#             max_count -= 1

#         if max_count > 0 and (False not in [filter(1) for filter in filters] if filters else True):
#             result.append(1)
#             max_count -= 1

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

#     if limit == 0:
#         return []
    
#     if offset < 0:
#         assert offset >= 0, 'Offset must be greater or equal to 0!'

#     return fibbonaci(filters=filters, max_count=(limit + offset))[offset:]

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


# def add_numbers(a, b, c=1):
#     return a + b

# def print_arguments(function):
#     def wrapper(*args, **kwargs):
#         print (f'Arguments are: {args}, {kwargs}')
#         return function(*args, **kwargs)

#     return wrapper

# augmented_multiply_by_two = print_arguments(multiply_by_two)
# print(augmented_multiply_by_two(10))

# augmented_add_numbers = print_arguments(add_numbers)
# print(augmented_add_numbers(3, 4, c=10))

# b)

# def multiply_by_three(x):
#     return x * 3


# def multiply_output(function):
#     def wrapper(*args, **kwargs):
#         return 2 * function(*args, **kwargs)
#     return wrapper


# augmented_multiply_by_three = multiply_output(multiply_by_three)
# print(f'Result: {augmented_multiply_by_three(10)}')

# c)
# def add_numbers(a, b):
#     return a + b


# def multiply_output(function):
#     def wrapper(*args, **kwargs):
#         return function(*args, **kwargs) * 2

#     return wrapper


# def print_arguments(function):
#     def wrapper(*args, **kwargs):
#         print (f'Arguments are: {args}, {kwargs}')
#         return function(*args, **kwargs)

#     return wrapper


# def augment_function(function, decorators):
#     for decorator in decorators:	
#         function = decorator(function)
#     return function


# decorated_function = augment_function(add_numbers, [print_arguments, multiply_output]) 
# print(decorated_function(3, 4))  # this will print: Arguments are: (3, 4), {} and will return (2 * (3 + 4))


# 9.
def pair_calulator(list):
    operations = {
        'sum': lambda a, b: a + b,
        'prod': lambda a, b: a * b,
        'pow': lambda a, b: a ** b,
    }

    try:
        for a, b in list:
            if type(a) != int or type(a) != float or type(b) != int or type(b) != float:
                raise Exception('All elements from tuples must be numbers!')

        return [{operation: function(a, b) for operation, function in operations.items()} for a, b in list]

    except Exception as e:
        print(e)
        return []

for elem in pair_calulator([(5, 2), (19, 1), (30, 6), (2, 2)] ):
    print(elem)