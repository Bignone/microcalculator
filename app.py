# -*- coding: utf-8 -*-
# ##############################################################################
# Version: 0.0.1 (2019-01-13)
# Author: Eduardo Bustos (ebustos@minsait.com), minsait

'''
Simple flask-based API to automatically calculate math expressions.
'''

import os
import sys
import logging
from flask import Flask, request, jsonify
from flask import Response
from flask_restful import Api, Resource
from microcalculator.MicroCalculator import MicroCalculator

# Model information

app = Flask(__name__)
api = Api(app)

logging.basicConfig(format='%(asctime)s [%(levelname)s] %(message)s', level=logging.INFO)

NAME = "MicroCalculator"
VERSION = 1
BASE_ROOT = "/{}/api/v{}".format(NAME, VERSION)

# Load model
global model # simple class to evaluate math expressions
model = MicroCalculator() # or load from file system
model.version = VERSION

print("Model: {}".format(model.__class__.__name__))
print("Version: {}".format(VERSION))

@app.route(BASE_ROOT + '/health', methods=['GET'])
def health_check():
    return Response("UP", status = 200)

@app.route(BASE_ROOT + '/information', methods=['GET'])
def get_version():
    return jsonify(model.getBasicInfo())

@app.route(BASE_ROOT + '/calculate', methods=['GET'])
def get_status():
    return jsonify(dict(success=True))

@app.route(BASE_ROOT + '/calculate', methods=['POST'])
def calculate():
    '''Processes the input txt document and returns the predicted classes and their probabilities'''
    body = request.get_json(force=True)
    expression = body['expression']

    result = model.calculate(expression)

    return jsonify(dict(expression=expression, result=result))

@app.route(BASE_ROOT + "/sumatory", methods = ["POST"])
def sumatory():
    body = request.get_json(force=True)
    values = body["values"]
    
    result = model.sumatory(values)

    return jsonify(dict(operation="sumatory", result=result))

@app.route(BASE_ROOT + "/multiply", methods = ["POST"])
def multiply():
    body = request.get_json(force=True)
    values = body["values"]
    
    result = model.multiply(values)

    return jsonify(dict(operation="multiply", result=result))


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
