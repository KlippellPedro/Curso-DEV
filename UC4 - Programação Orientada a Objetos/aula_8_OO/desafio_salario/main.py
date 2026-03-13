from aumento import Aumento
def main():
    print("-- Empresa Klippel LTDA --\n")
    salario= float(input("Digite o salario do funcionario: "))
    print("A - Aumento de 35%")
    print("B - Aumento de 30%")
    print("C - Aumento de 25%")
    print("D - Aumento de 20%")
    print("E - Aumento de 15%")
    categoria= input("\nDigite a categoria do aumento: ").upper()
    
    calc=Aumento(categoria,salario)
    salario_novo= calc.calculo_aumento()
    aumento= calc.calculo_salario_novo()

    print("\n","-"*30,"\n")

    print(f"Salário bruto: {salario}")
    print(f"Categoria do aumento: {categoria}")
    print(f"Valor do aumento: {aumento}")
    print(f"Salário com aumento: {salario_novo+aumento}")

main()
