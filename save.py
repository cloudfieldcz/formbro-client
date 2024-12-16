import json
import logging
import os

def save_JSON_to_file(data, file_path):
    """
    Saves the dictionary to a JSON file.

    Args:
        data (dict): The data to save.
        file_path (str): The file path where to save the JSON.
    """
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    try:
        logging.debug(f'Writing data to {file_path}.')
        with open(file_path, 'w') as json_file:
            json.dump(data, json_file, indent=4)
        logging.debug('Schema saved successfully.')
    except IOError as e:
        logging.error(f'Error saving schema to file: {e}')
        exit(1)
