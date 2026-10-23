"""Tests d'intégration de la route ``/`` avec le client de test Flask."""

import pytest

from app import app


@pytest.fixture
def client():
    """Fournit un client HTTP de test (aucun serveur réel n'est lancé)."""
    app.config["TESTING"] = True
    with app.test_client() as test_client:
        yield test_client


def test_get_retourne_la_page(client):
    """GET / répond 200."""
    assert client.get("/").status_code == 200


def test_post_addition_affiche_le_resultat(client):
    """POST 123+456 affiche 579 dans la page."""
    response = client.post("/", data={"display": "123+456"})
    assert response.status_code == 200
    assert "579" in response.get_data(as_text=True)


def test_post_multiplication_affiche_le_produit(client):
    """POST 13*17 affiche 221 (et non 13 puissance 17)."""
    response = client.post("/", data={"display": "13*17"})
    assert "221" in response.get_data(as_text=True)


def test_post_expression_invalide_affiche_une_erreur(client):
    """Une expression invalide produit un message « Error »."""
    response = client.post("/", data={"display": "abc"})
    assert response.status_code == 200
    assert "Error" in response.get_data(as_text=True)


def test_post_sans_champ_display_affiche_une_erreur(client):
    """Un POST sans champ « display » ne fait pas planter le serveur."""
    response = client.post("/", data={})
    assert response.status_code == 200
    assert "Error" in response.get_data(as_text=True)
