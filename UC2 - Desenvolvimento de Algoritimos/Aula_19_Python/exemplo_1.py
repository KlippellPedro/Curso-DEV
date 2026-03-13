# Função para calcular a soma dos elementos de uma lista
def calcular_soma(lista):
    # A função sum é nativa do python e soma todos os elementos da lista
    return sum(lista)

# Função para encontrar o maior valor na lista
def encontrar_maior(lista):
    # A função max retorna o maior valor de uma lista
    return max(lista)

# Função para encontrar o menor valor na lista
def encontrar_menor(lista):
    # A função min retorna o menor valor de uma lista
    return min(lista)

# Função para calcular a media dos valores da lista
def calcular_media(lista):
    # A media é a soma dos elementos divididos pelo numero de elementos
    return sum(lista) / len(lista)

# Função para contar os numeros pares na lista
def contar_pares(lista):
    return len([num for num in lista if num % 2== 0])

# Criar a função principal que executa as operações
def main():
    # Solicita ao usuario que insira 5 numeros inteiros
    lista = []
    for i in range(5):
        num = int(input(f"Digite o {i+1}ª número: "))
        lista.append(num)
    
    # Exibir os resultados de todas as operações, utilizando as funções definidas
    print("")
    print("--- Chamando as funções ---")
    print(f"Soma dos números: {calcular_soma(lista)}")
    print(f"Maior número: {encontrar_maior(lista)}")
    print(f"Menor número: {encontrar_menor(lista)}")
    print(f"Média dos números: {calcular_media(lista)}")
    print(f"Quantidade de números pares: {contar_pares(lista)}")

# Executar a função principal
if __name__ == "__main__":
    main()