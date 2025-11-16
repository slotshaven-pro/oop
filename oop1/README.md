# OOP: klasser og objekter

## Opgave 1: Byg din egen entitets-klasse

En entitet er en klasse (datatype) der repræsentaterer den genstand som dit webserver-projekt handlede om og svarer groft sagt til en rækkke i din database.

## Eksempel på entitets-klasse

Klasse `user.py` viser hvordan en User-klasse kan bygges for et User-objekt med agenskaberne:

- id (`uid`)
- brugernavn (`uname`)
- adgangskode (`password`)

## Sådan gør du

Brug `user.py` som reference eller skabelon, når du bygger din egen entitetsklasse.

Kig på din egen database fra flask-projektet og byg en tilsvarende klasse for din egen entitet. Indeholder din database fx film, kunstværker, webshops, skal du bygge en klasse sådan her:

- class `Film` i filen `film.py`
- class `Artwork` i filen `artwork.py`
- class `Webshop` i filen `webshop.py`

Dit klassenavn skal begynde med STORT forbogstav og være i ENTAL - den repræsenterer ET objekt (svarende til en række i databasen).

Eksempel med film - i `film.py` begynder du sådan her:

```python
class Film:
```

Tilføj som minimum en constructor `__init__()` med de nødvendige parametre og den "magiske" metode `__str__()` som kaldes når objektet printes.

Skriv en lille test som i eksemplet og test din klasse.

```python
# Testing User entity med kommandoen `python user.py`
if __name__ == "__main__":
    # Create and print random user (username) 1
    uid = random.randint(1_000, 9_999)
    # Create random user name and password from uid
    random_user = User(uid, f"user_{uid}", f"user_{uid}")
```

