import sqlite3
conexao = sqlite3.connect("escola.db")
conexao.execute("PRAGMA foreign_key = ON")
cursor = conexao.cursor()

# Inserir pessoas na tabela
cursor.execute("INSERT INTO pessoas (nome, cpf) VALUES (?, ?)", 
               ("Carlos da Silva", "11111111111"))
cursor.execute("INSERT INTO pessoas (nome, cpf) VALUES (?, ?)", 
               ("Ana de Souza", "22222222222"))

# Inserir funcionário vinculado a pessoa id = 1
cursor.execute("INSERT INTO funcionario (cargo, salario, pessoa_id)VALUES(?,?,?)", 
               ("Professor", 5000.00, 1))

# Insere cliente vinculado a pessoa id = 2
cursor.execute("INSERT INTO cliente (tipo_cliente, pessoa_id)VALUES(?, ?)", 
               ("VIP", 2))

conexao.commit()
conexao.close()
print("Dados inseridos com sucesso!")