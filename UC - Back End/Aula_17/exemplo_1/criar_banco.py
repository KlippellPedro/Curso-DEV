# Importa a biblioteca sqlite3
import sqlite3
# Conecta ao banco de dados escola.db ou cria se não existir
conexao = sqlite3.connect("escola.db")
# Ativa suporte a chave estrangeira
conexao.execute("PRAGMA foreign_keys = ON")
# Cria cursor para executar os comandos SQL
cursor = conexao.cursor()

# Cria tabela pessoas
cursor.execute("""
CREATE TABLE IF NOT EXISTS pessoas(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               nome TEXT NOT NULL,
               cpf TEXT NOT NULL
               );
""")
# Cria a tabela funcionario relacionada a pessoas
cursor.execute("""
CREATE TABLE IF NOT EXISTS funcionario(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               cargo TEXT NOT NULL,
               salario REAL NOT NULL,
               pessoa_id INTEGER,
               FOREIGN KEY (pessoa_id) REFERENCES pessoas (id)
               );
""")
# Cria tabela clientes relacionada a pessoas
cursor.execute("""
CREATE TABLE IF NOT EXISTS cliente(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               tipo_cliente TEXT NOT NULL,
               pessoa_id INTEGER,
               FOREIGN KEY (pessoa_id) REFERENCES pessoas(id)
               );
""")
# Salava alterações no banco
conexao.commit()
# Fecha conexão
conexao.close()
# Mensagem final (só vai aparecer se todo código estiver ok)
print("Banco de dados e tabelas criados com sucesso!")
