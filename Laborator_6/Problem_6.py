# 6.Write a function that, for a text given as a parameter, censures words that begin and end with vowels. 
# Censorship means replacing characters from odd positions with *.

import re

def censor_words(text):
    if not isinstance(text, str):
        raise Exception('Input must be a string')

    # return re.sub(r'\b[aeiouAEIOU]\w*[aeiouAEIOU]\b', lambda m: re.sub(r'\w', '*', m.group(0)), text)

    reg = r'\b[aeiouAEIOU]\w*[aeiouAEIOU]\b'
    for word in re.findall(reg, text):
        text = text.replace(word, ''.join(['*' if i % 2 == 1 else word[i] for i in range(len(word))]))

    return text

try:
    print(censor_words("Hello, how are you?"))
    print(censor_words("The weather is good."))
    print(censor_words([1, 2, 3]))
except Exception as e:
    print(e)