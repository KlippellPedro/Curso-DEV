# Função para calcular o dibro de um numero
def dobro(valor):
    total = valor *2
    return total

# Função principal que executa o programa
def main():
    print("-- Sistema utilizando a função --")
    numero = float(input("Digite um número: "))

    resultado = dobro(numero)
    print(f"Valor do calculo realizado na função: {resultado}")

if __name__ == "__main__":
    main()