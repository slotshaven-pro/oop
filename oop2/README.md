# OOP: klasser og objekter

## Opgave 2: Byg din egen database-klasse

En database-klasse håndterer alle forbindelser og forespørgsler til databasen. Den kan anvendes sådan fx her:

```python
db = Database()
db.load_all()
```

## Eksemplet

Klassen `Database` i `database.py` viser hvordan en database-klasse kan bygges.

Brug den som reference eller skabelon, når du bygger din egen databaseklasse.

## Sådan gør du

Kopier din database fra flask-projektet ind i projektet.

Husk `DB_FILE` skal pege på din egen database.

Implementer søgning, opslag, hent-alle som klasse-metoder:

- `search(term)`
- `load(id)`
- `load_all()`

med de nødvendige pararmetre.

Hvis du vil, kan du også implementere:

- `delete()`
- `insert()`
- `update()`

med de nødvendige paramtre.

Til sidst: Skriv en lille test i som i eksemplet og kør den.
