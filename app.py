from flask import Flask, send_file, url_for
# from Maths2SVG import main

app = Flask(__name__)
# main.circularGraph()
@app.route("/")
def index():
    return send_file('web/index.html')

@app.route("/image")
def return_image():
    return send_file('doc/graph.png')

@app.route("/style.css")
def return_style():
    return send_file('web/style.css')

@app.route("/script.js")
def return_js():
    return send_file('web/script.js')