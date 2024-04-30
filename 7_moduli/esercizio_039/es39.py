from flask import Flask, request, render_template
import json
import random

app = Flask(__name__)

# Load flashcards from JSON file
with open("flashcards.json") as f:
    flashcards = json.load(f)


@app.route("/print_all_flashcard/", methods=["GET", "POST"])
def print_all_flashcard():
    return render_template("all_flashcards.html", flashcards=flashcards)


@app.route("/print_one_flashcard/<int:id>", methods=["GET", "POST"])
def print_one_flashcard(id):
    flashcard = None
    for f in flashcards:
        if f["id"] == id:
            flashcard = f
            break

    if flashcard is None:
        return "Flashcard not found", 404

    return render_template("all_flashcards.html", flashcard=flashcard)


@app.route("/flashcard/<int:id>", methods=["GET", "POST"])
def flashcard(id):
    flashcard = None
    message = None
    return render_template("flashcard.html", flashcard=flashcard, message=message)


@app.route("/")
def home():
    return "Vai alla pagina delle flashcard"


if __name__ == "__main__":
    app.run(debug=True, port=7463)
