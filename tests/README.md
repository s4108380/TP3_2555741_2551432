# `tests/` — suite de tests automatisés

## Raison d'être

Vérifier que la calculatrice se comporte comme prévu et détecter les
régressions lors des corrections de bogues. Chaque test décrit le
comportement **correct** attendu : un test qui échoue révèle un bogue.

## Exécution

Depuis la racine du projet, environnement virtuel activé :

```bash
pip install -r requirements.txt
pytest -v
```

`pytest.ini` ajoute la racine au chemin Python, donc aucune configuration
supplémentaire n'est nécessaire.

## Contenu

| Fichier             | Cible                         | Ce qui est couvert |
|---------------------|-------------------------------|--------------------|
| `test_operators.py` | `operators.py`                | Les 4 opérations : cas simples, résultat négatif, division décimale, division par zéro. |
| `test_calculate.py` | `calculate()` dans `app.py`   | Expressions valides, espaces, décimaux, nombres négatifs, entrées invalides, division par zéro, `inf`/`nan`. |
| `test_routes.py`    | Route `/` (client Flask)      | `GET`, `POST` valide, `POST` invalide, champ `display` absent. |

## Convention d'erreur

Toute erreur de saisie doit lever `ValueError` dans `calculate()`, y compris
la division par zéro, pour que l'interface affiche un message uniforme
(`Error: ...`). Au niveau de `operators.divide`, la division par zéro lève
`ZeroDivisionError`.

## Résultats sur le code initial (avant corrections)

**15 tests échouent, 19 réussissent.** Les échecs se regroupent en 6 bogues,
chacun suivi par une issue GitHub :

| Bogue | Tests en échec |
|-------|----------------|
| `subtract` retourne `b - a` | `test_subtract_ordre_des_operandes`, `test_subtract_resultat_negatif`, `test_soustraction` |
| `multiply` utilise `**` | `test_multiply_deux_entiers`, `test_multiply_par_zero`, `test_multiplication`, `test_post_multiplication_affiche_le_produit` |
| `divide` utilise `//` | `test_divide_resultat_decimal`, `test_division_decimale` |
| Division par zéro non gérée proprement | `test_division_par_zero_leve_value_error` |
| Nombres négatifs refusés | `test_premier_operande_negatif`, `test_second_operande_negatif`, `test_soustraction_d_un_negatif` |
| `inf` et `nan` acceptés | `test_inf_et_nan_refuses` (2 cas) |

Après les corrections (partie 4), les 34 tests doivent réussir.

## Dépendances et hypothèses

- `pytest` et `flask` (voir `requirements.txt`).
- `test_routes.py` suppose que `templates/index.html` affiche la variable `result`.
