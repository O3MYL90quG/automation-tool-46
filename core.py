import sys

class InputValidationError(Exception):
    pass

def validate_input(user_input):
    if not isinstance(user_input, str) or len(user_input.strip()) == 0:
        raise InputValidationError("Input must be a non-empty string")

def process_data(user_input):
    validate_input(user_input)  # Validate input here
    # Simulate processing the validated input
    print(f"Processing: {user_input}")

if __name__ == '__main__':
    while True:
        try:
            user_input = input('Enter some data (or type "exit" to quit): ')
            if user_input.lower() == 'exit':
                print('Exiting...')
                sys.exit(0)
            process_data(user_input)
        except InputValidationError as e:
            print(f'Input error: {e}')
        except Exception as e:
            print(f'An unexpected error occurred: {e}')