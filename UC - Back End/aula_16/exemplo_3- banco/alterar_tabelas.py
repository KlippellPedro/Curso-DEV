import sqlite3
conexao=sqlite3.connect("petshop.db")
cursor=conexao.cursor()

cursor.execute("""ALTER TABLE clientes RENAME COLUMN nome TO nome_dono;""")

cursor.execute("""ALTER TABLE pets RENAME COLUMN nome TO nome_pet;""")

cursor.execute("""ALTER TABLE pets ADD COLUMN cor_pelo text;""")

conexao.commit()
conexao.close()
print("Tabelas alteradas com sucesso!")