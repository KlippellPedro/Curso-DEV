import sqlite3
conexao = sqlite3.connect("escola.db")
cursor = conexao.cursor()

# Executa JOIN entre as três tabelas
cursor.execute("""
SELECT
               pessoas.nome,
               pessoas.cpf,
               funcionario.cargo,
               funcionario.salario,
               cliente.tipo_cliente FROM pessoas 
               LEFT JOIN funcionario ON pessoas.id = funcionario.pessoa_id 
               LEFT JOIN cliente ON pessoas.id = cliente.pessoa_id;
""")

# Armazena o resultado
resultado = cursor.fetchall()
# Exibe dados do JOIN
print("Resultado da consulta JOIN:\n")
#Percorre cada linha do resultado
for linha in resultado:
    print(linha)

conexao.close()
print("\nConsulta finalizada com sucesso!")    