class Clinica_de_saude():
    def __init__(self, peso, altura):
        self.peso= peso
        self.altura= altura

    def calculo_imc(self):
        return  self.peso / (self.altura*self.altura)

if __name__ == "__main__":
    print("-- Clinica de Saúde --")
    peso = float(input("\nDigite o peso do paciente: "))
    altura = float(input(f"Digite a altura do paciente: "))
    
    print("\n","-"*40,"\n")

    calc = Clinica_de_saude(peso,altura)
    imc = calc.calculo_imc()

    if calc.calculo_imc() < 18.5:
        print(f"IMC: {imc:.2f}")
        print(f"Rsultado: Abaixo do Peso")
    elif calc.calculo_imc() >=18.5 and calc.calculo_imc() <=24.9:
        print(f"IMC: {imc:.2f}")
        print(f"Rsultado: Peso Normal")
    elif calc.calculo_imc() >=25 and calc.calculo_imc() <=29.9:
        print(f"IMC: {imc:.2f}")
        print(f"Rsultado: Sobrepeso")
    elif calc.calculo_imc() >30:
        print(f"IMC: {imc:.2f}")
        print(f"Rsultado: Obesidade")
    else:
        print(f"Digite valores Validos")
