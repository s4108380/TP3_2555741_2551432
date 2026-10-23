"""Application web Flask de la calculatrice.

Ce module expose une unique page (``/``) contenant l'interface de la
calculatrice. L'utilisateur saisit une expression de la forme
``<nombre> <opérateur> <nombre>`` ; le serveur l'évalue et réaffiche la
page avec le résultat (ou un message d'erreur).

Lancement en développement : ``python app.py``.
"""

from flask import Flask, request, render_template

from operators import add, subtract, multiply, divide

app = Flask(__name__)

# Table de correspondance symbole -> fonction. Ajouter un opérateur ici
# suffit pour que ``calculate`` le reconnaisse.
OPS = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
}


def calculate(expr: str):
    """Évalue une expression arithmétique à un seul opérateur.

    Le format attendu est ``<nombre><opérateur><nombre>``. Les espaces sont
    ignorés (``"2 + 3"`` équivaut à ``"2+3"``).

    Args:
        expr (str): L'expression saisie par l'utilisateur.

    Returns:
        float: Le résultat de l'opération.

    Raises:
        ValueError: Si l'expression est vide, si elle contient plus d'un
            opérateur, si l'opérateur est absent ou placé au début/à la fin,
            ou si un opérande n'est pas un nombre.
    """
    if not expr or not isinstance(expr, str):
        raise ValueError("empty expression")

    # Les espaces n'ont aucun sens pour le calcul : on les retire avant
    # l'analyse pour simplifier le repérage de l'opérateur.
    s = expr.replace(" ", "")

    # Parcours caractère par caractère pour repérer l'unique opérateur
    # (-1 signifie « aucun opérateur trouvé »).
    op_pos = -1
    op_char = None
    for i, ch in enumerate(s):
        if ch in OPS:
            if op_pos != -1:
                raise ValueError("only one operator is allowed")
            op_pos = i
            op_char = ch

    # Opérateur absent, en première position ou en dernière position :
    # il manque au moins un opérande.
    if op_pos <= 0 or op_pos >= len(s) - 1:
        raise ValueError("invalid expression format")

    left = s[:op_pos]
    right = s[op_pos+1:]

    try:
        a = float(left)
        b = float(right)
    except ValueError:
        # On relance une erreur au message uniforme pour l'interface.
        raise ValueError("operands must be numbers")

    return OPS[op_char](a, b)


@app.route('/', methods=['GET', 'POST'])
def index():
    """Affiche la calculatrice et traite la soumission d'une expression.

    - ``GET`` : affiche la page avec un résultat vide.
    - ``POST`` : lit le champ de formulaire ``display``, calcule le résultat
      et le transmet au gabarit ``index.html``. Toute erreur est convertie
      en chaîne ``"Error: <message>"`` afin que la page ne plante jamais.

    Returns:
        str: Le HTML de la page rendue.
    """
    result = ""
    if request.method == 'POST':
        expression = request.form.get('display', '')
        try:
            result = calculate(expression)
        except Exception as e:
            # Exception volontairement large : l'utilisateur doit toujours
            # voir un message plutôt qu'une page d'erreur 500.
            result = f"Error: {e}"
    return render_template('index.html', result=result)


if __name__ == '__main__':
    # debug=True : rechargement automatique et débogueur interactif.
    # À réserver au développement local (jamais en production).
    app.run(debug=True)
