# 1.Write a function that extracts the words from a given text as a parameter. 
# A word is defined as a sequence of alpha-numeric characters.

import re
def extract_words(text):

    if not isinstance(text, str):
        raise Exception('Input must be a string')

    return re.findall(r'\w+', text)


try:
    print(extract_words("Hello, how are you?"))
    print(extract_words("The weather is good."))
    print(extract_words([1, 2, 3]))
except Exception as e:
    print(e)