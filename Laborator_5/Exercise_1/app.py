from utils import process_item


while True:
    try:
        x = input('Enter a number: ')
        
        if x == 'q':
            break

        print(process_item(int(x)))

    except ValueError:
        print('Please enter a valid number!')