from flask import Flask, request, jsonify
from flask_cors import CORS

from .scrape import scrape
from .preprocess import main

app = Flask(__name__)
CORS(app)

# Default Route
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

# Scrape Route
@app.route("/scrape", methods=['GET'])
def scrapeRoute():
    request_data = request.get_json(force=True)
    url = request_data['url']
    res = jsonify(scrape(url))
    res.headers.add('Access-Control-Allow-Origin', '*')
    return res, 200

# Preprocess Route
@app.route('/preprocess', methods=['GET'])
def preprocessRoute():
    request_data = request.get_json(force=True)
    text = request_data['text']
    res = jsonify(main(text))
    res.headers.add('Access-Control-Allow-Origin', '*')
    return res, 200
