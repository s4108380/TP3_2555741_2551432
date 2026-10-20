# Calculatrice web — LOG3000 TP3

**Équipe :** 2555741 & 2551432 (Polytechnique Montréal, LOG3000)

## Objectif et portée

Application web de calculatrice simple construite avec **Flask** (Python).
L'utilisateur saisit une expression à un seul opérateur (`+`, `-`, `*`, `/`),
par exemple `12 * 3`, et le serveur renvoie le résultat dans la même page.

Ce dépôt sert aussi de support au TP3 : mise en place d'un dépôt GitHub,
documentation du code, tests automatisés, suivi des bogues par issues et
corrections via branches et pull requests.

**Dans la portée :** opérations binaires (deux opérandes), nombres décimaux,
messages d'erreur lisibles.
**Hors portée :** expressions composées (`1+2*3`), parenthèses, fonctions
scientifiques, historique des calculs.

## Structure du projet

```
.
├── app.py              # Serveur Flask, analyse et évaluation des expressions
├── operators.py        # Fonctions arithmétiques (add, subtract, multiply, divide)
├── templates/          # Gabarit HTML de l'interface (voir templates/README.md)
├── static/             # Feuille de style CSS (voir static/README.md)
├── tests/              # Tests pytest (voir tests/README.md)
├── requirements.txt    # Dépendances Python
└── pytest.ini          # Configuration de pytest
```

## Prérequis

- Un compte GitHub et **Git**
- **Python 3.10 ou plus récent** et **pip**

Vérifier les versions installées :

```bash
git --version
python --version     # ou python3 --version
pip --version
```

## Installation

1. **Cloner le dépôt**
   ```bash
   git clone https://github.com/s4108380/TP3_2555741_2551432.git
   cd TP3_2555741_2551432
   ```
2. **Créer un environnement virtuel**
   ```bash
   python -m venv venv
   ```
3. **Activer l'environnement**
   - Windows (PowerShell) : `venv\Scripts\Activate.ps1`
   - Windows (cmd) : `venv\Scripts\activate.bat`
   - macOS / Linux : `source venv/bin/activate`
4. **Installer les dépendances**
   ```bash
   pip install -r requirements.txt
   ```

## Utilisation

1. Lancer le serveur (environnement virtuel activé) :
   ```bash
   python app.py
   ```
2. Ouvrir <http://127.0.0.1:5000> dans un navigateur.
3. Saisir une expression puis la valider. Le résultat s'affiche dans la page.

Format accepté : `<nombre> <opérateur> <nombre>`. Les espaces sont ignorés.

| Expression | Résultat attendu |
|------------|------------------|
| `2 + 3`    | `5`              |
| `10 - 4`   | `6`              |
| `6 * 7`    | `42`             |
| `7 / 2`    | `3.5`            |

Une expression invalide (vide, opérateur manquant, texte, division par zéro)
affiche un message commençant par `Error:`.

> Le serveur démarre en mode `debug=True` (rechargement automatique). Ce mode
> est réservé au développement local.

## Tests

```bash
pytest            # exécute toute la suite
pytest -v         # détail test par test
pytest tests/test_operators.py   # un seul fichier
```

Les tests couvrent les opérations (`operators.py`), l'analyse des expressions
(`calculate` dans `app.py`) et la route web `/`. Le détail est dans
[tests/README.md](tests/README.md).

## Flux de contribution

1. **Issue d'abord** : tout bogue ou ajout commence par une issue GitHub
   (description, étapes de reproduction ou test en échec, assigné).
2. **Une branche par issue**, créée depuis `main` :
   ```bash
   git checkout main && git pull
   git checkout -b fix/<numero-issue>-<description-courte>
   ```
   Exemple : `fix/3-soustraction-inversee`.
3. **Corriger** puis relancer `pytest` : le test concerné doit passer.
4. **Commit** avec un message qui explique la correction :
   ```bash
   git commit -m "Corrige subtract: retourne a - b (fixes #3)"
   ```
5. **Pull Request** vers `main`, qui référence l'issue (`Closes #3`).
6. **Revue** par un autre membre de l'équipe, puis fusion une fois les tests
   verts. Ne jamais pousser directement sur `main`.
