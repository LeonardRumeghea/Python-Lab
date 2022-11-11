def my_function(lst):
    
    if type(lst) != list:
        raise TypeError('Please enter a list!')
    
    return [item for item in lst if type(item) == int or type(item) == float]

try:
    print(my_function([1, "2", {"3": "a"}, {4, 5}, 5, 6, 3.0]))
except TypeError as e:
    print(e)