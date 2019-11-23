import json

from flask import Flask
from flask import jsonify
from flask import request

from api.algorithms import *
from api.constants import *

app = Flask(__name__)

app.config['JSON_AS_ASCII'] = False

# Index
@app.route('/', methods=['GET'])
def hello_world():
    return jsonify({'message' : 'Solution for the FinTech Hackathon 11/2019'})

# Get all the moroccan words
@app.route('/output', methods=['GET'])
def returnAll():
    return jsonify({'message' : 'Output solution'})

if __name__ == "__main__":
    app.run(debug=True)