# Example Mapping

## Format de restitution
*(rappel, pour chaque US)*

```markdown
## Titre de l'US (post-it jaunes)

> Question (post-it rouge)

### Règle Métier (post-it bleu)

Exemple: (post-it vert)

- [ ] 5 USD + 10 EUR = 17 USD
```

Vous pouvez également joindre une photo du résultat obtenu en utilisant les post-its.

## Évaluation d'un portefeuille

> Comment est-ce que l'on peut consulter notre solde ?
> La banque accepte-elle des ajouts d'argents dans une devise dont elle n'a pas le taux de change ?
> Quels sont les devises que la banque accepte ?

### Règle Métier (post-it bleu)

> On peut ajouter de l'argent de différentes devises dans un même portfolio
> Le montant ajouté est d'une valeur normal dans une devise existante
> On ne peut pas évaluer un portfolio si la banque ne dispose pas des taux de changes nécessaires pour le faire
> On peut comparer les taux de changes entre plusieurs banques
> Si la banque où l'on souhaite convertir notre devise en une autre ne dispose pas de la convertion cela renvoie un message d'erreur

Exemple: (post-it vert)

- [x] Étant donné un portfolio vide, lorsque je veux évaluer mon portfolio, la banque me renvoie 0.
- [x] Étant donné un portfolio vide, lorsque je veux ajouter 10 EUR à mon portfolio, alors le portfolio a désormais 10 EUR.
- [x] Étant donné un portfolio contenant 10 EUR et une banque qui n'a pas de taux de change, lorsque je veux évaluer mon portfolio en USD, alors on me renvoie une erreur.
- [x] Étant donné un portfolio contenant 10 EUR et une banque qui a un taux de change EUR vers USD de 1, lorsque je veux évaluer mon portfolio en USD, alors on me renvoie 10 USD.

## Image
![Example Mapping](../img/our-example-mapping.jpg)