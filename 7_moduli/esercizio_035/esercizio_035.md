# Exercise: Building a Simple Weather Application with Flask

## Step 1: Basic Setup

Set up a new Flask project. Create a new Python file and import the necessary modules (Flask, render_template, and json). Initialize a new Flask web server. Create a basic route for the homepage ("/") that returns "Welcome to our Weather Application!".

## Step 2: Using Templates

Create a new directory in your project called "templates". Inside this directory, create an HTML file `list.html` for the list of cities. This file should include a welcome message and a list of cities. Create a basic route "/cities" that returns the list of cities in HTML.

## Step 3: Dynamic Routing

Add a new route that takes a city name as a parameter. This route should return a message with the city name. For example, if the route is "/weather/Paris", the page should display "Weather for Paris".

## Step 4: Reading Data from JSON

Create a JSON file in your project directory that contains weather data for a few cities. The data should include the city name and some weather information (like temperature and humidity). Update the dynamic route to read the weather data from this JSON file and display it on the page.
For example: `f"Weather for {city}: {temperature}"`

First, create a new file in your project directory and name it `weather.json`. This file will store the weather data for each city. The data for each city will include the city name, temperature, and humidity.

```json
{
    "Paris": {
        "temperature": "15C",
        "humidity": "70%"
    },
    "London": {
        "temperature": "17C",
        "humidity": "65%"
    },
    "New York": {
        "temperature": "20C",
        "humidity": "60%"
    }
}
```

## Step 5: Displaying Weather Details

Create a new template for the city weather page `weather.html`. This template should display the city name and its weather information. Update the dynamic route to render this template, passing the weather data as a parameter.

```html
<h1>Weather for {{ city }}</h1>
<p>Temperature: {{ weather_info.temperature }}</p>
<p>Humidity: {{ weather_info.humidity }}</p>
```

## Step 6: Fetching Real Weather Data from an API

This is very difficult!

In this step, you'll modify your Flask application to fetch real weather data from the Open-Meteo API.

[See here for details](https://open-meteo.com/en/docs)
