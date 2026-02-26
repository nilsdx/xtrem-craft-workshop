# Backlog

## What can be improved in the codebase ?

### bank.py
- typo in Bank class: addEchangeRate -> addExchangeRate
- convert's condition is too complex and should be extracted 
to another method that does it instead

### money_calculator.py
- useless parameter in all static methods of the class: 
it seems like the class does calculations with the same 
currency type, so the currency parameter can be removed
