from flask import Flask, render_template
import json

app = Flask(__name__)


@app.route("/")
def hello_world():
    # show a link to the table
    return "Hello, World! <a href='/table/'>Table</a>"



@app.route("/table/")
def table():
    with open("votes.json") as f:
        data = json.load(f)
    return render_template("table.html", students=data)


if __name__ == "__main__":
    # app.run() # flask --app main run --debug --port 1234
    app.run(debug=True, port=1234)  # python main.py
