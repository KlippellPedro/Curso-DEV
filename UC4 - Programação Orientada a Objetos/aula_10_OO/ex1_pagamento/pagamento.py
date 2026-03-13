'''
Classe responsavel por calcular o valor final da compra
com base na forma de pagamento
'''
class Pagamento:
    def __init__(self,valor:float,opcao:int):
        self.valor=valor
        self.opcao=opcao
        
    def calcular_pagamento(self):
        '''
        Método para calcular o valor final da compra
        aplicando desconto ou acréscimo, conforme
        a opção escolhida
        '''
        match self.opcao:
            case 1:
                return self.valor*0.90 # 10% de desconto
                # return self.valor=self.valor-(self.valor*0.1)
            case 2:
                return self.valor*0.95 # 5% de desconto
            case 3:
                return self.valor # Valor normal
            case 4:
                return self.valor*1.05 # 5% de acréscimo
            case 5:
                return self.valor*0.92 # 8% de desconto
            case 6:
                return self.valor*1.07 # 7% de acréscimo
            