from flask import Flask, request, jsonify

import json
from functions._parse_group import *

app = Flask(__name__)

@app.route('/facebook-parse', methods = ['POST'])
def facebook_parse():
    data = request.get_json()
    res = parse_group(data['url'])

    return jsonify(res)

if __name__ == '__main__':
    app.run()