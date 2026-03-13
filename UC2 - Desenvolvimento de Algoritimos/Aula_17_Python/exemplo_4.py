# Criar um sistema de notas com vetor
print(" Sistema de notas com vetor ")
print("")
nome = input("Digite o nome do aluno: ")
turma = input("Digite a turma do aluno: ")
quantidade = int(input("Digite quantas notas deseja registrar: "))
# Criar uma lista vazia para armazenar as notas
nota = []

# Lopp para ler cada nota
for i in range(quantidade):
    valor = float(input(f"Digite a {i+1}ª nota: "))
    nota.append(valor) # Adiciona a nota a lista

# Calcular a media das notas
media = sum(nota)/5

print("")
print(f"Nome do aluno: {nome}")
print(f"Turma: {turma}")

# Exibe todas as notas digitadas
for i in range(quantidade):
    print(f"Nota {i+1}: {nota[i]}")

print(f"Média final: {media:.1f}")