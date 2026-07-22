import json
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

class AutomationTool:
    def __init__(self, data):
        self.data = data

    def validate_data(self):
        if not isinstance(self.data, dict):
            logging.error('Data must be a dictionary')
            raise ValueError('Invalid data format. Expected a dictionary.')
        if 'name' not in self.data or 'value' not in self.data:
            logging.error('Missing required fields in data dictionary')
            raise KeyError('Both name and value keys must be present in the data.')

    def process_data(self):
        self.validate_data()
        name = self.data['name']
        value = self.data['value']
        try:
            result = self.perform_action(name, value)
            logging.info(f'Data processed successfully: {result}')
            return result
        except Exception as e:
            logging.error(f'Error processing data: {str(e)}')
            raise

    def perform_action(self, name, value):
        if not isinstance(value, (int, float)):
            logging.error('Value must be a number')
            raise TypeError('Value must be a number.')
        return f'The action on {name} with value {value} was successful.'

if __name__ == '__main__':
    try:
        sample_data = {'name': 'Sample', 'value': 10}
        tool = AutomationTool(sample_data)
        print(tool.process_data())
    except Exception as e:
        logging.critical(f'Failed to run automation tool: {str(e)}')