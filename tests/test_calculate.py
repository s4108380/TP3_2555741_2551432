"""Tests de la fonction ``app.calculate`` (analyse et évaluation).

Les tests sont regroupés en trois familles : cas valides, nombres négatifs,
cas invalides (qui doivent lever ``ValueError``) et cas limites.
"""

import pytest

from app import calculate


# --------------------------------------------------------------------------
# Cas valides
# --------------------------------------------------------------------------

def test_addition_simple():
    """2+3 doit donner 5."""
    assert calculate("2+3") == 5


def test_espaces_ignores():
    """Les espaces autour de l'opérateur n'ont pas d'influence."""
    assert calculate(" 2 + 3 ") == 5


def test_operandes_decimaux():
    """2.5+1.5 doit donner 4."""
    assert calculate("2.5+1.5") == 4


def test_soustraction():
    """10-3 doit donner 7."""
    assert calculate("10-3") == 7


def test_multiplication():
    """6*7 doit donner 42."""
    assert calculate("6*7") == 42


def test_division_decimale():
    """7/2 doit donner 3.5."""
    assert calculate("7/2") == 3.5


# --------------------------------------------------------------------------
# Nombres négatifs
# --------------------------------------------------------------------------

def test_premier_operande_negatif():
    """-5+3 doit donner -2."""
    assert calculate("-5+3") == -2


def test_second_operande_negatif():
    """5*-3 doit donner -15."""
    assert calculate("5*-3") == -15


def test_soustraction_d_un_negatif():
    """5--3 doit donner 8."""
    assert calculate("5--3") == 8


# --------------------------------------------------------------------------
# Cas invalides : doivent lever ValueError
# --------------------------------------------------------------------------

@pytest.mark.parametrize("expr", ["", None, 42])
def test_expression_vide_ou_non_texte(expr):
    """Une expression vide ou qui n'est pas une chaîne est refusée."""
    with pytest.raises(ValueError):
        calculate(expr)


def test_deux_operateurs_distincts_refuses():
    """Trois opérandes (deux opérateurs) ne sont pas supportés."""
    with pytest.raises(ValueError):
        calculate("1+2*3")


@pytest.mark.parametrize("expr", ["5+", "*5", "12"])
def test_operande_ou_operateur_manquant(expr):
    """Opérateur absent, au début ou à la fin : format invalide."""
    with pytest.raises(ValueError):
        calculate(expr)


def test_operande_non_numerique():
    """abc+1 : l'opérande de gauche n'est pas un nombre."""
    with pytest.raises(ValueError):
        calculate("abc+1")


# --------------------------------------------------------------------------
# Cas limites
# --------------------------------------------------------------------------

def test_division_par_zero_leve_value_error():
    """5/0 doit être signalé comme ValueError, comme les autres erreurs
    de saisie, afin d'afficher un message cohérent dans l'interface."""
    with pytest.raises(ValueError):
        calculate("5/0")


@pytest.mark.parametrize("expr", ["inf+1", "nan*2"])
def test_inf_et_nan_refuses(expr):
    """Les valeurs spéciales inf et nan ne sont pas de vrais nombres."""
    with pytest.raises(ValueError):
        calculate(expr)
