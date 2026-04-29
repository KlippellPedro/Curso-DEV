import sqlite3

class Conexao:
    @staticmethod
    def conectar():
        return sqlite3.connect("database.db")
    
    @staticmethod
    def criar_tabela():
        conn = Conexao.conectar()
        cursor = conn.cursor()
        
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuario(
                       id INTEGER PRIMARY KEY AUTOINCREMENT,
                       nome TEXT,
                       email TEXT,
                       senha TEXT  
                       )
        """)

        conn.commit()
        conn.close()