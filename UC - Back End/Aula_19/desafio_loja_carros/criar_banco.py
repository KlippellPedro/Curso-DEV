import sqlite3
conexao = sqlite3.connect("loja_carros.db")
conexao.execute("PRAGMA foreign_keys = ON")
cursor = conexao.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS pessoas(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               nome TEXT NOT NULL,
               cpf TEXT NOT NULL);
""")

cursor.execute("""CREATE TABLE IF NOT EXISTS carros(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               modelo TEXT NOT NULL,
               marca TEXT NOT NULL,
               ano INTEGER NOT NULL,
               preco REAL NOT NULL);
""")

cursor.execute("""CREATE TABLE IF NOT EXISTS vendas(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               data_venda TEXT NOT NULL,
               carro_id INTEGER, 
               pessoa_id INTEGER,
               FOREIGN KEY (carro_id) REFERENCES carros (id),
               FOREIGN KEY (pessoa_id) REFERENCES pessoas (id));
""")

conexao.commit()
conexao.close()
print("Database criado com sucesso!")
