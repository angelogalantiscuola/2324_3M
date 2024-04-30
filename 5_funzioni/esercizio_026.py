"""
This module contains functions for solving a quadratic equation.

The quadratic equation is in the form ax^2 + bx + c = 0, where:
- a is the coefficient of the term of second degree,
- b is the coefficient of the term of first degree, and
- c is the constant term.

The module provides the following functions:
- entrata(): Prompt the user to enter three numbers and return them as a list.
- elaborazione(a, b, c): Calculate the solutions of a quadratic equation.
- uscita(x1, x2): Print the values of x1 and x2 if they are not None.

"""

from math import sqrt


def entrata() -> list[int]:
    """
    Prompt the user to enter three numbers and return them as a list.

    Returns:
        list[int]: A list containing the three numbers entered by the user.
    """
    a = int(input("Inserisci un numero:"))
    b = int(input("Inserisci un numero:"))
    c = int(input("Inserisci un numero:"))
    return [a, b, c]


def elaborazione(a: int, b: int, c: int) -> list[float] | None:
    """
    Calcola le soluzioni di un'equazione di secondo grado nella forma ax^2 + bx + c = 0.

    Args:
        a (int): Il coefficiente del termine di secondo grado.
        b (int): Il coefficiente del termine di primo grado.
        c (int): Il termine noto.

    Returns:
        list[float] | None: Una lista contenente le soluzioni dell'equazione, se esistono.
                            None se l'equazione è impossibile.

    """
    x1 = 0
    x2 = 0
    delta = b * b - 4 * a * c
    if delta < 0:
        print("Delta è negativa, l'equazione è impossibile")
        x1 = None
        x2 = None
        return x1, x2
    elif delta == 0:
        x1 = -b / (2 * a)
        x2 = x1
        return x1, x2
    elif delta > 0:
        x1 = (-b + sqrt(delta)) / (2 * a)
        x2 = (-b - sqrt(delta)) / (2 * a)
        return [x1, x2]


def uscita(x1: float | None, x2: float | None) -> None:
    """
    Prints the values of x1 and x2 if they are not None.
    If x1 and x2 are equal, only x1 is printed.

    Args:
        x1 (float | None): The first value.
        x2 (float | None): The second value.
    """
    if x1 is not None:
        if x1 == x2:
            print(x1)
        else:
            print(x1)
            print(x2)


a1, b1, c1 = entrata()
sol1, sol2 = elaborazione(a1, b1, c1)
uscita(sol1, sol2)
