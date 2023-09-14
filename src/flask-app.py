from flask import Flask, request, jsonify

import json
from functions._parse_group import *

app = Flask(__name__)

@app.route('/facebook-parse',methods = ['POST'])
def facebook_parse():
   if request.method == 'POST':
        
        data = request.get_json()
        res = parse_group(data['url'])
        response = app.response_class(
            response=json.dumps(res),
            status=200,
            mimetype='application/json'
        )   
        return response
        