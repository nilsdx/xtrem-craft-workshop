# Clean code VS Dirty code

## Qu'est-ce que du code sale ?

- duplication de code (exemple: une fonction et un endroit dans le code qui effectue la même chose que la fonction)
- commentaires "inutiles" (ex: décrit le code)
- fonctions trop longues (ex: 79 lignes max)
- obsolescence des dépendances
- code inutilisé (variables, paramètres, ...)

## Qu'est-ce que du code propre ?

- Respect des conventions de code et de nommage (automatisé ?) (ex: PEP 8)
- Code en une langue unique (sur notre projet en anglais)
- Commentaires "haut niveau"
- Nom des variables et des fonctions sans duplications, cohérentes et explicites
- Documentation technique efficace et concise
- Organisation du code: attributs en haut, suivi du constructeurs, de ses getters/setters, ...
- Une fonction effectue une tâche (single responsibility)
- Historique MAJ clair (git, changelogs)
- Gestion de paquets/modules
- Design patterns
