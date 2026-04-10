import sqlite3
conexao = sqlite3.connect("loja_carros.db")
conexao.execute("PRAGMA foreign_key = ON")
cursor = conexao.cursor()

cursor.execute("INSERT INTO pessoas (nome, cpf) VALUES (?,?)", 
               ("João Pereira", "84599602845"))

cursor.execute("INSERT INTO pessoas (nome, cpf) VALUES (?,?)", 
               ("Maria Costa", "03588318093"))

cursor.execute("INSERT INTO carros (modelo, marca, ano, preco)VALUES(?,?,?,?)", 
               ("Corolla", "Toyota", "2022", "120000"))

cursor.execute("INSERT INTO carros (modelo, marca, ano, preco)VALUES(?,?,?,?)", 
               ("Civic", "Honda", "2021", "115000"))

cursor.execute("INSERT INTO vendas (carro_id, pessoa_id, data_venda)VALUES(?,?,?)", 
               (1, 1, "25/04/2025"))

cursor.execute("INSERT INTO vendas (carro_id, pessoa_id, data_venda)VALUES(?,?,?)", 
               (2, 2, "25/04/2025"))

conexao.commit()
conexao.close()
print("Dados populados nas tabelas com sucesso!")