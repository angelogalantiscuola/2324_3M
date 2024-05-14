from unittest.mock import patch
import io
import sys


def test_circle_calculations():
    # patch the input function to return the values from the side_effect list
    with patch("builtins.input", return_value="5.0"):

        # Replace sys.stdout with an instance of io.StringIO
        sys.stdout = io.StringIO()

        import esercizio_003

        # Get the output of the print function
        output = sys.stdout.getvalue().strip().split("\n")

        # Check that the output is correct
        assert output[0] == "Circumference: 31.40"
        assert output[1] == "Area: 78.50"
