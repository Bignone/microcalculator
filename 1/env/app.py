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
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

logging.basicConfig(format='%(asctime)s [%(levelname)s] %(message)s', level=logging.INFO)


global model, tokenizer, encoder, text_labels

with open(MODEL) as handle:
    model = model_from_json(handle.read())
    logging.info('Loaded model from {}'.format(MODEL))
    # load weights into new model
    model.load_weights(WEIGHTS)
    logging.info('Loaded weights from {}'.format(WEIGHTS))

with open(TOKENIZER, 'rb') as handle:
    tokenizer = pickle.load(handle)
    logging.info('Loaded tokenizer from {}'.format(TOKENIZER))

with open(ENCODER, 'rb') as handle:
    encoder = pickle.load(handle)
    text_labels = encoder.classes_
    logging.info('Loaded encoder from {}'.format(ENCODER))

# keras inference has problems with flask
graph = tf.get_default_graph()


@app.route('/api/v1/documents/classify', methods=['GET'])
def get_status():
    return jsonify(dict(success=True))


@app.route('/api/v1/documents/classify', methods=['POST'])
def classify():
    '''Processes the input txt document and returns the predicted classes and their probabilities'''
    doc = request.get_json(force=True)
    doc_id = doc['doc_id']
    text = doc['rawtext']
    X = tokenizer.texts_to_matrix([text], mode='tfidf')

    # keras models' inference breaks when multi-threads in Flask
    # check this: https://github.com/keras-team/keras/issues/2397#issuecomment-254919212
    global graph
    with graph.as_default():
        prediction = model.predict(np.array(X))

    top_indices = prediction[0].argsort()[-3:]
    top_predictions = [dict(category=text_labels[i], probability=float(prediction[0][i])) for i in top_indices]
    top_predictions.sort(key=lambda x: x['probability'], reverse=True)
    return jsonify(dict(doc_id=doc_id, predictions=top_predictions))


@app.route('/api/v1/documents/categories', methods=['POST'])
def get_categories():
    '''Returns a list of the categories recognized by the classifier'''
    categories = list(text_labels)
    return jsonify(dict(categories=list(text_labels)))


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
