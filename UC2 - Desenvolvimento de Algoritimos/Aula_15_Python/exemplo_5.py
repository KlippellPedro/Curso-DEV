# Fup para um sistema escolar
quantidade = int(input("Quantas pessoas deseja cadastrar: "))
for i in range(1, quantidade +1):
    print(f"\n Aluno: {i}")
    nome = input("Digite o nome do aluno: ")
    turma = int(input("Digite a turma do aluno: "))
    n1 = int(input("Digite a 1° nota do aluno: "))
    n2 = int(input("Digite a 2° nota do aluno: "))
    n3 = int(input("Digite a 3° nota do aluno: "))
    print("")
    print(f"Nome da pessoa: {nome}")
    print(f"Turma do aluno: {turma}")
    print(f"1° nota: {n1}")
    print(f"2° nota: {n2}")
    print(f"3° nota: {n3}")
    media= (n1+n2+n3)/3
    print(f"Média final: {media}")
    print(f"Situação curricular: ",end="")
    if media >= 7:
        print("Aprovado")
    elif media >= 5:
        print("Recuperação")
    else:
        print("Reprovado")