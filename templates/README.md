# `templates/` — gabarits HTML

## Raison d'être

Contient les gabarits Jinja2 rendus par Flask via `render_template`. Ils
forment l'interface utilisateur de la calculatrice.

## Fichiers principaux

| Fichier      | Responsabilité                                                        |
|--------------|-----------------------------------------------------------------------|
| `index.html` | Page unique : afficheur, boutons et formulaire. Envoie l'expression en `POST` vers `/` (champ `display`) et affiche la variable `result`. |

## Dépendances et hypothèses

- Le serveur (`app.py`, fonction `index`) fournit la variable `result` : vide
  au premier chargement, nombre après un calcul, ou chaîne `Error: ...`.
- Le champ de formulaire doit se nommer `display` : c'est la clé lue par
  `request.form.get('display')`.
- La feuille de style provient de `static/` (voir `static/README.md`).
- Flask exige que ce dossier s'appelle exactement `templates`.
