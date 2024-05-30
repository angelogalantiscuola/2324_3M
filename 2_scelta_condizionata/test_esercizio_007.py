from unittest.mock import patch
import io
import sys
import esercizio_007  # Import the module at the top of the file


def test_age_group():
    test_cases = [("11","2","2","il numero maggiore è 11\n"), ("2","12","2","il numero maggiore è 12\n"), ("2","2","13","il numero maggiore è 13\n")]

    for n1, n2, n3, expected_output in test_cases:
        with patch("builtins.input", side_effect=[n1,n2,n3]), patch("sys.stdout", new=io.StringIO()) as fake_out:
            esercizio_007.main()
            assert fake_out.getvalue() == expected_output
