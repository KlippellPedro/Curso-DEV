import sqlite3
conexao = sqlite3.connect("loja_carros.db")
cursor = conexao.cursor()

cursor.execute("""SELECT
               pessoas.nome,
               pessoas.cpf,
               carros.modelo,
               carros.marca,
               carros.ano,
               carros.preco,
               vendas.data_venda FROM vendas
               LEFT JOIN pessoas ON pessoas.id = vendas.pessoa_id
               LEFT JOIN carros ON carros.id = vendas.carro_id;
""")

resultado = cursor.fetchall()
print("Resultado da consulta JOIN:\n")
for linha in resultado:
    print(linha)
    
conexao.close()
print("\nConsulta finalizada com sucesso!")    