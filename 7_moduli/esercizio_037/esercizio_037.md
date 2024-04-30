# Ordered list with links from json

1. Load the JSON file containing the links.
2. Create a Flask app.
3. Define a route that will handle the GET request to display the list of links. (The template should get the links dinamically from the json file.)

Note: Remember to simplify the problem and solve it step by step.

## JSON file

```json
[
    {
        "text": "Google",
        "href": "https://www.google.com"
    },
    {
        "text": "GitHub",
        "href": "https://github.com"
    },
    {
        "text": "Stack Overflow",
        "href": "https://stackoverflow.com"
    }
]
```

## HTML file
The template should get the links dinamically from the json file.

```html
<!DOCTYPE html>
<html>
<head>
    <title>Links Page</title>
</head>
<body>
    <h1>Links</h1>
    <ol>
        <li><a href="https://www.google.com">Google</a></li>
        <li><a href="https://github.com">GitHub</a></li>
        <li><a href="https://stackoverflow.com">Stack Overflow</a></li>
    </ol>
</body>
</html>
```