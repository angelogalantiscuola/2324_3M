from unittest.mock import patch
import io
import sys


def test_calculate_average():
    # patch the input function to return the values from the side_effect list
    with patch("builtins.input", side_effect=["3", "2", "2", "2"]):

        # Replace sys.stdout with an instance of io.StringIO
        sys.stdout = io.StringIO()

        import esercizio_002

        # Get the output of the print function
        output = sys.stdout.getvalue()
        output = float(output.strip())

        # Check that the output is correct
        assert output == 141.0
