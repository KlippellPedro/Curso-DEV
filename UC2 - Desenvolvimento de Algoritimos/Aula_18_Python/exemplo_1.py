# Sistema para solicitar a idade de algumas pessoas
# Verificar a pessoa mais velha
# Verificar as pessoas com mais de 45 anos e a posição
# Média das idades

# Inicialização da variavel qie vai receber a lista de idades
idade = []
# Inicialização de algumas variaveis que serão utilizadas
soma = 0
maior= 0
posi = 0
c = 0
# Entrada de dados: leitura de 8 idades
for c in range(1, 9):
    valor = int(input(f"Digite a idade da {c}ª pessoa: "))
    idade.append(valor)
    soma += valor

# Verificação com pessoas com mais de 25 anos
for c in range(8): # Indicie de 0 a 7
    if idade[c] > 25:
        print("")
        print(f"Pessoa com mais de 25 anos na posição {c + 1}")

# Encontrar a maior idadde no vetor
for c in range(8):
    if idade[c] > maior:
        maior = idade[c]

print("")
print(f"A maior idade digitada foi: {maior}")
media = soma/8
print(f"Média das idades digitadas: {media:.1f}")