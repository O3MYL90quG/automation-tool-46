import re

def validate_input(user_input):
    """
    Validate the user input against specific criteria.
    Returns True if valid, False otherwise.
    """
    if not isinstance(user_input, str):
        return False
    
    # Check if the input is not empty
    if not user_input:
        return False
    
    # Check input length
    if len(user_input) < 3 or len(user_input) > 20:
        return False
    
    # Allow only alphanumeric characters and underscores
    if not re.match(r'^[a-zA-Z0-9_]*$', user_input):
        return False
    
    return True


def main_processing_loop():
    while True:
        user_input = input('Enter your input (or type exit to quit): ')
        if user_input.lower() == 'exit':
            break
        
        if validate_input(user_input):
            print(f'Valid input: {user_input}')
        else:
            print('Invalid input. Please try again.')