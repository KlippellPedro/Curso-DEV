import sqlite3
conexao=sqlite3.connect("petshop.db")
cursor=conexao.cursor()

cursor.execute("SELECT * FROM clientes")
print("CLIENTES: ")
print(cursor.fetchall())

cursor.execute("SELECT * FROM pets")
print("\nPETS: ")
print(cursor.fetchall())

cursor.execute("SELECT * FROM servicos")
print("\nSERVIÇOS: ")
print(cursor.fetchall)

conexao.close()