""" my custom Database class """
from database import Database

# opret et objekt af typen database
db = Database()

# lav en søgning og vis resultat
print(db.search("mkm"))

# opret en ny post
db.insert(uid = 237, name = "Henrik IIII", password = "hemmeligt")

# slet en post
db.delete(50)

# opdater en post
db.update(50, 'mkm', 'topsecret')

# hent en post
print(db.load(237))

# vis alle poster
print(db.load_all())
