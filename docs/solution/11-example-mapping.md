## US 1 — Définir une devise pivot

```
As a Foreign Exchange Expert
I want to be able to define a Pivot Currency
So that I can express exchange rates based on it
```

### Règles

- Quand je crée une banque alors je ne peux pas ne pas avoir de devise pivot  
  Exemple : [x] Lorsque je tente de créer une banque sans devise pivot Alors une exception est levée  

- Quand je tente de changer la devise pivot alors cela lève une exception  
  Exemple : [x] Étant donné une banque avec une devise pivot en euro Lorsque je change la devise pivot Alors une exception est levée  

---

## US 2 — Ajouter / modifier des taux de change

```
As a Foreign Exchange Expert
I want to add/update exchange rates by specifying: a multiplier rate and a currency
So they can be used to evaluate client portfolios
```

### Règles

- Quand j'ajoute un taux de change alors il doit tout le temps être un couple devise / multiplicateur  
  Exemple : [x] Étant donné une banque ayant déjà un taux de change vers l'USD à 1.2 ainsi qu'une devise pivot en EUR Lorsque j'ajoute un taux de change vers l'USD à 1.3 Alors quand je convertis 10 EUR en USD, je dois obtenir 13 USD  

- Quand j'ajoute un taux de change alors il n'y a pas de limitation quant au nombre de taux possibles  
  Exemple : [] Étant donné une banque ayant déjà un taux de change EUR to USD ainsi qu'une devise pivot en EUR Lorsque j'ajoute un taux de change EUR to KWR à 1.3 Alors on peut convertir une somme en EUR en KWR  

- Quand je tente d'ajouter un taux de change négatif alors cela me lève une exception  
  Exemple : [] Étant donné une banque avec une devise pivot en EUR Lorsque je tente d'ajouter un taux de change EUR->USD = -1.2 Alors cela lève une exception  

- Quand je tente de modifier un taux de change par une valeur négative alors cela me lève une exception  
  Exemple : [] Étant donné une banque avec au moins une devise pivot en EUR Lorsque je tente de modifier un taux de change EUR->USD par -1.2 Alors cela lève une exception  

- Quand je tente d'ajouter un taux de change existant alors cela modifie la valeur de ce dernier  
  Exemple : [] Étant donné une banque ayant déjà un taux de change EUR to USD 1.2 Lorsque je tente d'ajouter un taux de change EUR to USD de 1.3 Alors le taux de change EUR to USD voit sa valeur mise à 1.3  

- Quand je tente de modifier un taux de change par 0 alors cela me lève une exception  
  Exemple : [] Étant donné une banque avec au moins une devise pivot en EUR Lorsque je tente de modifier un taux de change EUR->USD par 0 Alors cela lève une exception  

- Tous les taux de change sont exprimés depuis la devise pivot vers une autre devise  Quand je crée un taux de change il faut obligatoirement que la devise pivot soit présente
  Exemple : [] Étant donné une banque avec une devise pivot en EUR Alors un taux EUR->USD = 1.2 signifie que 1 EUR = 1.2 USD  

---

## US 3 — Convertir des montants

```
As a Bank Consumer
I want to convert a given amount in currency into another currency
So it can be used to evaluate client portfolios

```

### Règles

- Quand je souhaite convertir une somme dans une autre devise alors je multiplie par le taux de change de la banque  
  Exemple : [] Étant donné une banque avec l'EUR comme devise pivot et un taux de change en USD de 1.2 Lorsque je veux convertir 10 EUR en USD Alors la banque me renvoie 12 USD  

- Quand je souhaite convertir une somme dans une autre devise que la devise pivot de ma banque alors je multiplie par l'inverse du taux de change de la banque  
  Exemple : [] Étant donné une banque avec l'EUR comme devise pivot et un taux de change en USD de 1.2 Lorsque je veux convertir 12 USD en EUR Alors la banque me renvoie 10 EUR  

- Quand je souhaite convertir une somme entre deux devises qui ne sont pas la devise pivot alors la conversion passe par la devise pivot  
  Exemple : [] Étant donné une banque avec l'EUR comme devise pivot, un taux EUR->USD = 1.2 et un taux EUR->GBP = 0.8 Lorsque je veux convertir 12 USD en GBP Alors la banque convertit 12 USD en EUR puis EUR en GBP  

- Quand je tente de convertir une somme vers une devise dont le taux de change n'existe pas alors cela lève une exception  
  Exemple : [] Étant donné une banque avec une devise pivot en EUR et aucun taux vers JPY Lorsque je tente de convertir 10 EUR en JPY Alors cela lève une exception  

- Quand je convertis une somme vers la même devise alors le montant reste inchangé  
  Exemple : [] Étant donné une banque avec l'EUR comme devise pivot Lorsque je veux convertir 10 EUR en EUR Alors la banque me renvoie 10 EUR  

- Quand je convertis une somme alors le résultat est arrondi selon une précision définie (ex : 2 décimales)  
  Exemple : [] Étant donné une banque avec l'EUR comme devise pivot et un taux EUR->USD = 1.23456 Lorsque je convertis 10 EUR en USD Alors la banque me renvoie 12.35 USD  

- Quand je tente d'utiliser une devise inconnue alors cela lève une exception  
  Exemple : [] Étant donné une banque avec une devise pivot en EUR Lorsque je tente de convertir 10 EUR en XXX Alors cela lève une exception  

- Quand je tente de convertir un montant négatif alors cela lève une exception  
  Exemple : [] Étant donné une banque avec une devise pivot en EUR Lorsque je tente de convertir -10 EUR en USD Alors cela lève une exception  

- Quand je convertis un montant égal à 0 alors le résultat est 0  
  Exemple : [] Étant donné une banque avec une devise pivot en EUR et un taux EUR->USD = 1.2 Lorsque je convertis 0 EUR en USD Alors la banque me renvoie 0 USD  
