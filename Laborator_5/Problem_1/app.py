from utils import process_item


while True:
    try:
        x = input('Enter a number: ')
        
        if x == 'q':
            break
            
        prime_number = process_item(int(x))
        print( f'\tFirst prime number greater than {x} is {prime_number}\n')

    except ValueError:
        print('\tPlease enter a valid number!\n')