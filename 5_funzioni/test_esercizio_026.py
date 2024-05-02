from unittest.mock import patch
from esercizio_026 import elaborazione, uscita, entrata


@patch("builtins.input", side_effect=[1, 2, 3])
def test_entrata(mock_input):
    a, b, c = entrata()
    assert a == 1, f"Expected 1, but got {a}"
    assert b == 2, f"Expected 2, but got {b}"
    assert c == 3, f"Expected 3, but got {c}"


def test_elaborazione():
    # Test case where delta is negative
    a, b, c = 1, 1, 1
    result = elaborazione(a, b, c)
    assert result == (None, None), f"Expected (None, None), but got {result}"

    # Test case where delta is zero
    a, b, c = 1, -2, 1
    result = elaborazione(a, b, c)
    assert result == (1.0, 1.0), f"Expected (1.0, 1.0), but got {result}"

    # Test case where delta is positive
    a, b, c = 1, -3, 2
    result = elaborazione(a, b, c)
    assert result == (2.0, 1.0), f"Expected (2.0, 1.0), but got {result}"


# As uscita() function only prints the result, it's a bit tricky to test it directly.
# However, you can test it indirectly by checking the stdout.
def test_uscita(capsys):
    # Test case where x1 and x2 are None
    uscita(None, None)
    captured = capsys.readouterr()
    assert captured.out == "", "Expected no output, but got some"

    # Test case where x1 and x2 are equal
    uscita(1.0, 1.0)
    captured = capsys.readouterr()
    assert captured.out == "1.0\n", f"Expected '1.0\\n', but got {captured.out}"

    # Test case where x1 and x2 are different
    uscita(2.0, 1.0)
    captured = capsys.readouterr()
    assert captured.out == "2.0\n1.0\n", f"Expected '2.0\\n1.0\\n', but got {captured.out}"
