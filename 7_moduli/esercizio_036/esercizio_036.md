# Table with student votes from a JSON file

1. Load the JSON file containing the student votes.
2. Create a Flask app.
3. Define a route that will handle the GET request to display the table.
4. In the route function, render a template that will display the student votes in a table. (The template should get the votes dinamically from the json file.)

```html
<table>
    <tr>
        <th>Student</th>
        <th>Vote</th>
    </tr>
    <tr>
        <td>Alice</td>
        <td>5</td>
    </tr>
    ...
</table>
```

```json
[
    {
        "student": "Alice",
        "vote": 5
    },
    {
        "student": "Bob",
        "vote": 3
    },
    {
        "student": "Charlie",
        "vote": 4
    },
    {
        "student": "Dave",
        "vote": 2
    }
]
```
