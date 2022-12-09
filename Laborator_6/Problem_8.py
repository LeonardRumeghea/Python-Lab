# 8.Write a function that recursively scrolls a directory and displays those files whose name matches a regular 
# expression given as a parameter or contains a string that matches the same expression. Files that satisfy both 
# conditions will be prefixed with ">>"

import os
import re

def find_files(path, regex):



    if not os.path.isdir(path):
        raise Exception('Path must be a directory')

    if not isinstance(regex, str):
        raise Exception('Regex must be a string')

    reg = re.compile(regex)
    result = []

    for file in os.listdir(path):
        file_name = os.path.splitext(file)[0]

        if os.path.isdir(os.path.join(path, file)):
            result += find_files(os.path.join(path, file), regex)
        else:
            first_condition = reg.fullmatch(file_name)
            second_condition = len(reg.findall(file_name[1:])) + len(reg.findall(file_name[:-1]))
            
            if first_condition and second_condition > 1:
                result += ['>>' + os.path.join(path, file)]
            elif first_condition or second_condition > 0:
                result += [os.path.join(path, file)]

    return result
try:
    print(*find_files(
                'D:\\Documents\\GitHub\\Python-Lab\\Laborator_6\\Folder', 
                r'[aeiouAEIOU](\.+?)[aeiouAEIOU]'
            ), 
            sep='\n'
        )
except Exception as e:
    print(e)
