""" Lightweight database library """
import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DB_FILE = str((BASE_DIR / "users.db").resolve())

class Database:
    """ Handles db connections """
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
        """ TODO implementation"""
        query = "SELECT uid, uname, password FROM user WHERE uname LIKE ?"
        params = (f"%{term}%",)
        return self._run_query(query, params)

    def load(self, user_id):
        """ TODO implementation"""
        query = "SELECT uid, uname, password FROM user WHERE uid = ?"
        params = (user_id,)
        return self._run_query(query, params)

    def load_all(self):
        """ TODO implementation"""
        query = "SELECT * FROM user"
        return self._run_query(query, {})

    def insert(self, uid, name, password) -> None:
        """ TODO implementation"""
        query = "INSERT INTO user (uid, uname, password) VALUES (?, ?, ?)"
        try:
            self._execute(query, (uid, name, password))
        except():
            return None

    def delete(self, uid: int):
        """ TODO implementation"""
        query = "DELETE from user where (uid) = (?)"
        params = (uid,)
        self._execute(query, params)

    def update(self, uid, name, password):
        """ TODO implementation"""
