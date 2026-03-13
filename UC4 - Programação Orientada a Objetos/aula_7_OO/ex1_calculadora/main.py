from calculadora import Calculadora

def main():
    print("-- Sistema de Calculadora Básica --\n")
    n1= float(input("Digite o primeiro número: "))
    n2= float(input("Digite o segundo número: "))

    print("\n--- Menu de Opções ---\n")
    print("1 - Adição")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")

    opcao= int(input("\nSelecione uma das opções: "))
    print("\n","-"*30,"\n")
    calc= Calculadora(n1,n2,opcao)
    resultado=calc.calcular()
    
    if resultado is None:
        if opcao == 4 and n2 == 0:
            print("Erro: divisão por 0 não é permitida!")
        else:
            print("Você escolheu uma operação matemática que não existe no sistema!")
    else:
        print(f"Resultado da operação matemática: {resultado:.1f}")

if __name__ == "__main__":
    main()