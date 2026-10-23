# `static/` — ressources statiques

## Raison d'être

Contient les fichiers servis tels quels au navigateur par Flask (sous l'URL
`/static/...`). Ici : la feuille de style de la calculatrice.

## Fichiers principaux

| Fichier     | Responsabilité                                              |
|-------------|-------------------------------------------------------------|
| `style.css` | Mise en page et apparence de l'interface (grille de boutons, afficheur, couleurs). |

## Dépendances et hypothèses

- Flask sert automatiquement ce dossier : aucun code Python à écrire.
- Le gabarit `templates/index.html` doit référencer la feuille de style avec
  `url_for('static', filename='style.css')`.
- Les noms de classes et d'identifiants CSS doivent rester synchronisés avec
  le HTML : renommer un élément d'un côté exige de le renommer de l'autre.
