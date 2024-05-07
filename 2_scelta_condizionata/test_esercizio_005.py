from unittest.mock import patch
import io
import sys
import esercizio_005  # Import the module at the top of the file


def test_age_group():
    test_cases = [("12", "Child\n"), ("13", "Teenager\n"), ("20", "Adult\n"), ("65", "Senior\n")]

    for input_age, expected_output in test_cases:
        with patch("builtins.input", return_value=input_age), patch("sys.stdout", new=io.StringIO()) as fake_out:
            esercizio_005.main()  # Call the main function directly
            assert fake_out.getvalue() == expected_output
