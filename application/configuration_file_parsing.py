import configparser

def parse_configuration_file(file_path):
    try:
        # Create a ConfigParser object
        config = configparser.ConfigParser()
        # Read the configuration file
        config.read(file_path)
        # Get the configuration values
        input_file = config.get('Input', 'file')
        output_file = config.get('Output', 'file')
        return input_file, output_file
    except Exception as e:
        print(f"Error: {e}")
        return None
