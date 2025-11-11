""" Database support """
import sqlite3
from pathlib import Path
from user import User

BASE_DIR = Path(__file__).resolve().parent
DB_FILE = str((BASE_DIR / "users.db").resolve())

class Database:
    """ doctring """
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
        """ doctring """
        query = "SELECT uid, uname, password FROM user WHERE uname LIKE ?"
        params = (f"%{term}%",)
        # return list of User instances
        return self._run_query(query, params)

    def load(self, user_id) -> User:
        """ returns single User instance """
        query = "SELECT uid, uname, password FROM user WHERE uid = ?"
        params = (user_id,)
        d = self._run_query(query, params)
        row = d['rows']
        uid, uname, pw = row[0]['uid'], row[0]['uname'], row[0]['password']
        user = User(uid, uname, pw)
        return user

    def load_all(self):
        """ doctring """
        query = "SELECT * FROM user"
        # return list of User instances
        return self._run_query(query, ())

    def insert(self, user: User) -> None:
        """ doctring """
        query = "INSERT INTO user (uid, uname, password) VALUES (?, ?, ?)"
        params = (user.get_uid(), user.get_uname(), user.get_password() )
        # Insert User instance into database
        self._execute(query, params)

db = Database()
print(db.load(1))
