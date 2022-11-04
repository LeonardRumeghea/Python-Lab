import os
import PyPDF2
# import docx
# import textract
import docx2txt


# 1.
# def get_extensions(director):
#
#     if os.path.exists(director) is False:
#         raise TypeError('Path is incorrect!')
#
#     if os.path.isdir(director) is False:
#         raise TypeError("The path is not a directory!")
#
#     return sorted({file.split('.')[-1] for file in os.listdir(director)
#                    if file.__contains__('.') and os.path.isfile(os.path.join(director, file))})
#
#
# try:
#     print(get_extensions('D:\\Documents\\GitHub\\Python-Lab\\Laborator_4\\Folder'))
# except TypeError as e:
#     print(e)


# 2.
# def get_files(director, write_to):
#     if os.path.exists(director) is False:
#         raise TypeError('Path is incorrect!')
#
#     if os.path.isdir(director) is False:
#         raise TypeError("The path is not a directory!")
#
#     files = (os.path.join(director, file) for file in os.listdir(director)
#              if file.startswith('A') and os.path.isfile(os.path.join(director, file)))
#
#     with open(write_to, 'w') as f:
#         f.writelines('\n'.join(files))
#
#
# try:
#     get_files(
#         director='D:\\Documents\\GitHub\\Python-Lab\\Laborator_4\\Folder',
#         write_to='D:\\Documents\\GitHub\\Python-Lab\\Laborator_4\\Folder\\Paths.txt'
#     )
# except TypeError as e:
#     print(e)


# 3.
# def get_last_20_chars_or_extensions(my_path):
#
#     if os.path.exists(my_path) is False:
#         raise TypeError('Path is incorrect!')
#
#     if os.path.isfile(my_path):
#         with open(my_path, 'r', encoding='utf-8') as f:
#             return f.read()[-20:]
#
#     if os.path.isdir(my_path):
#         extensions = {}
#         for files in os.walk(my_path):
#             # file[0] - director path
#             # file[1] - sub-directories list
#             # file[2] - files list
#             for file in files[2]:
#                 if file.__contains__('.') and os.path.isfile(os.path.join(str(files[0]), str(file))):
#                     extensions.update({file.split('.')[-1]: extensions.get(key=file.split('.')[-1], value=0) + 1})
#
#         return sorted(extensions.items(), key=lambda x: x[1], reverse=True)
#
#
# try:
#     print(get_last_20_chars_or_extensions('D:\\Documents\\GitHub\\Python-Lab\\Laborator_4\\Folder\\A1.txt'))
# except TypeError as e:
#     print(e)


# 4.
# def get_extensions(director):
#
#     if os.path.exists(director) is False:
#         raise TypeError('Path is incorrect!')
#
#     if os.path.isdir(director) is False:
#         raise TypeError("The path is not a directory!")
#
#     return sorted({file.split('.')[-1] for file in os.listdir(director)
#                    if file.__contains__('.') and os.path.isfile(os.path.join(director, file))})


# py .\main.py D:\Documents\GitHub\Python-Lab\Laborator_4\Folder
# print(get_extensions(sys.argv[1]))
# print(get_extensions('D:\\Documents\\GitHub\\Python-Lab\\Laborator_4\\Folder'))


# 5.
# def file_contains_target(target, to_search):
#
#     try:
#         if target.endswith('.docx'):
#             return to_search in docx2txt.process(target)
#
#         if target.endswith('.pdf'):
#             with open(target, 'rb') as f:
#                 pdf_reader = PyPDF2.PdfFileReader(f)
#                 for page in range(pdf_reader.numPages):
#                     if pdf_reader.getPage(page).extractText().find(to_search) != -1:
#                         return True
#                 return False
#
#         with open(target, 'r', encoding='utf-8') as f:
#             return to_search in f.read()
#
#     except Exception as exception:
#         print(f'An error occurred while processing the file: {target}\n\t{str(exception)}\n')
#         return False
#
#
# def get_files_who_contains(target, to_search):
#
#     if os.path.exists(target) is False:
#         raise ValueError('Path is incorrect!')
#
#     if os.path.isfile(target):
#         return [target] if file_contains_target(target, to_search) else []
#
#     if os.path.isdir(target):
#         files = (file for file in os.listdir(target) if os.path.isfile(os.path.join(target, file)))
#         return [file for file in files if file_contains_target(os.path.join(target, file), to_search)]
#
#     raise ValueError('Invalid path!')
#
#
# try:
#     print(get_files_who_contains('D:\\Documents\\GitHub\\Python-Lab\\Laborator_4\\Folder', 'mesaj'))
# except TypeError as e:
#     print(e)


# 6.
# def file_contains_target(target, to_search, callback_function):
#
#     try:
#         if target.endswith('.docx'):
#             return to_search in docx2txt.process(target)
#
#         if target.endswith('.pdf'):
#             with open(target, 'rb') as f:
#                 pdf_reader = PyPDF2.PdfFileReader(f)
#                 for page in range(pdf_reader.numPages):
#                     if pdf_reader.getPage(page).extractText().find(to_search) != -1:
#                         return True
#                 return False
#
#         with open(target, 'r', encoding='utf-8') as f:
#             return to_search in f.read()
#
#     except Exception as exception:
#         callback_function(f'An error occurred while processing the file: {target}\n\t{str(exception)}\n')
#         return False
#
#
# def throw_exception(error):
#     # raise error
#     print(error)
#
#
# def get_files(target, to_search, callback_function):
#
#     if os.path.exists(target) is False:
#         callback_function(ValueError('Path is incorrect!'))
#
#     if os.path.isfile(target):
#         return [target] if file_contains_target(target, to_search, callback_function) else []
#
#     if os.path.isdir(target):
#         files = (file for file in os.listdir(target) if os.path.isfile(os.path.join(target, file)))
#         return [file for file in files if file_contains_target(os.path.join(target, file), to_search, callback_function)]
#
#     callback_function(ValueError('Invalid path!'))
#
#
# try:
#     print(get_files('D:\\Documents\\GitHub\\Python-Lab\\Laborator_4\\Folder', 'mesaj', throw_exception))
# except TypeError as e:
#     print(e)


# 7.
# def get_file_info(file):
#
#     if os.path.exists(file) is False:
#         raise ValueError('Path is incorrect!')
#
#     if os.path.isfile(file) is False:
#         raise ValueError('The path is not a file!')
#
#     return {
#         'full_path': os.path.abspath(file),
#         'file_size': os.path.getsize(file),
#         'file_extension': file.split('.')[-1] if file.__contains__('.') else '',
#         'can_read': os.access(file, os.R_OK),
#         'can_write': os.access(file, os.W_OK)
#     }
#
#
# try:
#     print('For main.py: ')
#     for key, value in get_file_info('D:\\Documents\\GitHub\\Python-Lab\\Laborator_4\\main.py').items():
#         print(f'\t{key.replace("_", " ")}: {value}')
#
#     print('\nFor linux_file: ')
#     for key, value in get_file_info('D:\\Documents\\GitHub\\Python-Lab\\Laborator_4\\Folder\\linux_file').items():
#         print(f'\t{key.replace("_", " ")}: {value}')
#
# except Exception as e:
#     print(e)


# 8.
# def get_files(dir_path):
#
#     if os.path.exists(dir_path) is False:
#         raise ValueError('Path is incorrect!')
#
#     if os.path.isdir(dir_path) is False:
#         raise ValueError('The path is not a directory!')
#
#     files = []
#     for obj in os.listdir(dir_path):
#         files.extend([os.path.join(dir_path, obj)]
#                      if os.path.isfile(os.path.join(dir_path, obj))
#                      else get_files(os.path.join(dir_path, obj)))
#
#     return files
#
#
# try:
#     for path in get_files('D:\\Documents\\GitHub\\Python-Lab\\Laborator_4'):
#         print(path)
# except Exception as e:
#     print(e)
