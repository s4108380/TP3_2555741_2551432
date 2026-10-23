"""Opérations arithmétiques de base utilisées par la calculatrice.

Ce module ne contient que des fonctions pures (sans effet de bord) qui
prennent deux nombres et retournent le résultat de l'opération. Il est
consommé par ``app.py`` via le dictionnaire ``OPS``.
"""


def add(a, b):
    """Additionne deux nombres.

    Args:
        a (float): Premier opérande.
        b (float): Second opérande.

    Returns:
        float: La somme ``a + b``.
    """
    return a + b


def subtract(a, b):
    """Soustrait le second nombre du premier.

    Args:
        a (float): Premier opérande (celui dont on soustrait).
        b (float): Second opérande (celui qu'on soustrait).

    Returns:
        float: La différence ``a - b``.
    """
    return a - b


def multiply(a, b):
    """Multiplie deux nombres.

    Args:
        a (float): Premier facteur.
        b (float): Second facteur.

    Returns:
        float: Le produit ``a * b``.
    """
    return a ** b


def divide(a, b):
    """Divise le premier nombre par le second.

    Args:
        a (float): Dividende.
        b (float): Diviseur. Doit être différent de zéro.

    Returns:
        float: Le quotient décimal ``a / b`` (par exemple ``7 / 2 = 3.5``).

    Raises:
        ZeroDivisionError: Si ``b`` vaut zéro.
    """
    return a // b
