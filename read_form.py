import logging
import requests

import config
from read_result import read_result
from save import save_JSON_to_file

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def read_form(pdf_file_path, json_schema_path):
    """
    Reads data from a PDF form using a JSON schema and saves the result as a JSON file.

    Args:
        pdf_file_path (str): Path to the PDF form file.
        json_schema_path (str): Path to the JSON schema file.
    """
    logging.info('Starting the form data extraction process.')

    # Read the PDF form file
    logging.debug(f'Reading PDF form file from {pdf_file_path}.')
    with open(pdf_file_path, 'rb') as pdf_file:
        pdf_contents = pdf_file.read()

    # Read the JSON schema file
    logging.debug(f'Reading JSON schema file from {json_schema_path}.')
    with open(json_schema_path, 'rb') as schema_file:
        schema_contents = schema_file.read()

    # Send the PDF and schema to the API to extract form data
    logging.debug('Sending PDF form and JSON schema to the API for data extraction.')
    result_id = send_pdf_form(pdf_contents, schema_contents)

    # Retrieve and save the result
    result = read_result(result_id)
    save_JSON_to_file(result, f'results/{result_id}')
    logging.info(f"Form data saved to results/{result_id}")
    logging.info('Form data extraction process completed successfully.')

def send_pdf_form(pdf_contents, schema_contents):
    """
    Sends a PDF form and JSON schema to the API endpoint to extract form data.

    Args:
        pdf_contents (bytes): The binary contents of the PDF form file.
        schema_contents (bytes): The contents of the JSON schema file.

    Returns:
        str: The result_id provided by the API to retrieve the extracted data.
    """
    url = f'{config.BASE_URL}/read_pdf_form'
    files = {
        'pdf_form': ('form.pdf', pdf_contents, 'application/pdf'),
        'json_schema': ('schema.json', schema_contents, 'application/json')
    }

    try:
        logging.debug(f'Sending POST request to {url}.')
        response = requests.post(url, headers=config.get_headers(), files=files)
        response.raise_for_status()
        data = response.json()
        result_id = data['result_id']
        logging.debug(f'Received result_id: {result_id}.')
        return result_id
    except requests.exceptions.RequestException as e:
        logging.error(f'Error sending PDF form and schema to API: {e}')
        exit(1)
