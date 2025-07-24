import logging

def handle_error(error):
    # Log the error
    logging.error(error)
    # Handle the error
    print(f'An error occurred: {error}')
