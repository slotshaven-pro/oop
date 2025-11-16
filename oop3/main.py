import random
from database import Database
from user import User

# opret et objekt af typen database
db = Database()
print(db.load(2567))

# lav en søgning og vis resultat
print(db.search("mkm"))

# lav tilfældig bruger og opret en ny post
uid = random.randint(1_000, 9_999)
random_user = User(uid, f"user_{uid}", f"user_{uid}")
db.insert(random_user)

# hent den nye post og vis den
print(db.load(uid))

# vis alle rækker
print(db.load_all())
