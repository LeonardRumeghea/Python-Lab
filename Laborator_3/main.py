# 1.Write a function that receives as parameters two lists a and b and returns a list of sets containing:
# (an intersected with b, a reunited with b, a - b, b - a)

# def intersect(a, b):
#     return {value for value in a if value in b}
#
#
# def union(a, b):
#     return set(a).union({value for value in b if value not in a})
#
#
# def difference(a, b):
#     return {value for value in a if value not in b}
#
#
# def sets(a, b):
#     return [intersect(a, b), union(a, b), difference(a, b), difference(b, a)]
#
#
# print(sets([1, 2, 3, 4, 5], [3, 4, 5, 6, 7]))

# 2. Write a function that receives a string as a parameter and returns a dictionary in which the keys are the
# characters in the character string and the values are the number of occurrences of that character in the given text.
# Example: For string "Ana has apples." given as a parameter the function will return the dictionary:
# {'a': 3, 's': 2, '.': 1, 'e': 1, 'h': 1, 'l': 1, 'p': 2, ' ': 2, 'A': 1, 'n': 1} .

# def count_characters(text):
#     return {character: text.count(character) for character in text if character.isalpha()}
#
#
# print(count_characters("Ana has apples."))

# 3. Compare two dictionaries without using the operator "==" returning True or False. (Attention, dictionaries must
# be recursively covered because they can contain other containers, such as dictionaries, lists, sets, etc.)

# def compare_dictionaries(first_dictionary, second_dictionary):
#     if len(first_dictionary) != len(second_dictionary):
#         return False
#
#     for key, value in first_dictionary.items():
#         if key not in second_dictionary:
#             return False
#
#         if type(value) == dict:
#             if not compare_dictionaries(value, second_dictionary[key]):
#                 return False
#
#         elif value != second_dictionary[key]:
#             return False
#
#     return True
#
#
# print(compare_dictionaries(
#     {"k1": 1, "k2": 2, "k3_dict": {"k3": 3, "k4": 4}},
#     {"k1": 1, "k2": 2, "k3_dict": {"k3": 3, "k4": 4}}
# ))

# 4. The build_xml_element function receives the following parameters: tag, content, and key-value elements given as
# name-parameters. Build and return a string that represents the corresponding XML element. Example:
# build_xml_element ("a", "Hello there", href =" http://python.org ", _class =" my-link ", id= " someId ") returns
# the string = "<a href=\"http://python.org \ "_class = \" my-link \ "id = \" someid \ "> Hello there </a>"

# def build_xml_element(tag, content, **parameters):
#     attributes = " ".join([f'{key}="{value}"' for key, value in parameters.items()])
#     return f"<{tag} {attributes}> {content} </{tag}>"
#
#
# print(build_xml_element("a", "Hello there", href="https://python.org", _class="my-link", id="someId"))


# 5. The validate_dict function that receives as a parameter a set of tuples ( that represents validation rules for a
# dictionary that has strings as keys and values) and a dictionary. A rule is defined as follows: (key, "prefix",
# "middle", "suffix"). A value is considered valid if it starts with "prefix", "middle" is inside the value (not at
# the beginning or end) and ends with "suffix". The function will return True if the given dictionary matches all the
# rules, False otherwise.
#
# Example: the rules  s={("key1", "", "inside", ""), ("key2", "start", "middle", "winter")}  and d= {"key1": "come
# inside, it's too cold out", "key3": "this is not valid"} => False because although the rules are respected for
# "key1" and "key2" "key3" that does not appear in the rules.

# def validate_dict(rules, dictionary):
#     for key, prefix, middle, suffix in rules:
#         if key not in dictionary:
#             return False
#
#         value = dictionary[key]
#         if not value.startswith(prefix) or not value.endswith(suffix) \
#                 or middle not in value[len(prefix):-len(suffix)]:
#             return False
#
#     return True
#
#
# print(validate_dict(
#     {("key1", "", "inside", ""), ("key2", "start", "middle", "winter")},
#     {"key1": "come inside, it's too cold out", "key2": "start middle winter"}
# ))

# 6. Write a function that receives as a parameter a list and returns a tuple (a, b), representing the number of
# unique elements in the list, and b representing the number of duplicate elements in the list (use sets to achieve
# this objective).

# def count_unique_and_duplicate_elements(elements):
#     unique_elements = set(elements)
#     return len(unique_elements), len(elements) - len(unique_elements)
#
#
# print(count_unique_and_duplicate_elements([0, 0, 1, 2, 3, 4, 4, 5]))

# 7. Write a function that receives a variable number of sets and returns a dictionary with the following operations
# from all sets two by two: reunion, intersection, a-b, b-a. The key will have the following form: "a op b",
# where a and b are two sets, and op is the applied operator: |, &, -.
#
# Ex: {1,2}, {2, 3} =>
# {
#     "{1, 2} | {2, 3}":  {1, 2, 3},
#     "{1, 2} & {2, 3}":  { 2 },
#     "{1, 2} - {2, 3}":  { 1 },
#     ...
# }

# def sets_operations(*sets):
#     operations = {
#         "|": lambda a, b: a | b,
#         "&": lambda a, b: a & b,
#         "-": lambda a, b: a - b
#     }
#
#     result = {
#         f"{sets[i]} {operation} {sets[j]}": function(sets[i], sets[j])
#         for i in range(len(sets))
#         for j in range(i + 1, len(sets))
#         for operation, function in operations.items()
#     }
#
#     return result
#
#
# for key, value in sets_operations({1, 2}, {2, 3}).items():
#     print(f"{key} = {value}")

# 8. Write a function that receives a single dict parameter named mapping. This dictionary always contains a string
# key "start". Starting with the value of this key you must obtain a list of objects by iterating over mapping in the
# following way: the value of the current key is the key for the next value, until you find a loop (a key that was
# visited before). The function must return the list of objects obtained as previously described.
#
# Ex: loop({'start': 'a', 'b': 'a', 'a': '6', '6': 'z', 'x': '2', 'z': '2', '2': '2', 'y': 'start'})
# will return ['a', '6', 'z', '2']

# def loop(mapping):
#     result = []
#     current_key = mapping["start"]
#     while current_key not in result:
#         result.append(current_key)
#         current_key = mapping[current_key]
#
#     return result
#
#
# print(loop({'start': 'a', 'b': 'a', 'a': '6', '6': 'z', 'x': '2', 'z': '2', '2': '2', 'y': 'start'}))

# 9. Write a function that receives a variable number of positional arguments and a variable number of keyword
# arguments and will return the number of positional arguments whose values can be found among keyword arguments
# values.
# Ex: my_function(1, 2, 3, 4, x=1, y=2, z=3, w=5) will return returna 3

# def my_function(*positional, **keyword):
#     return sum([1 for p in positional if p in keyword.values()])
#
#
# print(my_function(1, 2, 3, 4, x=1, y=2, z=3, w=5))
