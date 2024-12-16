import argparse
import logging
import sys

import config
from ping import ping_api
from read_form import read_form
from read_result import read_result
from read_schema import read_schema
from save import save_JSON_to_file

# Configure logging
logging.basicConfig(level=config.get_logging_level(), format='%(asctime)s - %(levelname)s - %(message)s')

def check_file_extension(file_path, extension):
    if not file_path.lower().endswith(extension):
        logging.error(f"The file must be a {extension} file.")
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description='Process commands.')
    parser.add_argument('command', nargs='?', help='Command to execute')
    parser.add_argument('arguments', nargs='*', help='Arguments for the command')
    args = parser.parse_args()

    if not args.command:
        print("Usage: main.py <command> [options]")
        print("Commands:")
        print("  ping")
        print("  read_schema <pdf_path>")
        print("  read_form <pdf_path> <json_schema>")
        print("  read_result <result_id>")
        sys.exit(1)

    command = args.command

    if command == 'ping':
        result = ping_api()
        logging.info(result)
    elif command == 'read_schema':
        if len(args.arguments) < 1:
            print("Usage: main.py read_schema <pdf_path>")
        else:
            pdf_path = args.arguments[0]
            check_file_extension(pdf_path, '.pdf')
            read_schema(pdf_path)
    elif command == 'read_form':
        if len(args.arguments) < 2:
            print("Usage: main.py read_form <pdf_path> <json_schema>")
        else:
            pdf_path = args.arguments[0]
            json_schema = args.arguments[1]
            check_file_extension(pdf_path, '.pdf')
            check_file_extension(json_schema, '.json')
            read_form(pdf_path, json_schema)
    elif command == 'read_result':
        if len(args.arguments) < 1:
            print("Usage: main.py read_result <result_id>")
        else:
            result_id = args.arguments[0]
            result = read_result(result_id)
            save_JSON_to_file(result, f'results/{result_id}.json')
            logging.info(f"Result saved to results/{result_id}.json")
    else:
        logging.error(f"Unknown command: {command}")
        print("Commands:")
        print("  ping")
        print("  read_schema <pdf_path>")
        print("  read_form <pdf_path> <json_schema>")
        print("  read_result <result_id>")
        sys.exit(1)

if __name__ == '__main__':
    main()