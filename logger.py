# logger.py
import logging
from logging.handlers import RotatingFileHandler

# Configure the logger
def setup_logger(log_file='app.log', max_bytes=10**6, backup_count=5):
    # Create a logger
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)  # Set the log level to DEBUG

    # Create a file handler with rotation
    handler = RotatingFileHandler(log_file, maxBytes=max_bytes, backupCount=backup_count)
    handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))

    # Add the handler to the logger
    logger.addHandler(handler)
    
    return logger

# Example usage
if __name__ == '__main__':
    logger = setup_logger()
    logger.info('Logger has been set up.')  # Log an info message
