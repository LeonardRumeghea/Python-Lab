# 2.Write a function that receives as a parameter a regex string, a text string and a whole number x, and returns those 
# long-length x substrings that match the regular expression.

import re
def extract_words(regex, text, x):
    
        if not isinstance(regex, str):
            raise Exception('Regex must be a string')
        if not isinstance(text, str):
            raise Exception('Text must be a string')
        if not isinstance(x, int):
            raise Exception('x must be an integer')
    
        return [substring for substring in re.findall(regex, text) if len(substring) == x]

try:
    print(extract_words(r'\w+', "Hello, how are you?", 2))
    print(extract_words(r'\w+', "The weather is good.", 3))
    print(extract_words(r'\w+', [1, 2, 3], 3))
except Exception as e:
    print(e)