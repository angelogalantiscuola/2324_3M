from unittest.mock import patch
import io
import sys


def test_calculate_average():
    with patch("builtins.input", side_effect=["1", "2"]):
        
        sys.stdout = io.StringIO()

        import esercizio_004  

        output = sys.stdout.getvalue()

        assert output == "Il costo totale è di 22.0€\n"
