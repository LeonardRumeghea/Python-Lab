def vowels(string):
    if type(string) != str:
        raise TypeError('Please enter a string!')

    vw = ['a', 'e', 'i', 'o', 'u']
    return [letter for letter in string if letter in vw]


def vowels(string):
    if type(string) != str:
        raise TypeError('Please enter a string!')
    
    return list(filter(lambda x: x in 'aeiou', string))


vowels = lambda string: [letter for letter in string if letter in ['a', 'e', 'i', 'o', 'u']] if type(string) == str \
    else TypeError('Please enter a string!')

vowels = lambda string: list(filter(lambda x: x in 'aeiou', string)) if type(string) == str \
    else TypeError('Please enter a string!')


try:
    print(vowels('Programming in Python is fun'))
    print(vowels(2))
except TypeError as e:
    print(e)