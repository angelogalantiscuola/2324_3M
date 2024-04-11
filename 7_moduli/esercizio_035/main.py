from flask import Flask, render_template
import json

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Welcome to our Weather Application!"


@app.route("/cities")
def list_of_cities():
    cities = ["New York", "San Francisco", "Los Angeles", "Chicago"]
    return render_template("list.html", cities=cities)


@app.route("/weather/<city>")
def weather(city):
    return f"Weather for {city}"


@app.route("/weather2/<city>")
def weather2(city):
    with open("weather.json") as f:
        data = json.load(f)
    # check if the city is in the json file
    return f"Weather for {city}: {data[city]['temperature']}"


@app.route("/weather3/<city>")
def weather3(city):
    with open("weather.json") as f:
        data = json.load(f)
    # check if the city is in the json file
    return render_template("weather.html", city=city, weather_info=data[city])


if __name__ == "__main__":
    # app.run() # flask --app main run --debug --port 1234
    app.run(debug=True, port=1234)  # python main.py
