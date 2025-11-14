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
        """ Create and return connection """
        conn = sqlite3.connect(self.db_file)
        conn.row_factory = sqlite3.Row
        return conn

    def _execute(self, query: str, params: tuple):
        """ execute query in db """
        conn = self._connect()
        try:
            conn.execute(query, params)
            conn.commit()
        finally:
            conn.close()

    def _run_query(self, query: str, params: tuple):
        " run select query against db "
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
        """ returns single User instance """
        query = "SELECT uid, uname, password FROM user WHERE uid = ?"
        params = (user_id,)
        d = self._run_query(query, params)
        row = d['rows'][0]
        user_id, user_name, pw = row['uid'], row['uname'], row['password']
        return User(user_id, user_name, pw) # Make User instance

    def load_all(self):
        """ returns list of Users """
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
        params = (user.get_uid(), user.get_uname(), user.get_password() )
        # Insert User instance into database
        self._execute(query, params)

    def delete(self, user: User):
        """ Deletes a User instance """
        query = "DELETE from user where (uid) = (?)"
        params = (user.get_uid(),)
        self._execute(query, params)

    def update(self, user_id: int, user: User):
         """ TODO implementation"""

# Testing Database class
if __name__ == "__main__":
    db = Database()
    uid = random.randint(1_000, 9_999)
    random_user = User(uid, f"user_{uid}", f"user_{uid}")
    db.insert(random_user)
    inserted = db.load(uid)
    print(f"Inserted random user {inserted.get_uname()} with uid {inserted.get_uid()}")
    u = db.search('user_')
    print(f"Search for user: {u}")
    print("All users:")
    print(db.load_all())
