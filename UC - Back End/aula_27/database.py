import sqlite3
from sqlite3 import Error
from config import DATABASE

def get_connection():
    try:
        conn= sqlite3.connect(DATABASE)
        conn.row_factory= sqlite3.Row
        return conn
    except Error:
        return {"error": "não foi possível conectar no banco de dados"}

def init_db():
    conn= get_connection()
    cursor= conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE,
        senha TEXT NOT NULL)""")
    conn.commit()
    cursor.close()
    conn.close()