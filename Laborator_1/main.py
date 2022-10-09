'''
Comemtarii generale: nu e nevoie sa comentezi tot si sa faci cate o functie main si dupa sa mai faci si artificiul cu if __name__ == '__main__'. Poti avea doar un singur artificiu,
iar in interior sa apelezi ce iti doresti tu. Ar fi nice daca ai sti exact care e treaba cu acest artificiu, ce face si pentru ce e folosit, dar daca nu, o sa aflam toti la cursu cu packages.
'''

# 1. Find The greatest common divisor of multiple numbers read from the console.
''' 
prima problema e in regula.

'''
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
'''
a doua problema e in regula. am vazut ca ai folosit list comprehension si la 1., ai putea si aici, apoi sa folosesti built in functions, cum ar fi sum sau len.
'''
# def count_vowels(string):
#     counter = 0
#     for char in string:
#         if char in 'aeiouAEIOU':
#             counter += 1
#     return counter
#
#
# def main():
#     string = input("Enter a string: ")
#     print("Number of vowels:", count_vowels(string))
#
#
# if __name__ == "__main__":
#     main()

# 3. Write a script that receives two strings and prints the number of occurrences of the first string in the second.
'''
munctioreasca metoda, e foarte in regula, atinge corner case-urile pe care unii colegi nu au reusit sa le acopere. pe viitor ai putea incerca sa vezi cum ar functiona functia 'find'.
'''
# def count_occurrences(substring, string):
#     counter = 0
#     for i in range(len(string) - len(substring) + 1):
#         if string[i:i + len(substring)] == substring:
#             counter += 1
#     return counter
#
#
# def main():
#     string = input("Enter string: ")
#     substring = input("Enter substring: ")
#     print("Number of occurrences:", count_occurrences(substring, string))
#
#
# if __name__ == "__main__":
#     main()

# 4. Write a script that converts a string of characters written in UpperCamelCase into lowercase_with_underscores.
'''
looks good
'''
# def convert(string):
#     return ''.join(['_' + char.lower() if char.isupper() else char for char in string]).lstrip('_')
#
#
# def main():
#     string = input("Enter string: ")
#     print("Converted string:", convert(string))
#
#
# if __name__ == "__main__":
#     main()

# 5. Given a square matrix of characters writes a script that prints the string obtained by going through the matrix
# in spiral order (as in the example):
'''
nice
'''
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
#
#
# def main():
#     spiral([
#         ['f', 'i', 'r', 's'],
#         ['n', '_', 'l', 't'],
#         ['o', 'b', 'a', '_'],
#         ['h', 't', 'y', 'p'],
#     ])
#     print("Result: ", spiral)
#
#
# if __name__ == "__main__":
#     main()

# 6. Write a function that validates if a number is a palindrome.
'''
great
'''
# def is_palindrome(number):
#     return str(number) == str(number)[::-1]
#
#
# def main():
#     number = input("Enter number: ")
#     if not number.isdigit():
#         print("Please enter only numbers.")
#         return
#     else:
#         if is_palindrome(number):
#             print(number + " is a palindrome.")
#         else:
#             print(number + " is not a palindrome.")
#
#
# if __name__ == "__main__":
#     main()

# 7. Write a function that extract a number from a text (for example if the text is "An apple is 123 USD",
# this function will return 123, or if the text is "abc123abc" the function will extract 123). The function will
# extract only the first number that is found.
'''
great
'''
# def extract_number(string):
#     result = ''
#     for char in string:
#         if char.isdigit():
#             result += char
#         elif result != '':
#             break
#     if result == '':
#         return None
#     return int(result)
#
#
# def main():
#     string = input("Enter string: ")
#     print("Extracted number:", extract_number(string))
#
#
# if __name__ == "__main__":
#     main()

# 8. Write a function that counts how many bits with value 1 a number has. For example for number 24, the binary
# format is 00011000, meaning 2 bits with value "1"
'''
yep, perfect
'''
# def count_bits(number):
#     return bin(number).count('1')
#
#
# def main():
#     number = input("Enter number: ")
#     if not number.isdigit():
#         print("Please enter only numbers.")
#         return
#     else:
#         print("Number of bits with value 1:", count_bits(int(number)))
#
#
# if __name__ == "__main__":
#     main()

# 9. Write a functions that determine the most common letter in a string. For example if the string is "an apple is
# not a tomato", then the most common character is "a" (4 times). Only letters (A-Z or a-z) are to be considered.
# Casing should not be considered "A" and "a" represent the same character.
'''
great
'''
# def most_common_letter(string):
#     counter = {}
#     for char in string.lower():
#         if char.isalpha():
#             counter[char] = counter.get(char, 0) + 1
#     return max(counter, key=counter.get)
#
#
# def main():
#     string = input("Enter string: ")
#     if not string.isalpha():
#         print("Please enter only letters.")
#         return
#     print("Most common letter:", most_common_letter(string))
#
#
# if __name__ == "__main__":
#     main()

# 10. Write a function that counts how many words exists in a text. A text is considered to be form out of words that
# are separated by only ONE space. For example: "I have Python exam" has 4 words.
'''
great
'''
# def count_words(string):
#     return len(string.strip().split(' '))
#
#
# def main():
#     string = input("Enter string: ")
#     print("Number of words:", count_words(string))
#
#
# if __name__ == "__main__":
#     main()
