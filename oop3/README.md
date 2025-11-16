# OOP: klasser og objekter

## Opgave 3: Ombyg din database-klasse til at bruge din egen entitets-klasse

En database-klasse håndterer alle forbindelser og forespørgsler til databasen. Her anvendes `User`-klassen igen som eksempel. Den kan anvendes sådan fx her:

```python
db = Database()
# Create and save user
user = User(1, 'some-random-user', 'very-secret-password')
db.insert(user)
# Load all user and print them
user_list = db.load_all()
for user in user_list:
    print(user)
```

## Eksemplet

Klassen `Database` i `database.py` viser hvordan en database-klasse som bruger `User`-objektet kan bygges.

Brug den som reference eller skabelon, når du ombygger din database-klasse.

## Sådan gør du

Omskriv din `Database`-klasse så den modtager og returnerer din entitets-klasse.

Metoderne

- `search(term)`
- `load(id)`
- `load_all()`

returnere din klasse. Hvis der er flere objekter, returnér dem i en liste af klasse-instanser.
Hvis der kun er et objekt (som fx med ´load()`), kan du returnere det en instans af klassen.

Igen, hvis du vil, kan du også implementere eller omskrive:

- `delete()`
- `insert()`
- `update()`

med de nødvendige paramtre.

Til sidst: Skriv en lille test som i eksemplet og kør den.
