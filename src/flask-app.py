from flask import Flask, request, jsonify

from logging.config import dictConfig

from functions._parse_group import *

dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://sys.stdout',
        'formatter': 'default'
    }},
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi']
    }
})

app = Flask(__name__)


@app.route('/facebook-parse', methods=['POST'])
def facebook_parse():
    data = request.get_json()
    app.logger.info(f"Request: {request.get_data()}")

    try:
        res = parse_group(data['url'])
        app.logger.info(f"Return: {str(res)}")

        return jsonify(res)
    except Exception as e:
        app.logger.error("An error occurred: %s", str(e))


if __name__ == '__main__':
    app.run()
