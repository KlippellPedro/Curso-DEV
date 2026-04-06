import sqlite3
conexao=sqlite3.connect("petshop.db")
cursor=conexao.cursor()

# Inserindo dados na tabela clientes
cursor.execute("""INSERT INTO clientes (nome, telefone, email) VALUES (?,?,?)
""", ("João da Silva", "51997491810", "joao@gmail.com"))

# Executa o comando SQL para inserir o segundo cliente
cursor.execute("""INSERT INTO clientes (nome,telefone,email) VALUES(?,?,?)
""", ("Maria da Silva", "51997443331", "maria@gmail.com"))

# Inserindo dados na tabela pets

# Executa o comando SQL para inserir o primeiro pet
# cliente id=1,
cursor.execute("""INSERT INTO pets (nome,especie,idade,cliente_id) VALUES (?,?,?,?)
""", ("Rex", "Cachorro", 3,2))

# Inserindo dados na tabela servicos

# Executando o comando SQL para inserir o primeiro sevoço
cursor.execute("""INSERT INTO servicos (descricao, preco) VALUES (?,?)
""", ("Banho e tosa", 80.00))

cursor.execute("""INSERT INTO servicos (descricao, preco) VALUES (?,?)
""", ("Consulta veterinária", 150.00))

conexao.commit()
conexao.close()
print("Tabelas populadas com sucesso!")