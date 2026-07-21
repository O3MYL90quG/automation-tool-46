import sys

class InputValidationError(Exception):
    pass

class DataProcessor:
    def __init__(self):
        self.processed_data = []

    def validate_input(self, user_input):
        if not isinstance(user_input, str) or not user_input:
            raise InputValidationError('Input must be a non-empty string.')
        return user_input.strip()

    def process_input(self, user_input):
        valid_input = self.validate_input(user_input)
        processed = valid_input.upper()  # Example processing
        self.processed_data.append(processed)

    def main_loop(self):
        while True:
            user_input = input('Enter a string (or type "exit" to quit): ')
            if user_input.lower() == 'exit':
                break
            try:
                self.process_input(user_input)
                print(f'Processed data: {self.processed_data}')
            except InputValidationError as e:
                print(f'Error: {e}')

if __name__ == '__main__':
    processor = DataProcessor()
    processor.main_loop()