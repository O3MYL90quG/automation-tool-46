import json
import logging

logging.basicConfig(level=logging.INFO)

class DataProcessor:
    def __init__(self, data):
        self.data = data

    def validate_data(self):
        if not isinstance(self.data, dict):
            raise ValueError('Data must be a dictionary')
        if 'key' not in self.data:
            raise KeyError('Missing required key in data')

    def process_data(self):
        self.validate_data()
        return json.dumps(self.data)

def main():
    sample_data = {'key': 'value', 'other_key': 'other_value'}
    processor = DataProcessor(sample_data)
    try:
        processed_data = processor.process_data()
        logging.info('Processed data: %s', processed_data)
    except (ValueError, KeyError) as e:
        logging.error('Error occurred: %s', e)
        return json.dumps({'error': str(e)})

if __name__ == '__main__':
    main()