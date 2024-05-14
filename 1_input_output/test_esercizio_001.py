from unittest.mock import patch
import io
import sys


def test_calculate_average():
    with patch("builtins.input", side_effect=["Giovanni", "8", "9", "7"]):
        # This will replace 'input' with a mock function that returns 'Giovanni' the first time it's called,
        # '8' the second time, '9' the third time, and '7' the fourth time.

        # Replace sys.stdout with an instance of io.StringIO
        sys.stdout = io.StringIO()

        import esercizio_001  # Import the module here

        # Get the output of the print function
        output = sys.stdout.getvalue()

        # Check that the output is correct
        assert output == "La media dei voti di Giovanni è 8.0\n"
