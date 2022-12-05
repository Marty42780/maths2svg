from flask import Flask, send_file, request
from Maths2SVG.main import circularGraph, CGdefaults
import ast

app = Flask(__name__)


@app.route("/")
def index():
    return send_file("web/index.html")


@app.route("/image")
def return_image():
    # TODO: Find a way to get parameters
    circularGraph(
        fileType=request.args.get("fileType")
        if not request.args.get("fileType") == None
        else CGdefaults["fileType"],
        graphInputs=ast.literal_eval(request.args.get("graphInputs"))
        if not request.args.get("graphInputs") == None
        else {
            "Error": ["Error"],
            "Give": ["me"],
            "me": ["some"],
            "some": ["points"],
            "points": [],
        },
        label=True
        if request.args.get("label") == "True"
        else False
        if not request.args.get("label") == None
        else CGdefaults["label"],
        labelCapitalize=True
        if request.args.get("labelCapitalize") == "True"
        else False
        if not request.args.get("labelCapitalize") == None
        else CGdefaults["labelCapitalize"],
        oriented=True
        if request.args.get("oriented") == "True"
        else False
        if not request.args.get("oriented") == None
        else CGdefaults["oriented"],
        allowLoops=True
        if request.args.get("allowLoops") == "True"
        else False
        if not request.args.get("allowLoops") == None
        else CGdefaults["allowLoops"],
        mainColor=request.args.get("mainColor")
        if not request.args.get("mainColor") == None
        else CGdefaults["mainColor"],
        bgColor=request.args.get("bgColor")
        if not request.args.get("bgColor") == None
        else CGdefaults["bgColor"],
    )
    return send_file(
        "Maths2SVG/results/graph."
        + (
            request.args.get("fileType")
            if not request.args.get("fileType") == None
            else CGdefaults["fileType"]
        )
    )


# TODO: Make no args work too


@app.route("/style.css")
def return_style():
    return send_file("web/style.css")


@app.route("/script.js")
def return_js():
    return send_file("web/script.js")


if __name__ == "__main__":
    app.run(debug=False, threaded=False)

""" Favicon : circularGraph(
        fileType='svg',
        allowLoops=False,
        label=False,
        globalOpacity=1,
        oriented=True,
        bgColor='transparent',
        pointColor='transparent',
        mainColor='random',
        graphInputs={
        "aa":["ab"],
        "ab":["ac"],
        "ac":["ad"],
        "ad":["aa"]  
"""
