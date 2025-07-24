import logging

def configure_logging():
    # Configure the logger
    logging.basicConfig(level=logging.DEBUG)
    # Create a file handler
    file_handler = logging.FileHandler('log.txt')
    # Create a console handler
    console_handler = logging.StreamHandler()
    # Create a formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    # Add the formatter to the handlers
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)
    # Add the handlers to the logger
    logging.getLogger().addHandler(file_handler)
    logging.getLogger().addHandler(console_handler)
