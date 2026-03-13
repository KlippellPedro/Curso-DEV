# Criação de uma lista com 5 posições, todas iniciando com valor 0
num = [0] * 5 # Lista que simula o vetor[1..5]

# Solicitar ao usuário que digite números inteiros e armazene na lista
num[0] = int(input("Digite o primeiro número: "))
num[1] = int(input("Digite o segundo número: "))
num[2] = int(input("Digite o terceiro número: "))
num[3] = int(input("Digite o quarto número: "))
num[4] = int(input("Digite o quinto número: "))

# Exibir os números digitados na mesma ordem em que foram inseridos
print("")
print(f"Primeiro número digitado: {num[0]}")
print(f"Segundo número digitado: {num[1]}")
print(f"Terceiro número digitado: {num[2]}")
print(f"Quarto número digitado: {num[3]}")
print(f"Quinto número digitado: {num[4]}")
