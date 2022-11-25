def pair_calulator(list):
    operations = {
        'sum': lambda a, b: a + b,
        'prod': lambda a, b: a * b,
        'pow': lambda a, b: a ** b,
    }

    for a, b in list:
        if type(a) != int and type(a) != float:
            raise Exception(f'{type(a)} are not numbers! All elements from tuples must be numbers!' )
        
        if type(b) != int and type(b) != float:
            raise Exception(f'{type(b)} are not numbers! All elements from tuples must be numbers!' )

    return [{operation: function(a, b) for operation, function in operations.items()} for a, b in list]

try:
    for elem in pair_calulator([(5, 2), (19, 1), (30, 6), (2, 2)]):
        print(elem)
except Exception as e:
    print(e)
    