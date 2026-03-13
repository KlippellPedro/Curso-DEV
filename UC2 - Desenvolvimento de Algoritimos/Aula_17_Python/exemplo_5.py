# Criar um sistema de notas com vetor
op = "s"
while op.lower() == "s":
    print("--------------- Sistema de notas com vetor ---------------")
    print("")
    nome = input("Digite o nome do aluno: ")
    turma = input("Digite a turma do aluno: ")
    quantidade = int(input("Digite quantas notas deseja registrar: "))
    nota = []
    for i in range(quantidade):
        valor = float(input(f"Digite a {i+1}ª nota: "))
        nota.append(valor)
    media = sum(nota)/5
    print("")
    print(f"Nome do aluno: {nome}")
    print(f"Turma: {turma}")
    for i in range(quantidade):
        print(f"Nota {i+1}: {nota[i]}")
    print(f"Média final: {media:.1f}")
    print(f"Situação curricular: ",end="")
    if media >= 7:
        print("Aprovado")
    elif media >=5:
        print("Recuperação")
    elif media <5:
        print("Reprovado")
    print("")
    op = input("Deseja fazer uma nova compra? (S/N): ")
    print("")