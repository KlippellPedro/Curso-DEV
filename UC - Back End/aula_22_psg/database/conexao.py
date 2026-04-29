import sqlite3

class Conexao:
    def conectar():
        return sqlite3.connect("escola.db")
    def criar_tabela():
        conn = sqlite3.connect("escola.db")
        cursor = conn.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS aluno(
                       id INTEGER PRIMARY KEY AUTOINCREMENT,
                       nome TEXT,
                       sobrenome TEXT,
                       idade INTEGER
                       )
        """)

        conn.commit()
        conn.close()