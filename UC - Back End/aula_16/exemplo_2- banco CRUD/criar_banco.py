# Importando a biblioteca sqlite3 que ja vem instalado com o python
import sqlite3

# Cria ou conecta ao banco de dados 
conexao=sqlite3.connect("petshop.db")

# Cria um cursor para executar o comando SQL
cursor=conexao.cursor()

# Executa o comando SQL para criar a tabela clientes
cursor.execute("""CREATE TABLE IF NOT EXISTS clientes(
    id integer primary key autoincrement,
    nome text not null, 
    telefone text,
    email text
    );
""")

# Executa o comando SQL para criar a tabela pets

cursor.execute("""CREATE TABLE IF NOT EXISTS pets(
    id integer primary key autoincrement,
    nome text not null,
    especie text not null,
    idade integer,
    cliente_id integer,
    FOREIGN KEY (cliente_id) REFERENCES clientes(id)
    );
""")

# Executa o comendo SQL para criar a tabela servicos
cursor.execute("""CREATE TABLE IF NOT EXISTS servicos(
    id integer primary key autoincrement,
    descricao text not null,
    preco real not null    
    );
""")

# Salva todas as alterações feitas no banco
conexao.commit()
# Fecha a conexão com o banco de dados
conexao.close()
# Exibe uma mensagem informando que o banco foi criado com sucesso
print("Banco de dados criado com sucesso!")