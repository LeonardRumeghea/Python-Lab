def my_function(*args, **kwargs):
    try:
        return sum(kwargs.values())
    except Exception:
        print('Please enter only numbers!')
        return None


my_anonymous_funtions = lambda *args, **kwargs: sum(kwargs.values())


print(my_function(1, 2, c=3, d='a'))
print(my_anonymous_funtions(1, 2, c=3, d=4))