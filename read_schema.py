import logging
import requests

import config
from read_result import read_result  # Import read_result function
from save import save_JSON_to_file  # Import save_JSON_to_file function

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def read_schema(pdf_file_path):
    """
    Generates the schema for a given PDF file and saves it as a JSON file.

    Args:
        pdf_file_path (str): Path to the PDF file.
    """
    logging.info('Starting the schema generation process.')

    # Read the PDF file
    logging.debug(f'Reading PDF file from {pdf_file_path}.')
    with open(pdf_file_path, 'rb') as pdf_file:
        pdf_contents = pdf_file.read()

    # Send the PDF to the API to generate the schema
    logging.debug('Sending PDF to the API for schema generation.')
    result_id = send_pdf_for_schema(pdf_contents)
    logging.info(f"Schema generation request sent. Result ID: {result_id}")

    # Retrieve and save the result
    result = read_result(result_id)
    save_JSON_to_file(result, f'results/{result_id}')
    logging.info(f"Schema saved to results/{result_id}")
    logging.info('Schema generation process completed successfully.')

def send_pdf_for_schema(pdf_contents):
    """
    Sends a PDF file to the API endpoint to generate a schema.

    Args:
        pdf_contents (bytes): The binary contents of the PDF file.

    Returns:
        str: The result_id provided by the API to retrieve the schema.
    """
    url = f'{config.BASE_URL}/read_pdf_schema'
    files = {'pdf_sample_form': ('input.pdf', pdf_contents, 'application/pdf')}

    try:
        logging.debug(f'Sending POST request to {url}.')
        response = requests.post(url, headers=config.get_headers(), files=files)
        response.raise_for_status()
        data = response.json()
        result_id = data['result_id']
        logging.debug(f'Received result_id: {result_id}.')
        return result_id
    except requests.exceptions.RequestException as e:
        logging.error(f'Error sending PDF to API: {e}')
        exit(1)
