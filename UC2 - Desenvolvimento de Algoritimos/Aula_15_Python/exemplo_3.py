# Sistema para ler 5 dados de uma pessoa e veirficar qual pessoa é mais velha
maior= 0
nomemaior = str("")
# Estrutura de repetição para ler os dados de 5 pessoas
for i in range(1, 6):
    nome = input("Digite um nome: ")
    idade = int(input("Digite a idade: "))
    print("")
    print(f"Nome da pessoa: {nome}")
    print(f"Idade da pessoa {idade}")
    if idade > maior:
        nomemaior = nome
        maior = idade
# Exibir o resultado final
print("")
print(f"Nome da pessoa com a maior idade: {nomemaior}")
print(f"Idade da pessoa mais velha: {maior}")