# 1. Find The greatest common divisor of multiple numbers read from the console.

# def gcd(a, b):
#     while b:
#         a, b = b, a % b
#     return a
#
#
# def main():
#     # numbers = [int(x) for x in input("Enter numbers: ").split()]
#     numbers = input("Enter numbers: ").split()
#     converted_numbers = []
#     for number in numbers:
#         if not number.isdigit():
#             print("Please enter only numbers.")
#             return
#         converted_numbers.append(int(number))
#
#     result = converted_numbers[0]
#     for number in converted_numbers[1:]:
#         result = gcd(result, number)
#     print(result)
#
#
# if __name__ == "__main__":
#     main()

# 2. Write a script that calculates how many vowels are in a string.

# def count_vowels(string):
#     counter = 0
#     for char in string:
#         if char in 'aeiouAEIOU':
#             counter += 1
#     return counter


# print(count_vowels('hello world'))

# 3. Write a script that receives two strings and prints the number of occurrences of the first string in the second.

# def count_occurrences(substring, string):
#     return string.count(substring)
#
#
# def main():
#     string = input("Enter string: ")
#     substring = input("Enter substring: ")
#     print(count_occurrences(substring, string))
#
#
# if __name__ == "__main__":
#     main()

# 4. Write a script that converts a string of characters written in UpperCamelCase into lowercase_with_underscores.

# def convert(string):
#     result = ''
#     for char in string:
#         if char.isupper():
#             result += '_' + char.lower()
#         else:
#             result += char
#     if result[0] == '_':
#         result = result[1:]
#     return result
#
#
# print(convert('HelloWorld'))

# 5. Given a square matrix of characters writes a script that prints the string obtained by going through the matrix
# in spiral order (as in the example):

# def spiral(matrix):
#     moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]
#     result = ''
#     i, j = 0, 0
#     move = 0
#     while matrix:
#         result += matrix[i][j]
#         matrix[i][j] = None
#         next_i, next_j = i + moves[move][0], j + moves[move][1]
#         if 0 <= next_i < len(matrix) and 0 <= next_j < len(matrix[0]) and matrix[next_i][next_j] is not None:
#             i, j = next_i, next_j
#         else:
#             move = (move + 1) % 4
#             i, j = i + moves[move][0], j + moves[move][1]
#             if matrix[i][j] is None:
#                 break
#     return result


# print(spiral([
#     ['f', 'i', 'r', 's'],
#     ['n', '_', 'l', 't'],
#     ['o', 'b', 'a', '_'],
#     ['h', 't', 'y', 'p'],
# ]))

# 6. Write a function that validates if a number is a palindrome.

# def is_palindrome(number):
#     return str(number) == str(number)[::-1]


# print(is_palindrome(12321))

# 7. Write a function that extract a number from a text (for example if the text is "An apple is 123 USD",
# this function will return 123, or if the text is "abc123abc" the function will extract 123). The function will
# extract only the first number that is found.

# def extract_number(string):
#     result = ''
#     for char in string:
#         if char.isdigit():
#             result += char
#         elif result != '':
#             break
#     return int(result)


# print(extract_number('An apple is 123 USD'))
# print(extract_number('abc123abc'))

# 8. Write a function that counts how many bits with value 1 a number has. For example for number 24, the binary
# format is 00011000, meaning 2 bits with value "1"

# def count_bits(number):
#     return bin(number).count('1')
#
#
# print(count_bits(24))

# 9. Write a functions that determine the most common letter in a string. For example if the string is "an apple is
# not a tomato", then the most common character is "a" (4 times). Only letters (A-Z or a-z) are to be considered.
# Casing should not be considered "A" and "a" represent the same character.

# def most_common_letter(string):
#     counter = {}
#     for char in string.lower():
#         if char.isalpha():
#             counter[char] = counter.get(char, 0) + 1
#     return max(counter, key=counter.get)


# print(most_common_letter('an apple is not a tomato'))

# 10. Write a function that counts how many words exists in a text. A text is considered to be form out of words that
# are separated by only ONE space. For example: "I have Python exam" has 4 words.

# def count_words(string):
#     return len(string.split(' '))


# print(count_words('I have Python exam'))
