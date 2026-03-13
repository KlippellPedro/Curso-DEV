# Criação de uma lista vazia que armazene os 5 números digitados pelo usuario
num = []
# Lista de ordinais para exibir mensagens persolnalizadas para o usuario
ordinais = ["primeiro", "segundo", "terceiro", "quarto", "quinto"]

# Loop para ler os 5 números do usuario
for i in range(5):
    # Solicita o número ao usuario, com a posição correspondente
    valor = int(input(f"Digite o {ordinais[i]} número: "))
    num.append(valor) # Adiciona o valor digitado a lista num

# Exibição dos numeros digitados
print("")
# Loop para exibir cada numero na ordem que foi digitado
for i in range(5):
    # Mostra o ordinal e o valor correspondente na lista
    print(f"{ordinais[i].capitalize()} número digitado: {num[i]}")