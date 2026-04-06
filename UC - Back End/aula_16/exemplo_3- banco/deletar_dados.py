import sqlite3
conexao=sqlite3.connect("petshop.db")
cursor=conexao.cursor()

# Deleta primeiro o pet pra não dar erro no cliente
cursor.execute("""DELETE FROM pets WHERE id=?
""", (2,))

# So vai deletar se não tiver nenhuma chave estrangeira ligada ao cliente que for ser deletado
cursor.execute("""DELETE FROM clientes WHERE id=?
""", (2,))

cursor.execute("""DELETE FROM servicos WHERE id=?
""", (2,))

conexao.commit()
conexao.close()
print("Informações deletadas com sucesso!")