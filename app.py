from flask import Flask, send_file, request
from Maths2SVG.main import circularGraph
import math

app = Flask(__name__)

@app.route("/")
def index():
    return send_file('web/index.html')

@app.route("/image")
def return_image():
    circularGraph()
    return send_file('Maths2SVG/results/graph.svg')

@app.route("/style.css")
def return_style():
    return send_file('web/style.css')

@app.route("/script.js")
def return_js():
    return send_file('web/script.js')

if __name__ == '__main__':
    app.run(debug=False, threaded=False)