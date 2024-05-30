from unittest.mock import patch
import io
import sys
import esercizio_006  # Import the module at the top of the file


def test_age_group():
    test_cases = [("2","2","Entrambi i numeri sono pari\n"), ("1","3", "Tutti i numeri sono dispari\n"), ("2","1", "Un numero è pari e l'altro è dispari\n")]

    for n1, n2, expected_output in test_cases:
        with patch("builtins.input", side_effect=[n1,n2]), patch("sys.stdout", new=io.StringIO()) as fake_out:
            esercizio_006.main()
            assert fake_out.getvalue() == expected_output
