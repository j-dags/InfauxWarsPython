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
    url = request.args.get('url')
    res = jsonify(scrape(url))
    return res

# Preprocess Route
@app.route('/preprocess', methods=['GET'])
def preprocessRoute():
    text = request.args.get('text')
    res = jsonify(main(text))
    return res, 200
