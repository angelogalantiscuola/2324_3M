import os
from flask import Flask, render_template
import json

app = Flask(__name__)

# Get the directory of this Python file
dir_path = os.path.dirname(os.path.realpath(__file__))


@app.route("/")
def hello_world():
    # show a link to the table
    return """
    <a href='/dati_grezzi/'>Vai ai dati grezzi</a>
    <br>
    <a href='/dati_formattati/'>Vai ai dati formattati</a>
    <br>
    <a href='/table/'>Vai alla tabella</a>

    """


@app.route("/dati_grezzi/")
def dati_grezzi():
    # Construct the path to the JSON file
    json_path = os.path.join(dir_path, "esercizio_036.json")
    with open(json_path) as f:
        data = json.load(f)
    return data


@app.route("/dati_formattati/")
def dati_formattati():
    # Construct the path to the JSON file
    json_path = os.path.join(dir_path, "esercizio_036.json")
    with open(json_path) as f:
        data = json.load(f)
    result = ""
    for student in data:
        result += f"{student['name']} ha preso {student['vote']}"
        result += "<br>"
    return result


@app.route("/table/")
def table():
    # Construct the path to the JSON file
    json_path = os.path.join(dir_path, "esercizio_036.json")
    with open(json_path) as f:
        data = json.load(f)
    return render_template("table.html", students=data)


if __name__ == "__main__":
    # app.run() # flask --app main run --debug --port 1234
    app.run(debug=True, port=1234)  # python main.py
