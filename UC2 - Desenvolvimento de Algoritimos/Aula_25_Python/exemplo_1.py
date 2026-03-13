from datetime import datetime

print("--- Sistema de notas ---")
disciplina = input("Informe o nome da disciplina: ")
professor = input("Informe o nome do professor: ")
quant = int(input("Indorme quantos registros deseja realizar: "))
soma_media = 0
dados_arquivo = []

for i in range(1, quant +1):
    print("")
    nome = input("Digite o nome do aluno(a): ")
    turma = input ("Informe a turma: ")
    n1 = int(input("Informe a primeira nota: "))
    n2 = int(input("Informe a segunda nota: "))
    n3 = int(input("Informe a terceira nota: "))

    media = (n1+n2+n3)/3
    soma_media += media

    if media >= 7:
        situacao = "Aprovado"
    elif media >= 5:
        situacao = "Recuperação"
    else:
        situacao = "Reprovado"

    # Captura da data e hora do registro
    data_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    print("")
    print(f"Nome do aluno: {nome}")
    print(f"Turma: {turma}")
    print(f"Primeira nota: {n1}")
    print(f"Segunda nota {n2}")
    print(f"Terceira nota: {n3}")
    print(f"Média final: {media:.1f}")
    print(f"Situação curricular: {situacao}")

    # Armazena e salva o arquivo
    registro = (
        f"Registro realizado em: {data_hora}\n"
        f"Nome: {nome}\n"
        f"Turma: {turma}\n"
        f"Notas: {n1}, {n2}, {n3}\n"
        f"Média final: {media:.1f}\n"
        f"Situação curricular: {situacao}\n"
        f"{''}\n"
    )

    dados_arquivo.append(registro)

media_geral = soma_media / quant
print("")
print(f"Média geral da turma: {media_geral:.2f}")
print("")

nome_arquivo = input("Informe o nome do arquivo (Ex: notas.txt): ")

# Salvar os dados no arquivo
with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
    arquivo.write("-- Relatório de notas dos alunos --\n\n")
    arquivo.write(f"Disciplina: {disciplina}\n")
    arquivo.write(f"Professor: {professor}\n")
    arquivo.write(f"Data do relatório: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n\n")
    arquivo.writelines(dados_arquivo)
    arquivo.write(f"\nMédia geral da turma: {media_geral:.2f}\n")

print(f"Dados salvos no arquivo: {nome_arquivo}")