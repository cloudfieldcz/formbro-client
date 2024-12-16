import os
from dotenv import load_dotenv
import logging

# Load environment variables from .env file
load_dotenv()

BASE_URL = os.getenv('BASE_URL', "https://formbroapi-fnezhbdzdfhkejgw.swedencentral-01.azurewebsites.net")
API_KEY = os.getenv('API_KEY')
LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')

READ_MAX_RETRIES = os.getenv('READ_MAX_RETRIES', 30)

def get_logging_level():
    if LOG_LEVEL == 'DEBUG':
        return logging.DEBUG
    elif LOG_LEVEL == 'INFO':
        return logging.INFO
    elif LOG_LEVEL == 'WARNING':
        return logging.WARNING
    elif LOG_LEVEL == 'ERROR':
        return logging.ERROR
    elif LOG_LEVEL == 'CRITICAL':
        return logging.CRITICAL
    else:
        return logging.INFO

def get_headers():
    return {
        'API-Key': API_KEY
    }
