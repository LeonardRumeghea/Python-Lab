# 5.Write another variant of the function from the previous exercise that returns those elements that have at least one 
# attribute that corresponds to a key-value pair in the dictionary.

import os
import re

def parse_xml(path, attrs):
    if not os.path.isfile(path):
        raise Exception('Path must be a file')

    if not isinstance(attrs, dict):
        raise Exception('Attrs must be a dictionary')

    with open(path, 'r') as file:
        data = file.read()

    reg_attrs = re.compile(r'(\S+)="(.+?)"')
    result = []

    result = [tag for tag in re.compile(r'<\w+\s+[^>]*>').findall(data) 
        if any([attr in attrs.items() for attr in reg_attrs.findall(tag)])]

    return result

try:
    print(*parse_xml('D:\\Documents\\GitHub\\Python-Lab\\Laborator_6\\file.xml',
          {"class": "url", "name": "url-form", "data-id": "item"}), sep='\n')
except Exception as e:
    print(e)