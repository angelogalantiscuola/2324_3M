import json
from flask import Flask, request, render_template
import random

app = Flask(__name__)


def read_recipes(filename: str) -> list:
    with open(filename, "r", encoding="utf-8") as f:
        recipes = json.load(f)
    return recipes


def get_recipe_by_id(recipes_list, recipe_id) -> dict:
    for recipe in recipes_list:
        if recipe["id"] == recipe_id:
            return recipe
    return {}


def get_user_input():
    recipe_id = int(input("Enter the id of the recipe: "))
    return recipe_id


@app.route("/")
def home():
    return "Funziona?"


@app.route("/recipe/<recipe_id>")
def recipe(recipe_id):
    recipes_list = read_recipes("esercizio_040.json")
    recipe = get_recipe_by_id(recipes_list, int(recipe_id))
    return render_template("recipe.html", recipe=recipe)


@app.route("/recipes")
def recipes():
    recipes_list = read_recipes("esercizio_040.json")
    return render_template("recipes.html", recipes=recipes_list)

    # return render_template("recipe.html", recipe={
    #     "id": 1,
    #     "name": "Spaghetti Carbonara",
    #     "ingredients": [
    #         "Spaghetti",
    #         "Eggs",
    #         "Pancetta",
    #         "Parmesan Cheese"
    #     ],
    #     "instructions": "Boil the spaghetti. Fry the pancetta. Mix eggs and cheese. Combine everything."
    # })


if __name__ == "__main__":
    # recipes_list = read_recipes("esercizio_040.json")

    # # ask user for recipe id
    # recipe_id = get_user_input()

    # recipe = get_recipe_by_id(recipes_list, recipe_id)

    # # print the recipe
    # if recipe:
    #     print(recipe)
    # else:
    #     print(f"No recipe found with id {recipe_id}")

    # # print all recipes as a list
    # for recipe in recipes_list:
    #     print(recipe["name"])

    random_port = random.randint(1024, 49151)
    app.run(debug=True, port=random_port)
