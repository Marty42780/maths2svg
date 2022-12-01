from flask import Flask, send_file, request
from Maths2SVG.main import circularGraph
import math
import ast

app = Flask(__name__)


@app.route("/")
def index():
    return send_file("web/index.html")


@app.route("/image")
def return_image():
    circularGraph(
        fileType=request.args.get("fileType"),
        graphInputs=ast.literal_eval(request.args.get("graphInputs")),
        label = True if request.args.get("label") in ['True', 'pourquoi pas', 'avec plaisir'] else False,
        labelCapitalize= True if request.args.get("labelCapitalize") in ['True', 'Si le coeur vous en dis', 'allez lets go', 'Tout le plaisir est pour moi'] else False,
        oriented = True if request.args.get("oriented") in ['True', 'pourquoi pas', 'avec plaisir'] else False,
        allowLoops = True if request.args.get("allowLoops") in ['True', 'Si le coeur vous en dis', 'allez lets go', 'Tout le plaisir est pour moi'] else False,
        mainColor = request.args.get("mainColor"),
        bgColor = request.args.get("bgColor")
    )
    return send_file("Maths2SVG/results/graph." + request.args.get("fileType"))


@app.route("/style.css")
def return_style():
    return send_file("web/style.css")


@app.route("/script.js")
def return_js():
    return send_file("web/script.js")


if __name__ == "__main__":
    app.run(debug=False, threaded=False)

''' Favicon : circularGraph(
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
'''        

