from utils import process_item


while True:
    try:
        x = input('Enter a number: ')
        
        if x == 'q':
            break

        x = int(x)
        print(process_item(x))

    except ValueError:
        print('Please enter a valid number!')