# Sistema que pergunte quantas pessoas deseja cadastrar o nome e idade
# Verificar a pessoa com a maior idade
# Media das idades
pessoas = []
# While para solocitar quantas pessoas serão informadas
while True:
    try:
        quantidade = int(input("Quantas pessoas deseja informar: "))
        if quantidade > 0:
            break
        else:
            print("Por favor, informe um número positivo.")
    except ValueError:
        print("Digite um número inteiro válido!")

soma = 0
maior = -1
nome_maior = ""

# Leitura dos dados
for i in range(1, quantidade + 1):
    print(f"\nCadastro da {i}ª pessoa: ")
    nome = input("Digite o nome: ")

    # Validação da idade
    while True:
        try:
            idade = int(input("Digite a idade: "))
            if idade >= 0:
                break
            else:
                print("A idade não pode ser negativa.")
        except ValueError:
            print("Digite uma idade válida (número inteiro).")
    
    pessoas.append({"nome": nome, "idade": idade})
    soma += idade

    # Verificar a maior idade
    if idade > maior:
        maior = idade
        nome_maior = nome

# Exibe quem tem mais de 25 anos
print("\nPessoa com mais de 25 anos: ")
encontrou = False
for idx, pessoa in enumerate(pessoas):
    if pessoa["idade"] > 25:
        print(f"- {pessoa["nome"]} (posição {idx + 1})")
        encontrou = True

if not encontrou:
    print("Nenhuma pessoa com mais de 25 anos foi registrada.")

# Exibe a maior e quem possui
print(f"\nA maior idade digitada foi: {maior}")
print(f"Pessoa com maior idade: {nome_maior}")
media = soma / quantidade
print(f"Média das idades digitada {media:.1f}")