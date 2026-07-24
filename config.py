import json
import os

DEFAULT_CONFIG = {
    'app_name': 'Automation Tool',
    'version': '1.0',
    'log_level': 'INFO',
    'max_retries': 3,
    'timeout': 30,
}

def load_config(file_path='config.json'):
    """Load configuration from a JSON file, merging with defaults."""
    config = DEFAULT_CONFIG.copy()  # Start with default config
    
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            try:
                user_config = json.load(f)
                config.update(user_config)  # Merge user config with defaults
            except json.JSONDecodeError:
                print('Error decoding JSON from config file.')
    else:
        print('Config file does not exist; using defaults.')
    
    return config

if __name__ == '__main__':
    config = load_config()
    print(config)