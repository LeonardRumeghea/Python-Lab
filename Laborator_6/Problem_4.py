# 4.Write a function that receives as a parameter the path to an xml document and an attrs dictionary and returns those 
# elements that have as attributes all the keys in the dictionary and values ​​the corresponding values. 
# For example, if attrs={"class": "url", "name": "url-form", "data-id": "item"} the items selected will be those tags 
# whose attributes are class="url" si name="url-form" si data-id="item".

import os
import re

def parse_xml(path, attrs):
    if not os.path.isfile(path):
        raise Exception('Path must be a file')

    if not isinstance(attrs, dict):
        raise Exception('Attrs must be a dictionary')

    with open(path, 'r') as file:
        data = file.read()

    reg_attrs = re.compile(r'(\S+)="(\w+?)"')
    result = []
    attrs = attrs.items()

    result = [tag for tag in re.compile(r'<\w+\s+[^>]*>').findall(data) 
        if all([attr in attrs for attr in reg_attrs.findall(tag)])]

    return result

try:
    print(*parse_xml('D:\\Documents\\GitHub\\Python-Lab\\Laborator_6\\file.xml',
          {"class": "url", "name": "url-form", "data-id": "item"}), sep='\n')
except Exception as e:
    print(e)