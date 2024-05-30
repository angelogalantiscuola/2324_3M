from unittest.mock import patch
import io
import sys


#!non funziona
def test_age_group():
    
    with patch("builtins.input", return_value="9467280000"):
        import esercizio_009
        sys.stdout = io.StringIO()
        
        output = sys.stdout.getvalue()
        assert output[0] == "300\n"
        assert output[1] == "2\n"
        assert output[2] == "15\n"
        assert output[3] == "0\n"
        assert output[4] == "0\n"
        assert output[5] == "0\n"
            
        
