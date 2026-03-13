from calculadora import Calculadora
def main():
    print("-- Calculadora Klippel --\n")
    n1=int(input("Informe o primeiro número: "))
    n2=int(input("Informe o segundo número: "))
    print("\n--- Menu de operações matemáticas ---\n")
    print("1 - Adição")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão\n")
    operacao=int(input("Digite uma opção (1 a 4): "))
    calc=Calculadora(n1,n2,operacao) # Cria um objeto Calculadora com os dados informados
    resultado= calc.calcular() # Executa o cálculo e recebe o resultado ou mensagem de erro
    print(resultado)
# Pode chamar o main dessas duas formas
main()
'''
if __name__=="__main__:
    main()
'''