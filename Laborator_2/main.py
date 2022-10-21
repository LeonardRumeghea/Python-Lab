# 1. Write a function to return a list of the first n numbers in the Fibonacci string.

# def fibonacci(n):
#
#     if n <= 0:
#         return []
#     elif n == 1:
#         return [1]
#
#     fib = [0, 1]
#     for i in range(2, n):
#         fib.append(fib[i-1] + fib[i-2])
#     return fib
#
#
# print(fibonacci(12))

# 2. Write a function that receives a list of numbers and returns a list of the prime numbers found in it.

# def is_prime(number):
#     if number < 2:
#         return False
#     for i in range(2, number):
#         if number % i == 0:
#             return False
#     return True
#
#
# def prime_numbers_from_list(numbers):
#     if numbers is None:
#         return None
#     prime_numbers = [number for number in numbers if is_prime(number)]
#     return prime_numbers
#
#
# print(prime_numbers_from_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

# 2. Write a function that receives as parameters two lists a and b and returns: (A intersected with B,
# A reunited with B, A - B, B - A)

# def intersect(a, b):
#     return [value for value in a if value in b]
#
#
# def union(a, b):
#     return a + [value for value in b if value not in a]
#
#
# def difference(a, b):
#     return [value for value in a if value not in b]
#
#
# def sets(a, b):
#     if a is None:
#         return None
#     if b is None:
#         return None
#     return intersect(a, b), union(a, b), difference(a, b), difference(b, a)
#
#
# print(sets([1, 2, 3, 4, 5], [3, 4, 5, 6, 7]))

# 4. Write a function that receives as a parameters a list of musical notes (strings), a list of moves (integers) and
# a start position (integer). The function will return the song composed by going through the musical notes beginning
# with the start_position position and following the moves given as parameter.
# Example : compose(["do", "re", "mi", "fa", "sol"], [1, -3, 4, 2], 2)
# will return ["mi", "fa", "do", "sol", "re"]

# def compose(notes, moves, start_position):
#     song = [notes[start_position]]
#     for move in moves:
#         start_position += move
#         if start_position < 0:
#             start_position = len(notes) + start_position
#         elif start_position >= len(notes):
#             start_position = start_position - len(notes)
#         song.append(notes[start_position])
#     return song
#
#
# print(compose(["do", "re", "mi", "fa", "sol"], [1, -3, 4, 2], 2))

# 5. Write a function that receives as parameter a matrix and will return the matrix obtained by replacing all the
# elements under the main diagonal with 0 (zero).

# def replace_under_main_diagonal(matrix):
#     matrix_len = len(matrix)
#     for i in range(1, matrix_len):
#         for j in range(i):
#             matrix[i][j] = 0
#     return matrix
#
#
# print(replace_under_main_diagonal([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))

# 6. Write a function that receives as a parameter a variable number of lists and a whole number x.
# Return a list containing the items that appear exactly x times in the incoming lists.
# Example: For the [1,2,3], [2,3,4],[4,5,6], [4,1, "test"] and x = 2 lists [1,2,3 ] # 1 is in list 1 and 4, 2
# is in list 1 and 2, 3 is in lists 1 and 2.

# def x_times_in_lists(x, *lists):
#     result = []
#     appearances = {}
#     for lst in lists:
#         for item in lst:
#             appearances[item] = appearances.get(item, 0) + 1
#             result.append(item) if appearances[item] == x else result.remove(item) if appearances[item] > x else None
#     return result
#
#
# print(x_times_in_lists(2, [1, 2, 3], [2, 3, 4], [4, 5, 6], [4, 1, "test"]))

# 7.  Write a function that receives as parameter a list of numbers (integers) and will return a tuple with 2
# elements. The first element of the tuple will be the number of palindrome numbers found in the list and the second
# element will be the greatest palindrome number.

# def palindrome_numbers(numbers):
#     palindrome_numbers_list = [number for number in numbers if str(number) == str(number)[::-1]]
#     return len(palindrome_numbers_list), max(palindrome_numbers_list)
#
#
# print(palindrome_numbers([121, 220, 12321, 321, 123, 1234, 123321, 1234321, 12345, 123456, 1234567, 12345678, ]))

# 8.  Write a function that receives a number x, default value equal to 1, a list of strings, and a boolean flag set
# to True. For each string, generate a list containing the characters that have the ASCII code divisible by x if the
# flag is set to True, otherwise it should contain characters that have the ASCII code not divisible by x.
#  Example: x = 2, ["test", "hello", "lab002"], flag = False will return (["e", "s"], ["e", "o"], ["a"])
#  Note: The function must return list of lists.

# def ascii_code_divisible_by_x(x, strings, flag):
#     return [[char for char in string if (ord(char) % x == 0) == flag] for string in strings]
#
#
# print(ascii_code_divisible_by_x(2, ["test", "hello", "lab002"], False))

# 9. Write a function that receives as paramer a matrix which represents the heights of the spectators in a stadium
# and will return a list of tuples (line, column) each one representing a seat of a spectator which can't see the
# game. A spectator can't see the game if there is at least one taller spectator standing in front of him. All the
# seats are occupied. All the seats are at the same level. Row and column indexing starts from 0, beginning with the
# closest row from the field.
#
# 	Example:
# FIELD
# [[1, 2, 3, 2, 1, 1],
# [2, 4, 4, 3, 7, 2],
# [5, 5, 2, 5, 6, 4],
# [6, 6, 7, 6, 7, 5]]
#
# Will return : [(2, 2), (3, 4), (2, 4)]

# METHOD 1 - BASIC: if every row has the same length
# def seats(matrix):
#     result = []
#     rows = len(matrix)
#     columns = len(matrix[0])
#     for j in range(columns):
#         tallest_up_to_him = 0
#         for i in range(rows):
#             if matrix[i][j] <= tallest_up_to_him:
#                 result.append((i, j))
#             else:
#                 tallest_up_to_him = matrix[i][j]
#     return result
#
# METHOD 2 - FANCY: if every row has a different length.
# def seats(matrix):
#     tallest_up_to_him = [0] * (max([len(row) for row in matrix]))
#     return [(i, j) for i in range(len(matrix)) for j in range(len(matrix[i]))
#             if matrix[i][j] <= tallest_up_to_him[j] or tallest_up_to_him.__setitem__(j, matrix[i][j])
#             ]
#
#
# print(seats([
#     [1, 2, 3, 2, 1, 1],
#     [2, 4, 4, 3, 7, 2, 5],
#     [5, 5, 2, 5, 6, 4, 4, 5],
#     [6, 6, 7, 6, 7, 5]
# ]))

# 10.  Write a function that receives a variable number of lists and returns a list of tuples as follows: the first
# tuple contains the first items in the lists, the second element contains the items on the position 2 in the lists,
# etc. Ex: for lists [1,2,3], [5,6,7], ["a", "b", "c"] return: [(1, 5, "a ") ,(2, 6, "b"), (3,7, "c")].

# Note: If input lists do not have the same number of items, missing items will be replaced with None to be able to
# generate max ([len(x) for x in input_lists]) tuples.

# def tuples(*lists):
#     max_list_len = max([len(lst) for lst in lists])
#     return [tuple(lst[i] if i < len(lst) else None for lst in lists) for i in range(max_list_len)]
#
#
# print(tuples([1, 2, 3], [5, 6, 7, 9, 8], ["a", "b", "c", "d"]))

# 11. Write a function that will order a list of string tuples based on the 3rd character of the 2nd element in the
# tuple. Example: ('abc', 'bcd'), ('abc', 'zza')] ==> [('abc', 'zza'), ('abc', 'bcd')]

# def order_tuples(tuples):
#     if len(tuples) == 0:
#         return tuples
#     if tuples is None:
#         return None
#     return sorted(tuples, key=lambda x: x[1][2])
#
#
# print(order_tuples([('abc', 'bcd'), ('abc', 'zza')]))

# 12.  Write a function that will receive a list of words  as parameter and will return a list of lists of words,
# grouped by rhyme. Two words rhyme if both of them end with the same 2 letters.
# 	Example: group_by_rhyme(['ana', 'banana', 'carte', 'arme', 'parte'])
# 	will return [['ana', 'banana'], ['carte', 'parte'], ['arme']]

# METHOD 1 - BASIC - O(n^2) in the worst case (when no words rhyme with each other)
# def group_by_rhyme(words):
#     result = []
#     for word in words:
#         for group in result:
#             if len(word) > 2 and word[-2:] == group[0][-2:]:
#                 group.append(word)
#                 break
#         else:
#             result.append([word])
#     return result
#
#
# METHOD 2 - FANCY - O(n * log n) in the worst case (when no words rhyme with other)\
# def group_by_rhyme(words):
#     words = sorted(words, key=lambda x: x[-2:])  # sort by last 2 letters - O(n * log n)
#     print(words)
#     buckets = [[words[0]]]
#     [buckets[-1].append(word) if word[-2:] == buckets[-1][0][-2:] else buckets.append([word]) for word in words[1:]]
#     return buckets
#
#
# print(group_by_rhyme(['ana', 'banana', 'carte', 'arme', 'parte']))
