import sqlite3
from pathlib import Path
import random
from user import User

BASE_DIR = Path(__file__).resolve().parent
DB_FILE = str((BASE_DIR / "users.db").resolve())

class Database:
    """ Database class handles database connections and queries.
        Supports all CRUD operations.
        Uses class "User" as datatype for method parameters and return values.
    """
    def __init__(self, db_file: str = DB_FILE):
        self.db_file = db_file

    def _connect(self):
        """ Internal method that creates and returns connection """
        conn = sqlite3.connect(self.db_file)
        conn.row_factory = sqlite3.Row
        return conn

    def _execute(self, query: str, params: tuple):
        """ Internal method that executes query """
        conn = self._connect()
        try:
            conn.execute(query, params)
            conn.commit()
        finally:
            conn.close()

    def _run_query(self, query: str, params: tuple):
        """ Internal method that runs select query """
        conn = self._connect()
        try:
           cur = conn.execute(query, params)
           rows = cur.fetchall()
        finally:
           conn.close()
        return {"rows": [dict(u) for u in rows]}

    def search(self, term: str):
        """ Searches for user and returns list of User instances """
        query = "SELECT uid, uname, password FROM user WHERE uname LIKE ?"
        params = (f"%{term}%",)
        d = self._run_query(query, params)
        l = []
        for u in d["rows"]:
            user = User(u['uid'], u['uname'], u['password'])
            l.append(user)
        return l

    def load(self, user_id) -> User:
        """ Returns single User instance """
        query = "SELECT uid, uname, password FROM user WHERE uid = ?"
        params = (user_id,)
        d = self._run_query(query, params)
        breakpoint()
        if not d['rows']:
            return None
        row = d['rows'][0]
        user_id, user_name, pw = row['uid'], row['uname'], row['password']
        return User(user_id, user_name, pw) # Make User instance

    def load_all(self):
        """ Returns all users as a list of Users instances """
        query = "SELECT * FROM user"
        params = ()
        d = self._run_query(query, params)
        l = []
        for u in d["rows"]:
            user = User(u['uid'], u['uname'], u['password'])
            l.append(user)
        return l

    def insert(self, user: User) -> None:
        """ Inserts a User instance """
        query = "INSERT INTO user (uid, uname, password) VALUES (?, ?, ?)"
        params = (user.uid, user.uname, user.password )
        # Insert User instance into database
        self._execute(query, params)

    def delete(self, user: User):
        """ Deletes a User instance """
        query = "DELETE from user where (uid) = (?)"
        params = (user.uid,)
        self._execute(query, params)

    def update(self, user_id: int, user: User):
         """ TODO implementation"""

# Testing Database class
if __name__ == "__main__":
    db = Database()

    # Testing non-existing user.
    if u := db.load(23434324):
        print(u)

    uid = random.randint(1_000, 9_999)
    random_user = User(uid, f"username_{uid}", f"password_{uid}")
    print(f"Created random user with uid {uid}")
    print()

    db.insert(random_user)
    print(f"Inserted random user with uid {uid}")
    print()

    loaded_user = db.load(uid)
    print(f"Loaded random user with username {loaded_user.uname}")
    print()

    term = 'user_'
    users = db.search(term)
    print(f"Search for users")
    for user in users:
        print(user)
    print()

    print("All users:")
    users = db.load_all()
    for user in users:
        print(user)
    print()

