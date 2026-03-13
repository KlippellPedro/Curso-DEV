# Criar um sistema de notas com vetor
print(" Sistema de notas com vetor ")
print("")
nome = input("Digite o nome do aluno: ")
turma = input("Digite a turma do aluno: ")
# Criar uma lista chamada nota para armazenar as 5 notas
nota = []

nota.append(int(input("Digite a primeira nota: "))) # nota[0]
nota.append(int(input("Digite a segunda nota: "))) # nota[1]
nota.append(int(input("Digite a terceira nota: "))) # nota[2]
nota.append(int(input("Digite a quarta nota: "))) # nota[3]
nota.append(int(input("Digite a quinta nota: "))) # nota[4]

# Calcular a média das notas digitadas
# media = (nota[0]+nota[1]+nota[2]+nota[3]+nota[4])/5
media = sum(nota)/5

print("")
print(f"Nome do aluno: {nome}")
print(f"Turma do aluno: {turma}")
print(f"Primeira nota: {nota[0]}")
print(f"Segunda nota: {nota[1]}")
print(f"Terceira nota: {nota[2]}")
print(f"Quarta nota: {nota[3]}")
print(f"Quinta nota: {nota[4]}")
print(f"Média final: {media}")