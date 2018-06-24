from flask import Flask, request
from sim import *
import json
import logging

# gunicorn main:app --log-level debug -t 500 -w 1 -b 127.0.0.1:8007

app = Flask(__name__)

LOGGER = logging.getLogger('gunicorn.error')


@app.route('/')
def home():
    return 'Welcome to The Similarity Games'

@app.route('/connections')
def connections():
    word = request.args.get('word')
    connections = similarToWord(word)
    return json.dumps(connections)

@app.route('/tagSimilarity')
def tagSimilarity():
    arr1 = request.args.get('array1')
    arr2 = request.args.get('array2')
    arraySim = getArraySimilarity(arr1, arr2)
    return json.dumps(arraySim)

@app.route('/distance')
def distance():
    word1 = request.args.get('word1')
    word2 = request.args.get('word2')
    distance = getDistinceBetweenEntitys(word1, word2)
    return json.dumps(distance)

@app.route('/mismatch')
def mismatch(array):
    mismatch = oddOneOut(array)
    return json.dumps(mismatch)

@app.errorhandler(500)
def server_error(e):
    # Log the error and stacktrace.
    logging.exception('An error occurred during a request.')
    return 'An internal error occurred.', 500

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)