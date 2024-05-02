# Recipe Sharing Application Exercise

Create a simple recipe sharing application using Flask. Store the recipe data (name, ingredients, and instructions) in a JSON file. Each recipe should have a unique ID, a name, a list of ingredients, and instructions.

## Requirements

1. **Recipe Data:** Store the recipe data (name, ingredients, and instructions) in a JSON file. Each recipe should have a unique ID, a name, a list of ingredients, and instructions.

    Example of recipe data:

    ```json
    [
        {
            "id": 1,
            "name": "Spaghetti Carbonara",
            "ingredients": ["Spaghetti", "Eggs", "Pancetta", "Parmesan Cheese"],
            "instructions": "Boil the spaghetti. Fry the pancetta. Mix eggs and cheese. Combine everything."
        },
        ...
    ]
    ```

2. **Recipe Page (`/recipe/<id>`):** When the user visits the `/recipe/<id>` URL, they should see the recipe with its name, ingredients, and instructions.

    Example of static recipe.html:

    ```html
    <h1>Spaghetti Carbonara</h1>
    <h2>Ingredients</h2>
    <ul>
        <li>Spaghetti</li>
        <li>Eggs</li>
        <li>Pancetta</li>
        <li>Parmesan Cheese</li>
    </ul>
    <h2>Instructions</h2>
    <p>Boil the spaghetti. Fry the pancetta. Mix eggs and cheese. Combine everything.</p>
    ```

    > You are required to create a dynamic version of the recipe page using Flask and Jinja2 templates. Instead of hardcoding the recipe details like in the static HTML example provided, you will retrieve the recipe data from a JSON file and use it to populate the HTML template.


3. **Recipe List Page (`/recipes`):** When the user visits the `/recipes` URL, they should see a list of all recipes. Each recipe in the list should be a link to the recipe page for that recipe.

    Example of recipes.html:

    ```html
    <h1>Recipes</h1>
    <ul>
        {% for recipe in recipes %}
            <li><a href="/recipe/{{ recipe.id }}">{{ recipe.name }}</a></li>
        {% endfor %}
    </ul>
    ```

## Top-down approach

1. **Read and print the JSON data (`read_recipes`):**
    - Create a JSON file with recipe data as described in the exercise.
    - Write a Python function `read_recipes(filename: str) -> None:` to read this JSON file and print the data.

2. **Access individual recipes (`get_recipe_by_id`):**
    - Modify the function `read_recipes` to accept an ID as a parameter, rename it to `get_recipe_by_id(id: int) -> None:`.
    - The function `get_recipe_by_id` should print the recipe with the given ID.

3. **Create a simple CLI interface (`prompt_for_id`):**
    - Write a function `prompt_for_id() -> int:` to prompt the user for an ID.
    - Call the function `get_recipe_by_id` from step 2 with the user's input.
    - Print the name, ingredients, and instructions from the recipe.

4. **Convert the CLI interface to a Flask application:**
    - Start by importing the necessary modules and creating a new Flask application instance:
        ```python
        from flask import Flask, render_template
        app = Flask(__name__)
        ```
    - Replace the CLI prompts with Flask routes and views. Each route in a Flask application is associated with a Python function. When the route is accessed through a web browser, the associated function is executed.
        - For example, create a route for getting a recipe by ID:
            ```python
            @app.route('/recipe/<int:id>')
            def recipe(id):
                recipe = get_recipe_by_id(id)
                return render_template('recipe.html', recipe=recipe)
            ```
    - Create a HTML template file named 'recipe.html' in a templates folder in your project directory. This file should contain the HTML structure of your recipe, with placeholders for the recipe data.
        - For example:
            ```html
            <h1>{{ recipe.name }}</h1>
            ...
            ```

5. **Recipe List Page (`/recipes`):**
    - Write a function `get_all_recipes() -> list:` to get a list of all recipes.
    - Add a route for `/recipes` that uses this function.
        - For example:
            ```python
            @app.route('/recipes')
            def recipes():
                ...
            ```
    - Create a HTML template file named 'recipes.html' in a templates folder in your project directory. This file should contain the HTML structure of your recipe list, with placeholders for the recipe data.
        - For example:
            ```html
            <h1>Recipes</h1>
            <ul>
                {% for recipe in recipes %}
                    <li><a href="/recipe/{{ recipe.id }}">{{ recipe.name }}</a></li>
                {% endfor %}
            </ul>
            ```
