# Formbro Client

This is a client app for the Formbro API. The Formbro API allows you to process PDF files and JSON schemas to extract and manage form data.

## API Overview

The Formbro API provides endpoints to:

- **Ping the API**: Check if the API is reachable.
- **Read Schema from PDF**: Generate a JSON schema from a PDF file.
- **Read Form Data from PDF**: Extract form data from a PDF file using a JSON schema.
- **Retrieve Result by ID**: Retrieve previously generated results using a result ID.

For detailed API documentation, visit [Formbro API Docs](https://formbroapi-fnezhbdzdfhkejgw.swedencentral-01.azurewebsites.net/docs).

## Prerequisites

- Python 3.9 or higher
- `pip` (Python package installer)

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/formbro-client.git
    cd formbro-client
    ```

2. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Configuration

1. Copy the `.env.example` file to `.env`:
    ```sh
    cp .env.example .env
    ```

2. Edit the `.env` file to include your API key and other configuration settings:
    ```env
    BASE_URL=https://formbroapi-fnezhbdzdfhkejgw.swedencentral-01.azurewebsites.net # optional
    API_KEY=your_api_key
    LOG_LEVEL=INFO # optional
    ```

To obtain an API key or for any other questions, please contact us at [formbro@cloudfield.cz](mailto:formbro@cloudfield.cz).

## Usage

To use the client, run the `main.py` script with the appropriate command and arguments.

### Commands

- `ping`: Pings the API to check if it is reachable.
- `read_schema <pdf_path>`: Reads a PDF file and generates a schema, saving the result as a JSON file.
- `read_form <pdf_path> <json_schema>`: Reads data from a PDF form using a JSON schema and saves the result as a JSON file.
- `read_result <result_id>`: Retrieves a previously generated result from the API using a result ID and saves it as a JSON file.

### Examples

1. **Ping the API**:
    ```sh
    python main.py ping
    ```

2. **Read Schema from PDF**:
    ```sh
    python main.py read_schema sample_data/invoice_1912.pdf
    ```

3. **Read Form Data from PDF using JSON Schema**:
    ```sh
    python main.py read_form sample_data/invoice_1912.pdf sample_data/schema_invoice.json
    ```

4. **Retrieve Result by ID**:
    ```sh
    python main.py read_result your_result_id
    ```

The invoice used in the examples comes from [invoice_1912.pdf](https://www.urotta.cz/historie-faktury-snizek-obchodnik/).

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

This project is licensed under the MIT License.