import logging
import time

import requests

import config
from save import save_JSON_to_file

# Configure logging
logging.basicConfig(level=config.get_logging_level(), format='%(asctime)s - %(levelname)s - %(message)s')

def read_result(result_id):
    """
    Retrieves the result from the API using the provided result_id.

    Args:
        result_id (str): The identifier for the result.

    Returns:
        dict: The JSON result retrieved from the API.
    """
    url = f'{config.BASE_URL}/read_result'
    payload = {'result_id': result_id}

    retries = 0
    while retries < config.READ_MAX_RETRIES:
        try:
            retries += 1
            response = requests.post(url, headers=config.get_headers(), json=payload)
            if response.status_code == 200:
                data = response.json()
                return data['result']
            elif response.status_code == 404:
                logging.info(f"Attempt {retries}/{config.READ_MAX_RETRIES}: Result not ready yet. Waiting 5 seconds.")
                time.sleep(5)
                continue
            else:
                response.raise_for_status()
        except requests.exceptions.RequestException as e:
            logging.error(f'Error retrieving result from API: {e}')
            exit(1)
    logging.error('Read result retries exceeded. Exiting.')
    exit(1)
