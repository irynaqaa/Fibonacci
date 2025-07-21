import configparser

"""
Module for reading configuration from config.ini file.
"""

def read_config():
    """
    Read the configuration from the config.ini file.

    Returns:
        config (ConfigParser): The configuration object.
    """
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config
