# Sistema vai solicitar quantas linhas e quantas colunas deseja informar

# Solicitar ao usuario o numero de linhas e colunas para matriz
linhas = int(input("Digite o número de linhas da matriz: "))
colunas = int(input("Digite o número de colunas da matriz: "))

# Criar a matriz com o tamanho especificado
matriz = [[0 for _ in range(colunas)] for _ in range(linhas)]

soma_total = 0
maior_valor = None
valores_pares = []

# Leitura da matriz e processamento dos dados
for i in range(linhas):
    for j in range(colunas):
        valor = int(input(f"Digite o número para posição [{i+1}, {j+1}]: "))
        matriz[i][j] = valor
        soma_total += valor

        if valor % 2 == 0:
            valores_pares.append(valor)

        # Define o maior valor
        if maior_valor is None or valor > maior_valor:
            maior_valor = valor

# Calcula a media dos valores da matriz
total_elemento = linhas * colunas
media = soma_total / total_elemento

# Exibição da matriz formatada
for linha in matriz:
    for item in linha:
        print(f"{item:4}", end="") # Imprimir com alinhamento
    print("")

# Resultados finais
print("\n Resultados da análise: ")
print(f"Soma do total dos elementos: {soma_total}")
print(f"Média dos valores: {media:.1f}")
print(f"Maior valor encontrado: {maior_valor}")
print(f"Números pares encontrados: {valores_pares}")