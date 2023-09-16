from flask import Flask, request, jsonify

import sys
import logging
import os

from functions._parse_group import *
from functions._log_writer import LogWriter

app = Flask(__name__)

log_filename = str(os.path.join(os.path.dirname(__file__), 'flask_output.log'))
logging.basicConfig(
    filename=log_filename,
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s]: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S")

# redirect stdout and stderr to the log file
sys.stdout = LogWriter(logging.INFO)
sys.stderr = LogWriter(logging.ERROR)

@app.route('/facebook-parse', methods=['POST'])
def facebook_parse():
    data = request.get_json()
    logging.info(f"Request: {request.get_data()}")

    try:
        res = parse_group(data['url'])
        logging.info(f"Return: {str(res)}")

        return jsonify(res)
    except Exception as e:
        logging.error("An error occurred: %s", str(e))


if __name__ == '__main__':
    app.run()
