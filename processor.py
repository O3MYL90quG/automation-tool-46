import json
import os

class DataProcessor:
    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file

    def read_data(self):
        with open(self.input_file, 'r') as file:
            return json.load(file)

    def process_data(self, data):
        # Example processing: filter out None values
        return {k: v for k, v in data.items() if v is not None}

    def write_data(self, data):
        with open(self.output_file, 'w') as file:
            json.dump(data, file, indent=4)

    def execute(self):
        data = self.read_data()
        processed_data = self.process_data(data)
        self.write_data(processed_data)

if __name__ == '__main__':
    processor = DataProcessor('input.json', 'output.json')
    processor.execute()