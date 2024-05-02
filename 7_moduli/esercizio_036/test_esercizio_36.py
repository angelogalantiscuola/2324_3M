import pytest
from esercizio_036 import app
import json


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_hello_world(client):
    rv = client.get("/")
    assert b"Vai ai dati grezzi" in rv.data
    assert b"Vai ai dati formattati" in rv.data
    assert b"Vai alla tabella" in rv.data


def test_dati_grezzi(client):
    rv = client.get("/dati_grezzi/")
    data = json.loads(rv.data)
    assert isinstance(data, list)
    for item in data:
        assert "name" in item
        assert "vote" in item
        assert isinstance(item["name"], str)
        assert isinstance(item["vote"], int)


def test_dati_formattati(client):
    rv = client.get("/dati_formattati/")
    data = rv.data.decode()  # decode bytes to string
    assert "Alice ha preso 5" in data
    assert "Bob ha preso 3" in data
    assert "Charlie ha preso 4" in data
    assert "Dave ha preso 2" in data


def test_table(client):
    rv = client.get("/table/")
    data = rv.data.decode()  # decode bytes to string

    # Check that the response contains the expected HTML structure
    assert "<table>" in data
    assert "</table>" in data

    # Check that the response contains the expected data
    students = [
        {"name": "Alice", "vote": 5},
        {"name": "Bob", "vote": 3},
        {"name": "Charlie", "vote": 4},
        {"name": "Dave", "vote": 2},
    ]
    for student in students:
        assert f"<td>{student['name']}</td>" in data
        assert f"<td>{student['vote']}</td>" in data
