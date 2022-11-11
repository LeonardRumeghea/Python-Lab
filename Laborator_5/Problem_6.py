def is_even(number):

    if type(number) == int:
        return number & 1 == 0
    
    elif type(number) == float:
        return int(str(number).split('.')[1]) & 1 == 0
    
    else:
        raise TypeError('Please enter only numbers!')


def my_function(list):
    
    try:
        even = []
        odd = [] 
        result = []

        for item in list:

            if is_even(item):
                result.append((item, odd.pop(0))) if len(odd) > 0 else even.append(item)
            else:
                result.append((even.pop(0), item)) if len(even) > 0 else odd.append(item)

        if len(odd) > 0:
            raise ValueError('There are more odd numbers than even numbers!')

        if len(even) > 0:
            raise ValueError('There are more even numbers than odd numbers!')

        return result

    except TypeError as e:
        return e

try:
    print(my_function([1, 3, 5, 2, 8, 7, 4, 10, 9, 2]))
except ValueError as e:
    print(e)