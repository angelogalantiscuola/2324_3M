# from flask import Flask, request, render_template
# import json
# import random

# app = Flask(__name__)

# # Load flashcards from JSON file
# with open("flashcards.json") as f:
#     flashcards = json.load(f)


# @app.route("/print_all_flashcard/", methods=["GET", "POST"])
# def print_all_flashcard():
#     return render_template("all_flashcards.html", flashcards=flashcards)


# @app.route("/print_one_flashcard/<int:id>", methods=["GET", "POST"])
# def print_one_flashcard(id):
#     flashcard = None
#     for f in flashcards:
#         if f["id"] == id:
#             flashcard = f
#             break

#     if flashcard is None:
#         return "Flashcard not found", 404

#     return render_template("all_flashcards.html", flashcard=flashcard)


# @app.route("/flashcard/<int:id>", methods=["GET", "POST"])
# def flashcard(id):
#     flashcard = None
#     message = None
#     return render_template("flashcard.html", flashcard=flashcard, message=message)


# @app.route("/")
# def home():
#     return "Vai alla pagina delle flashcard"


# if __name__ == "__main__":
#     app.run(debug=True, port=7463)

# pylint: disable=redefined-outer-name
# pylint: disable=missing-function-docstring

import json


# Step 1: Read and print the JSON data
def read_flashcards(filename: str) -> None:
    with open(filename, "r", encoding="utf-8") as f:
        flashcards = json.load(f)
    print(flashcards)


# Step 2: Access individual flashcards
def get_flashcard_by_id(flashcard_id: int, filename: str) -> None:
    with open(filename, "r", encoding="utf-8") as f:
        flashcards = json.load(f)
    for flashcard in flashcards:
        if flashcard["id"] == flashcard_id:
            print(flashcard)
            return flashcard
    print(f"No flashcard found with id {flashcard_id}")


# Step 3: Create a simple CLI interface
def prompt_for_id() -> int:
    flashcard_id = int(input("Enter the id of the flashcard: "))
    return flashcard_id

# Step 4: Allow the user to answer a question
def prompt_for_answer() -> str:
    user_answer = input("Enter your answer: ")
    return user_answer

def check_answer(user_answer: str, correct_answer: str) -> bool:
    return user_answer.lower() == correct_answer.lower()

if __name__ == "__main__":
    # Test the functions
    filename = "flashcards.json"  # replace with your json file
    read_flashcards(filename)
    flashcard_id = prompt_for_id()
    flashcard = get_flashcard_by_id(flashcard_id, filename)
    if flashcard:
        user_answer = prompt_for_answer()
        is_correct = check_answer(user_answer, flashcard['answer'])
        if is_correct:
            print("Correct!")
        else:
            print("Incorrect. The correct answer was: " + flashcard['answer'])