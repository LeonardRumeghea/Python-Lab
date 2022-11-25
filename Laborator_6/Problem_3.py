# Write a function that receives two parameters: a list of strings and a list of regular expressions. 
# The function will return a list of the strings that match on at least one regular expression from the list 
# given as parameter.

import re

def extract_words(strings, regex_list):
    
    if not isinstance(strings, list):
        raise Exception('First parameter must be a list')
    if not any(isinstance(item, str) for item in strings):
        raise Exception('First parameter must be a list of strings')
    if not isinstance(regex_list, list):
        raise Exception('Regex list must be a list')

    return [re.findall('|'.join(regex_list), string) for string in strings]

try:
    print(extract_words(["A stirng and 2 numbers: hello, 12 and 13", "A stirng and 2 numbers: hello, 12 and 13"], 
        [r'\w+', r'\d+']))

except Exception as e:
    print(e)