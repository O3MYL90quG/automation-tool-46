import sys


def is_valid_input(user_input):
    if not user_input:
        print('Input cannot be empty.')
        return False
    if not isinstance(user_input, str):
        print('Input must be a string.')
        return False
    return True


def process_input(user_input):
    if not is_valid_input(user_input):
        return
    # Simulate some processing on the valid input
    print(f'Processing: {user_input}')


def main():
    while True:
        user_input = input('Enter some data (or type "exit" to quit): ')
        if user_input.lower() == 'exit':
            print('Exiting...')
            sys.exit(0)
        process_input(user_input)


if __name__ == '__main__':
    main()