from database import Database

db = Database() # opret et objekt af typen database
print(db.load(1))
# lav en søgning og vis resultat
user = "mkm"
print(db.search(user))

# opret en ny post
db.insert(uid = 232, name = "Henrik", password = "hemmeligt")

# hent den nye post og vis den
print(db.load(232))

# vis alle rækker
print(db.load_all())
