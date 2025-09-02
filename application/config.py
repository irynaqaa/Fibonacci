"""
Configuration management for the data processing application.
"""
import json
import os

CONFIG_FILE = 'config.json'


def load_config():
    """
    Load configuration settings from a JSON file.
    """
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, 'r', encoding='utf-8') as f:
            config = json.load(f)
            return config
    else:
        raise FileNotFoundError(f'Configuration file not found: {CONFIG_FILE}')


def validate_config(config):
    """
    Validate the loaded configuration settings.
    """
    # Add validation logic here
    return True
