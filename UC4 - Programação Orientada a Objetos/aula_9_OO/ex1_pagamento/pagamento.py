class Pagamento:
    def __init__(self,cliente):
        self.cliente=cliente
        self.valor_final=0

    def calcular_pagamento(self,opcao):
        '''
        Método para calcular o valor final de acordo
        com a opção de pagamento escolhido
        '''
        venda=self.cliente.valor_compra

        # Usar o match-case para determinar o tipo de pagamento
        match opcao:
            case 1:
                self.valor_final= venda-(venda*0.10)
            case 2:
                self.valor_final= venda-(venda*0.05)
            case 3:
                self.valor_final= venda
            case 4:
                self.valor_final= venda+(venda*0.05)
            case 5:
                self.valor_final= venda-(venda*0.08)
            case 6:
                self.valor_final= venda-(venda*0.07)
            case _:
                self.valor_final=None
        return self.valor_final