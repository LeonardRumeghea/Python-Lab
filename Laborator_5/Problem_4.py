def is_valid(object):

    return  type(object) == dict \
                and len(object) >= 2 \
                and any([type(key) == str and len(key) >= 3 for key in object.keys()])


def my_function(*args, **kwargs):
    return [object for object in args if is_valid(object)] + [object for object in kwargs.values() if is_valid(object)]

print(my_function(
    {1: 2, 3: 4, 5: 6},
    {'a': 5, 'b': 7, 'c': 'e'},
    {2: 3},
    [1, 2, 3],
    {'abc': 4, 'def': 5},
    3764,
    dictionar={'ab': 4, 'ac': 'abcde', 'fg': 'abc'},
    test={1: 1, 'test': True}
))