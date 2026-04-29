import sqlite3
class DataBase:
    database= "database.db"
    
    @classmethod
    def get_connection(cls):
        conn= sqlite3.connect(cls.database)
        conn.row_factory= sqlite3.Row
        return conn

    # Cria tabela se não existir
    @classmethod
    def create_table(cls):
        conn= cls.get_connection()
        cursor= conn.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS fale_conosco(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            sobrenome TEXT NOT NULL,
            data_nascimento TEXT NOT NULL,
            endereco TEXT NOT NULL,
            bairro TEXT NOT NULL,
            cidade TEXT NOT NULL,
            estado TEXT NOT NULL,
            sexo TEXT NOT NULL,
            telefone TEXT NOT NULL,
            email TEXT NOT NULL,
            usuario TEXT NOT NULL,
            senha TEXT NOT NULL,
            observacao TEXT NOT NULL)""")
        conn.commit()
        conn.close()