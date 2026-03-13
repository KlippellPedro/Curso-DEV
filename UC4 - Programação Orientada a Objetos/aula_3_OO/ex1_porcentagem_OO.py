'''
Vamos criar um exemplo para trabalhar com porcentagens
'''
class CalculadoraPorcentagem:
    '''
    Classe para realizar cálculos de acréscimo e desconto em
    porcentagem sobre um valor
    '''
    def __init__(self, valor):
        '''
        Método contrutor, inicializa o objeto com o valor base 
        para os cálculos.
        '''
        self.valor = valor
    
    def acrescimo(self, percentual):
        '''
        Método para calcular o valor com acéscimo percentual.
        '''
        return self.valor+(self.valor*percentual)
    
    def desconto(self,percentual):
        '''
        Calcula o valor com desconto percentual.
        '''
        return self.valor-(self.valor*percentual)
    
if __name__ == "__main__":
    print("-- Exemplo da Porcentagem Dentro do Código --")
    valor = int(input("\nDigite um valor inteiro: "))

    # Instância da classe
    calc = CalculadoraPorcentagem(valor)
    # Exemplo de acrécimos
    print(f"\nValor com 10% de acrécimo: {calc.acrescimo(0.10)}")
    print(f"Valor com 27% de acrécimo: {calc.acrescimo(0.27)}")
    print(f"Valor com 31% de acrécimo: {calc.acrescimo(0.31)}")
    print(f"Valor com 9% de acrécimo: {calc.acrescimo(0.09)}")
    print(f"Valor com 5% de acrécimo: {calc.acrescimo(0.05)}")
    print(f"Valor com 150% de acrécimo: {calc.acrescimo(1.50)}")

    print("\n","-"*40,"\n")

    print(f"Valor com 30% de desconto: {calc.desconto(0.30)}")
    print(f"Valor com 100% de desconto: {calc.desconto(1.00)}")
    print(f"Valor com 4% de desconto: {calc.desconto(0.04)}")
    print(f"Valor com 1% de desconto: {calc.desconto(0.01)}")