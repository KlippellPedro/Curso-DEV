# Vamos criar uma matriz de 2x2 vazia
matriz = [[0, 0], [0, 0]]
# Preenchendo a matriz com valores do usuario
for i in range(2): # Loop de 0 a 1
    for j in range(2):
        # Solicita ao ususario um numero para cada posição da matriz
        matriz[i][j] = int(input(f"Digite um número na posição [{i+1}, {j+1}]: "))

# Exibição dos valores da matriz nas posições
print("")
print(f"O valor que está na posição [1,1] é: {matriz[0][0]}")
print(f"O valor que está na posição [1,2] é: {matriz[0][1]}")
print(f"O valor que está na posição [2,1] é: {matriz[1][0]}")
print(f"O valor que está na posição [2,2] é: {matriz[1][1]}")
