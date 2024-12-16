import os
import requests
import logging
import config

logging.basicConfig(level=config.get_logging_level(), format='%(asctime)s - %(levelname)s - %(message)s')

def ping_api():
    url = f"{config.BASE_URL}/ping"
    logging.info(f"Sending GET request to {url}")
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        logging.error(f"Error sending GET request to {url}: {e}")
        return None

# Call the function and print the result
if __name__ == "__main__":
    result = ping_api()
    print(result)
