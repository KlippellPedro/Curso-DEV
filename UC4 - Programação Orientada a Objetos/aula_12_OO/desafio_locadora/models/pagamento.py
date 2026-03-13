class Pagamento:
    def __init__(self,total):
        self.total=total
    def calcular_pagamento(self,opcao:int):
        if opcao==1:
            return self.total*0.90,"A vista em dinheiro ou Pix - 10% de Desconto"
        elif opcao==2:
            return self.total*.95,"Cartão de débito - 5% de Desconto"
        elif opcao==3:
            return self.total,"Cartão de crédito 30 dias - Mesmo valor"
        elif opcao==4:
            return self.total*1.05,"Cartão de crédito 2X - 5% de Acréscimo"
        elif opcao==5:
            return self.total*1.10,"Cartão de crédito 3X - 10% de Aréscimo"
        else:
            raise ValueError("Opção de pagamento inválido!")
        