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
