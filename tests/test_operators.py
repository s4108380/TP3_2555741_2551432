"""Tests unitaires du module ``operators``.

Chaque test décrit le comportement CORRECT attendu d'une opération. Un test
qui échoue révèle donc un bogue dans ``operators.py``.
"""

import pytest

from operators import add, subtract, multiply, divide


def test_add_deux_entiers():
    """2 + 3 doit donner 5."""
    assert add(2, 3) == 5


def test_add_avec_negatif():
    """-4 + 6 doit donner 2."""
    assert add(-4, 6) == 2


def test_subtract_ordre_des_operandes():
    """10 - 3 doit donner 7 (et non -7 : l'ordre compte)."""
    assert subtract(10, 3) == 7


def test_subtract_resultat_negatif():
    """3 - 10 doit donner -7."""
    assert subtract(3, 10) == -7


def test_multiply_deux_entiers():
    """6 * 7 doit donner 42 (et non 6 puissance 7)."""
    assert multiply(6, 7) == 42


def test_multiply_par_zero():
    """Tout nombre multiplié par 0 donne 0."""
    assert multiply(5, 0) == 0


def test_divide_resultat_exact():
    """12 / 4 doit donner 3."""
    assert divide(12, 4) == 3


def test_divide_resultat_decimal():
    """7 / 2 doit donner 3.5 (division décimale, pas entière)."""
    assert divide(7, 2) == 3.5


def test_divide_par_zero_leve_une_exception():
    """Diviser par 0 doit lever ZeroDivisionError."""
    with pytest.raises(ZeroDivisionError):
        divide(5, 0)
