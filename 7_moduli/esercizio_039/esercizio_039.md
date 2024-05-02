# Flashcard Application Exercise

In this exercise, you will create a simple flashcard application using Flask. The application will present the user with a flashcard and a button to reveal the answer.

## Requirements

1. **Flashcard Data:** Store the flashcard data (questions and answers) in a JSON file. Each flashcard should have a unique ID, a question, and an answer.

    Example of flashcard data:

    ```json
    [
        {
            "id": 1,
            "question": "What is the capital of Italy?",
            "answer": "Mondaino"
        },
        ...
    ]
    ```


2. **Flashcard Page (`/flashcard/<id>`):** When the user visits the `/flashcard/<id>` URL, they should see a flashcard with the question. The flashcard should also include a form for the user to submit their answer.

    Example of flashcard.html:

    ```html

    <p>Question: {{ flashcard.question }}</p>
    <form method="POST">
        <label for="answer">Your answer:</label>
        <input type="text" id="answer" name="answer">
        <input type="submit" value="Submit Answer">
    </form>
    {% if message %}
        <p>{{ message }}</p>
    {% endif %}
    ```

3. **Answer Submission:** When the user submits their answer through the form, the application will check if the answer is correct. A message will be displayed on the page indicating whether the answer is correct or not. If the answer is incorrect, the correct answer will also be displayed.

## Bonus

If you finish the main part of the exercise and want an extra challenge, try adding the following features:

- **Random Flashcard:** Add a "Random" button that takes the user to a random flashcard `/flashcard/random`.


## Setup the environment

1. **Create a new repository:**
    - Open your terminal and navigate to the directory where you want to create your new repository or open an existing one.

2. **Create a virtual environment:**
    - Still in the terminal, run `python3 -m venv .venv` to create a new virtual environment in a directory named `.venv`.

3. **Activate the virtual environment:**
    - On Linux, run `source .venv/bin/activate` to activate the virtual environment.

4. **Install required modules:**
    - If you have a `requirements.txt` file, run `pip install -r requirements.txt` to install all required modules.

5. **Add a .gitignore file:**
    - Create a new file named `.gitignore` in your repository.
    - Add `.venv` and any other directories or files you want Git to ignore.


## Top-down approach

Remember, this is a top-down approach. You can start working on each step, test it thoroughly before moving to the next one. This way, you can ensure that each part of your application is working as expected before adding more complexity.

1. **Read and print the JSON data (`read_flashcards`):**
    - Create a JSON file with flashcard data as described in the exercise.
    - Write a Python function `read_flashcards(filename: str) -> None:` to read this JSON file and print the data.

2. **Access individual flashcards (`get_flashcard_by_id`):**
    - Modify the function `read_flashcards` to accept an ID as a parameter, rename it to `get_flashcard_by_id(id: int) -> None:`.
    - The function `get_flashcard_by_id` should print the flashcard with the given ID.

3. **Create a simple CLI interface (`prompt_for_id`):**
    - Write a function `prompt_for_id() -> int:` to prompt the user for an ID.
    - Call the function `get_flashcard_by_id` from step 2 with the user's input.
    - Print the question from the flashcard.

4. **Allow the user to answer a question (`prompt_for_answer` and `check_answer`):**
    - After printing the question, prompt the user for an answer using the function `prompt_for_answer() -> str:`.
    - Write a function `check_answer(user_answer: str, correct_answer: str) -> bool:` to check if the user's answer matches the answer in the flashcard.
    - Call `check_answer` with the user's answer and the correct answer from the flashcard.
    - Print a message indicating whether the user was correct.
        ```python
        def prompt_for_id() -> int:
            ...
            flashcard = get_flashcard_by_id(id)
            ...
            user_answer = prompt_for_answer()
            is_correct = check_answer(user_answer, flashcard['answer'])
            ...
        ```

5. **Convert the CLI interface to a Flask application:**
    - Start by importing the necessary modules and creating a new Flask application instance:
        ```python
        from flask import Flask, render_template, request
        app = Flask(__name__)
        ```
    - Replace the CLI prompts with Flask routes and views. Each route in a Flask application is associated with a Python function. When the route is accessed through a web browser, the associated function is executed.
        - For example, create a route for getting a flashcard by ID:
            ```python
            @app.route('/flashcard/<int:id>')
            def flashcard(id):
                flashcard = get_flashcard_by_id(id)
                return render_template('flashcard.html', flashcard=flashcard)
            ```
    - Create a HTML template file named 'flashcard.html' in a templates folder in your project directory. This file should contain the HTML structure of your flashcard and form, with placeholders for the flashcard data.
        - For example:
            ```html
            <h1>{{ flashcard.question }}</h1>
            <form action="/answer/{{ flashcard.id }}" method="post">
                <input type="text" name="answer">
                <input type="submit" value="Submit">
            </form>
            ```

            > The HTML code provided is a template for displaying a flashcard and a form for submitting an answer. The template uses Flask's Jinja2 templating language.
            > 
            > - `<h1>{{ flashcard.question }}</h1>`: This line displays the question of the flashcard. The `{{ flashcard.question }}` is a placeholder that gets replaced with the actual question when the template is rendered.
            > 
            > - `<form action="/answer/{{ flashcard.id }}" method="post">`: This line starts a form. The `action` attribute specifies where to send the form data when the form is submitted. In this case, the form data is sent to the `/answer/{{ flashcard.id }}` URL. The `{{ flashcard.id }}` is a placeholder that gets replaced with the actual ID of the flashcard when the template is rendered. The `method="post"` attribute specifies that the HTTP POST method should be used when sending the form data.
            > 
            > - `<input type="text" name="answer">`: This line creates a text input field where the user can enter their answer.
            > 
            > - `<input type="submit" value="Submit">`: This line creates a submit button. When the user clicks this button, the form data is sent to the URL specified in the `action` attribute.

6. **Handle form submissions:**
    - Add a route to handle POST requests from the form.
        - For example:
            ```python
            @app.route('/answer/<int:id>', methods=['POST'])
            def answer(id):
                user_answer = request.form.get('answer')
                flashcard = get_flashcard_by_id(id)
                is_correct = check_answer(user_answer, flashcard['answer'])
                return render_template('result.html', is_correct=is_correct)
            ```
    - Create a HTML template file named 'result.html' in the templates folder. This file should display a message based on whether the user's answer was correct.
        - For example:
            ```html
            {% if is_correct %}
                <h1>Correct!</h1>
            {% else %}
                <h1>Incorrect.</h1>
            {% endif %}
            ```

7. **Add a random flashcard feature (`get_random_flashcard`):**
    - Write a function `get_random_flashcard() -> dict:` to get a random flashcard.
    - Add a route for `/flashcard/random` that uses this function.
        - For example:
            ```python
            @app.route('/flashcard/random')
            def random_flashcard():
                flashcard = get_random_flashcard()
                return render_template('flashcard.html', flashcard=flashcard)
            ```
    - You can use the same 'flashcard.html' template for this route.