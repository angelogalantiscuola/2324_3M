"""
This is a test file for the esercizio_040.py file. It uses pytest, a testing framework for 
Python that allows you to easily create small, simple tests, yet scales to support complex 
functional testing for applications and libraries.

Pytest is useful because it helps you make sure your code is working as expected.
To run these tests, you need to have pytest installed. You can install it with pip:

    pip install pytest

Then, you can run the tests with the following command:

    pytest test_esercizio_040.py

Important: Make sure you are in the same directory as the test_esercizio_040.py file when
running the command.

This will run all the tests in the test_esercizio_040.py file and print the results to the 
console. If all the tests pass, it means your code is working as expected. If any test fails, 
pytest will provide a detailed error message that can help you debug the problem.
"""

import pytest
from unittest.mock import patch
from flask import url_for
from esercizio_040 import read_recipes, get_recipe_by_id, get_user_input


# Test for Step 1
@pytest.mark.skip(reason="No way to currently run this test")
def test_read_recipes():
    recipes = read_recipes("recipes.json")
    assert isinstance(recipes, list)
    assert len(recipes) > 0
    assert all(
        "id" in recipe and "name" in recipe and "ingredients" in recipe and "instructions" in recipe
        for recipe in recipes
    )


# Test for Step 2
@pytest.mark.skip(reason="No way to currently run this test")
def test_get_recipe_by_id():
    recipe = get_recipe_by_id(1)
    assert recipe["id"] == 1
    assert recipe["name"] == "Spaghetti Carbonara"
    assert recipe["ingredients"] == ["Spaghetti", "Eggs", "Pancetta", "Parmesan Cheese"]
    assert recipe["instructions"] == "Boil the spaghetti. Fry the pancetta. Mix eggs and cheese. Combine everything."


# Test for Step 3
@pytest.mark.skip(reason="No way to currently run this test")
@patch("builtins.input", return_value="1")
def test_user_input(mock_input):
    recipe_id = get_user_input()
    assert recipe_id == 1
    mock_input.assert_called_once()


# Test for Step 4
@pytest.mark.skip(reason="No way to currently run this test")
def test_recipe_page(client):
    rv = client.get(url_for("recipe", id=1))
    assert rv.status_code == 200
    data = rv.data.decode()

    # Check that the response contains the expected HTML structure
    assert "<h1>Spaghetti Carbonara</h1>" in data
    assert "<h2>Ingredients</h2>" in data
    assert "<ul>" in data
    assert "<li>Spaghetti</li>" in data
    assert "<li>Eggs</li>" in data
    assert "<li>Pancetta</li>" in data
    assert "<li>Parmesan Cheese</li>" in data
    assert "</ul>" in data
    assert "<h2>Instructions</h2>" in data
    assert "<p>Boil the spaghetti. Fry the pancetta. Mix eggs and cheese. Combine everything.</p>" in data


# Test for Step 5
@pytest.mark.skip(reason="No way to currently run this test")
def test_recipes_page(client):
    rv = client.get(url_for("recipes"))
    assert rv.status_code == 200
    data = rv.data.decode()

    # Check that the response contains the expected HTML structure
    assert "<h1>Recipes</h1>" in data
    assert "<ul>" in data

    # Check that the response contains the expected data
    recipes = [
        {"id": 1, "name": "Spaghetti Carbonara"},
        # Add more recipes here as needed
    ]
    for recipe in recipes:
        assert f'<li><a href="/recipe/{recipe["id"]}">{recipe["name"]}</a></li>' in data

    assert "</ul>" in data
