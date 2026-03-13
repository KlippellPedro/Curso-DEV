# Sistema que vai perguntar quantas pessoas deseja cadastrar
quantidade = int(input("Quantas pessoas deseja cadastrar: "))
maior = 0
nomemaior = ""
for i in range(1, quantidade +1):
    print(f"\n Pessoa: {1}")
    nome = input("Digite o nome da pessoa: ")
    idade = int(input("Digite a idade da pessoa: "))
    print("")
    print(f"Nome da pessoa: {nome}")
    print(f"Idade da pessoa: {idade}")
    print("")
    if idade > maior:
        nomemaior = nome
        maior = idade
print("")
print(f"Nome da pessoa com a maior idade: {nomemaior}")
print(f"Idade da pessoa mais velha: {maior}")