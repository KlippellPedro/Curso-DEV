from calculadora import Calculadora
def main():
    print("-- Calculadora Klippel --\n")
    n1=int(input("Informe o primeiro número: "))
    n2=int(input("Informe o segundo número: "))
    operacao=str(input("Digite o sismbolo da operação matemática: "))
    calc=Calculadora(n1,n2,operacao) # Cria um objeto Calculadora com os dados informados
    resultado= calc.calcular() # Executa o cálculo e recebe i resultado ou mensagem de erro
    print(resultado)
# Pode chamar o main dessas duas formas
main()
'''
if __name__=="__main__:
    main()
'''