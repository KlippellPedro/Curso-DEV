import sqlite3
def get_connection():
    conn = sqlite3.connect("registros.db")
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS clientes(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   nome TEXT NOT NULL,
                   sobrenome TEXT NOT NULL,
                   endereco TEXT NOT NULL,
                   numero INT NOT NULL,
                   complemento TEXT NOT NULL,
                   bairro TEXT NOT NULL,
                   cidade TEXT NOT NULL,
                   estado TEXT NOT NULL,
                   data_nasc DATE NOT NULL,
                   cpf TEXT NOT NULL,
                   rg TEXT NOT NULL,
                   email TEXT NOT NULL,
                   telefone TEXT NOT NULL
                   )
    """)
    conn.commit()
    conn.close()