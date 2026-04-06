import sqlite3
conexao=sqlite3.connect("petshop.db")
cursor=conexao.cursor()

cursor.execute("""UPDATE clientes SET telefone=? WHERE id=?
""", ("51888888888", 1))

cursor.execute("""UPDATE pets SET idade=? WHERE id=?
""", (6,1))

cursor.execute("""UPDATE servicos SET preco=? WHERE id=?
""", (95.00, 1))

cursor.execute("""UPDATE pets SET cor_pelo=? WHERE id=?
""", ("preto", 1))

conexao.commit()
conexao.close()
print("Informações atualizadas com sucesso!")