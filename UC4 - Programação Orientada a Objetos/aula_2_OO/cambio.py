class Cambio:
    def __init__(self):
        self.real= 0.0
        self.dolar= 0.0
        self.euro=0.0
        self.cotacao_dolar=0.0
        self.cotacao_euro=0.0
        self.escolha= 0

    def coletar_dados(self):
        print("-- Sistema de Câmbio --")
        print("")
        self.real= float(input("Quantos reais deseja converter: "))
        self.cotacao_dolar= float(input("Qual a cotação do dolar atualmente: "))
        self.cotacao_euro= float(input("Qual a cotação do euro atualmente: "))
    
    def calculo_cambio(self):
        self.calcaulo_dolar= self.real/self.cotacao_dolar
        self.calculo_euro= self.real/self.cotacao_euro
    
    def exibir_dados(self):
        print("")
        print(f"Real convertido: {self.real}")
        print(f"Dolar convertido: {self.calcaulo_dolar:.2f}")
        print(f"Euro convertido: {self.calculo_euro:.2f}")

if __name__ == "__main__":
    sistema = Cambio()
    sistema.coletar_dados()
    sistema.calculo_cambio()
    sistema.exibir_dados()